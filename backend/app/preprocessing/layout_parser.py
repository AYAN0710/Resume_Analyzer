import torch
import numpy as np
from PIL import Image
from transformers import LayoutLMv3Processor
from app.config.settings import settings
from app.config.model_config import model_manager,DEVICE
from app.utils.logger import logger
from app.utils.timer import measure_time

layout_processor=LayoutLMv3Processor.from_pretrained(
    settings.LAYOUT_MODEL,
    apply_ocr=False
)

def normalize_box(box,width,height):
    x0,y0,x1,y1=box
    return [
        int(1000*x0/width),
        int(1000*y0/height),
        int(1000*x1/width),
        int(1000*y1/height)
    ]
    
def validate_box(box):
    return [max(0,min(1000,value)) for value in box]

def prepare_ocr_data(ocr_results,image_width,image_height):
    words=[]
    boxes=[]
    for result in ocr_results:
        coordinates=result[0]
        text=result[1]
        confidence=result[2]
        if confidence < 0.30:
            continue
        text=text.strip()
        if not text:
            continue
        xs=[point[0] for point in coordinates]
        ys=[point[1] for point in coordinates]
        box=[min(xs),min(ys),max(xs),max(ys)]
        box=normalize_box(box,image_width,image_height)
        box=validate_box(box)
        words.append(text)
        boxes.append(box)
    return words,boxes

#create layout presentation
@measure_time("LayoutLM Processing")
def analyze_page(image,words,boxes):
    model=model_manager.load_layout_model()
    image=image.convert("RGB")
    encoded=layout_processor(image,words,boxes=boxes,return_tensors="pt",truncation=True,padding="max_length",max_length=512)
    encoded={key: value.to(DEVICE) for key,value in encoded.items()}
    with torch.inference_mode():
        outputs=model(**encoded)
    hidden_states=outputs.last_hidden_state
    page_embedding=hidden_states[:,0,:]
    return {
        "hidden_states":hidden_states,
        "page_embedding":page_embedding,
        "words":words,
        "boxes":boxes
    }

#process complete pdf
@measure_time("Complete Layout Analysis")
def process_layout(pdf_path):
    logger.info(f"Starting layout analysis: {pdf_path}")
    import fitz
    pdf=fitz.open(pdf_path)
    import easyocr
    reader=easyocr.Reader(["en"],gpu=settings.USE_GPU)
    pages=[]
    for page_number,page in enumerate(pdf):
        logger.info(f"Processing layout page {page_number+1}")
        pixmap=page.get_pixmap(dpi=200,alpha=False)
        image=Image.frombytes("RGB",[pixmap.width,pixmap.height],pixmap.samples)
        ocr_results=reader.readtext(np.array(image),detail=1)
        words,boxes=prepare_ocr_data(ocr_results,image.width,image.height)
        layout_result=analyze_page(image,words,boxes)
        pages.append({
            'page_number':page_number+1,
            "words":words,
            "boxes":boxes,
            'pages_embedding':layout_result["page_embedding"].detach().cpu().numpy().tolist()
        })
    pdf.close()
    logger.success("Layout analysis completed.")
    return pages
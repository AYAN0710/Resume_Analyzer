import fitz
import easyocr
import numpy as np
from PIL import Image
from app.utils.logger import logger
from app.utils.timer import measure_time
from app.config.settings import settings

reader=easyocr.Reader(['en'],gpu=settings.USE_GPU)

@measure_time("Resume Parsing")
def load_pdf(file_path:str):
    logger.info(f"Opening PDF: {file_path}")
    pdf=fitz.open(file_path)
    return pdf

@measure_time("PDF Inspection")
def is_text_pdf(pdf):
    for page in pdf:
        text=page.get_text()
        if text.strip():
            return True
    return False

@measure_time("Text Extraction")
def extract_text(pdf):
    logger.info("Extracting Text...")
    complete_text=""
    for page in pdf:
        complete_text+=page.get_text()
        complete_text+="\n"
    return complete_text

@measure_time("OCR")
def extract_using_ocr(pdf):
    logger.warning("Scanned PDF Detected.")
    complete_text=""
    for page in pdf:
        pix=page.get_pixmap(dpi=300)
        image=Image.frombytes(
            "RGB",[pix.width,pix.height],pix.samples
        )
        result=reader.readtext(np.array(image),detail=0)
        complete_text+=" ".join(result)
        complete_text+="\n"
    return complete_text

@measure_time("Complete PDF Loading")
def process_resume(file_path:str):
    pdf=load_pdf(file_path)
    if is_text_pdf(pdf):
        logger.success("Text PDF Detected.")
        text=extract_text(pdf)
    else:
        text=extract_using_ocr(pdf)
    pdf.close()
    return text
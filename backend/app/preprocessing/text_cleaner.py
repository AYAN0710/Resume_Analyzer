import re
import unicodedata
from app.utils.logger import logger
from app.utils.timer import measure_time

def normalize_unicode(text:str) -> str:
    return unicodedata.normalize("NFKC",text)

def normalize_line_breaks(text:str) ->str:
    text=text.replace("\r\n","\n")
    text.replace("\r","\n")
    return text

def normalize_spaces(text:str)->str:
    text=re.sub(r"[\t]+"," ",text)
    return text

def normalize_blank_lines(text:str)->str:
    return re.sub(r"\n{3,}","\n\n",text)

def remove_pdf_artifacts(text:str)->str:
    cleaned_characters=[]
    for character in text:
        if character=="\n":
            cleaned_characters.append(character)
            continue
        if unicodedata.category(character)=="Cc":
            continue
        cleaned_characters.append(character)
    return "".join(cleaned_characters)
    
def fix_line_break_hyphenation(text:str)->str:
    return re.sub(r"([A-Za-z]{3,})-\n([A-Za-z]{3,})", r"\1-\2",text)

def clean_lines(text:str)->str:
    lines=text.split("\n")
    cleaned_lines=[]
    for line in lines:
        line=line.strip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

@measure_time("Text Cleaning")
def clean_resume_text(text:str)->str:
    logger.info("Starting resume text cleaning.")
    if not text:
        logger.warning("Empty resume text recieved.")
        return ""
    text=normalize_unicode(text)
    text=normalize_line_breaks(text)
    text=fix_line_break_hyphenation(text)
    text=remove_pdf_artifacts(text)
    text=normalize_spaces(text)
    text=normalize_blank_lines(text)
    text=clean_lines(text)
    logger.success("Resume cleaning completed.")
    return text.strip()
    
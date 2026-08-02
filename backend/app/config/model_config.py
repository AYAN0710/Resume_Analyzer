import torch
import google.generativeai as genai
from transformers import AutoTokenizer,AutoModel,AutoModelForSequenceClassification,AutoModelForTokenClassification,LayoutLMv3Model,LayoutLMv3Processor
from sentence_transformers import SentenceTransformer
from app.config.settings import settings

DEVICE=torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ModelManager:
    
    def __init__(self):
        self.layout_processor=None
        self.layout_model=None
        self.embedding_model=None
        self.reranker_tokenizer=None
        self.reranker_model=None
        self.skill_tokenizer=None
        self.skill_model=None
        self.ner_tokenizer=None
        self.ner_model=None
        self.gemini=None
        
    def load_layout_model(self):
        if self.layout_model is None:
            print("loading LayoutLMv3...")
            self.layout_processor=LayoutLMv3Processor.from_pretrained(settings.LAYOUT_MODEL)
            self.layout_model=(LayoutLMv3Processor.from_pretrained(settings.LAYOUT_MODEL).to(DEVICE))
        return self.layout_model
    
    def load_embedding_model(self):
        if self.embedding_model is None:
            print("Loading Embedding model....")
            self.embedding_model=SentenceTransformer(settings.EMBEDDING_MODEL,device=str(DEVICE))
        return self.embedding_model
    
    def load_reranker(self):
        if self.reranker_model is None:
            print("Loading reranker model...")
            self.reranker_tokenizer=AutoTokenizer.from_pretrained(settings.RERANKER_MODEL)
            self.reranker_model=(AutoModelForSequenceClassification.from_pretrained(settings.RERANKER_MODEL).to(DEVICE))
        return self.reranker_model
    
    def load_skill_model(self):
        if self.skill_model is None:
            print("Loading skill model...")
            self.skill_tokenizer=AutoTokenizer.from_pretrained(settings.SKILL_MODEL)
            self.skill_model=(AutoModelForTokenClassification.from_pretrained(settings.SKILL_MODEL).to(DEVICE))
        return self.skill_model
    
    def load_ner_model(self):
        if self.ner_model is None:
            print("Loading NER model...")
            self.ner_tokenizer=AutoTokenizer.from_pretrained(settings.NER_MODEL)
            self.ner_model=(AutoModelForTokenClassification.from_pretrained(settings.NER_MODEL).to(DEVICE))
        return self.ner_model
        
    def load_gemini(self):
        if self.gemini is None:
            print("Gemini LLM Loading...")
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.gemini=genai.GenerativeModel("gemini-3.1-flash-lite")
        return self.gemini
    
    def load_all_models(self):
        self.load_layout_model()
        self.load_embedding_model()
        self.load_reranker()
        self.load_skill_model()
        self.load_ner_model()
        self.load_gemini()
        print("All models loaded successfully !")
        
model_manager=ModelManager()
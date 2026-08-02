from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict

BASE_DIR=Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    DEBUG:bool
    
    #fastapi
    HOST:str
    PORT:int
    
    #PostgreSQL
    DB_HOST:str
    DB_PORT:int
    DB_NAME:str
    DB_USER:str
    DB_PASSWORD:str
    
    #redis
    REDIS_HOST:str
    REDIS_PORT:int
    
    #Qdrant
    QDRANT_HOST:str
    QDRANT_PORT:int
    
    #Gemini
    GEMINI_API_KEY:str
    
    #upload
    UPLOAD_FOLDER:str
    MAX_UPLOAD_SIZE:int
    ALLOWED_EXTENSIONS:str
    
    #logs
    LOG_FOLDER:str
    LOG_LEVEL:str
    
    #models
    EMBEDDING_MODEL:str
    RERANKER_MODEL:str
    LAYOUT_MODEL:str
    SKILL_MODEL:str
    NER_MODEL:str
    OCR_MODEL:str
    
    #vector database
    COLLECTION_NAME:str
    VECTOR_DIMENSION:int
    DISTANCE_METRIC:str
    
    #Performance
    CACHE_TTL:int
    USE_GPU:bool
    BATCH_SIZE:int
    MAX_CHUNK_SIZE:int
    CHUNK_OVERLAP:int
    TOP_K:int
    RERANK_TOP_K:int
    
    #benchmark
    ENABLE_BENCHMARK:bool
    SAVE_LATENCY:bool
    SAVE_MEMORY_USAGE:bool
    
    @property
    def UPLOAD_PATH(self):
        return BASE_DIR/self.UPLOAD_FOLDER
    
    @property
    def LOG_PATH(self):
        return BASE_DIR/self.LOG_FOLDER
    
    @property
    def DATABASE_URL(self):
        return (
            f"postgresql://"
            f"{self.DB_USER}"
            f"{self.DB_HOST}"
            f"{self.DB_PORT}"
            f"{self.DB_NAME}"
        )

model_config=SettingsConfigDict(
    env_file=BASE_DIR/".env",
    env_file_encoding="utf-8",
    extra="ignore"
)

settings=Settings()
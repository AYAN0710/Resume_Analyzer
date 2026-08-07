#project constants 
SUPPORTED_FILE_TYPES=["pdf"]

RESUME_SECTIONS=[
    "summary","education","experience","projects","skills","certifications","achievements","internships","languages","publications"
]

COMMON_SKILLS=[
    "python","java","c++","javascript","typescript","react","nextjs","nodejs","fastapi","django","flask","spring boot","sql",
    "mongodb","postgresql","redis","docker","kubernetes","aws","azure","gcp","tensorflow","pytorch","langchain","langgraph","rag","vectordatabase",
    "machine learning","deep learning","nlp","computer vision","opencv","git","github"
]

ACTION_VERBS=[
    "developed","designed","implemented","optimized","built","created","engineered","imporved","deployed","integrated",
    "automated","trained","analyzed","achieved","managed","led","reduced","increased"
]

WEAK_WORDS=[
    "worked","helped","did","made","good","nice","various","many","some"
]

ATS_WEIGHTS={
    "skills":30,
    "experience":25,
    "projects":20,
    "education":10,
    "grammar":5,
    "keywords":10
}

PERFORMANCE_TARGETS={
    "resume_parsing":1.0,
    "embedding_generation":0.3,
    "vector_search":0.1,
    "reranking":0.2,
    "llm_response":2.0,
    "total_response":4.0
}

BENCHMARK_STATUS={
    "excellent":"green",
    "good":"blue",
    "average":"orange",
    "poor":"red"
}
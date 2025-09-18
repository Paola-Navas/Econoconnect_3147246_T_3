from fastapi import APIRouter, HTTPException
from models.News import News
from services import news_data
from datetime import datetime

router = APIRouter(prefix="/news", tags=["News"])

@router.post("/create", status_code=201)
def create_news(news: News):
    return news_data.add_news(news)

@router.get("/drafts")
def get_drafts():
    return [n for n in news_data.news_db if not n.published]

@router.post("/{news_id}/publish")
def publish_news(news_id: int):
    for n in news_data.news_db:
        if n.id == news_id:
            n.published = True
            n.published_at = datetime.utcnow()
            return n
    raise HTTPException(status_code=404, detail="Noticia no encontrada")

@router.get("/")
def get_published():
    return [n for n in news_data.news_db if n.published]

from models.News import News

news_db = []

def add_news(news: News):
    news.id = len(news_db) + 1
    news_db.append(news)
    return news

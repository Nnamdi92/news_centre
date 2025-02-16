# DAO/db_queries.py
CREATE_DATABASE_QUERY = "CREATE DATABASE IF NOT EXISTS news_db;"
 
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    news_title VARCHAR(255) NOT NULL,
    media_house VARCHAR(100) NOT NULL,
    article_link TEXT NOT NULL,
    abstract TEXT,
    thumbnail TEXT,
    large_image TEXT,
    publisher VARCHAR(100),
    publish_date VARCHAR(255)
);
"""
 
CHECK_DATA_EXIST_QUERY = "SELECT 1 FROM news LIMIT 1;"
 
SAVE_DATA_QUERY = """
INSERT INTO news (news_title, media_house, article_link, abstract, thumbnail, large_image, publisher, publish_date)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""
 
 
# Query to fetch all news articles from the database
GET_ALL_NEWS_QUERY = "SELECT * FROM news;"
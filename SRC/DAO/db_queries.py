CREATE_DATABASE_QUERY = """CREATE DATABASE news_data"""

CREATE_TABLE_QUERY = """
CREATE TABLE news_data (
  news_id INT PRIMARY KEY AUTO_INCREMENT,
  news_title VARCHAR(255) NOT NULL,       
  media_house VARCHAR(255) NOT NULL,      
  article_link TEXT NOT NULL,             
  abstract TEXT NOT NULL,                 
  thumbnail VARCHAR(2083),                
  large_image VARCHAR(2083),              
  publisher VARCHAR(255) NOT NULL,                            
  publish_date VARCHAR(255)                        
);
"""
ALTER_TABLE_QUERY = """
ALTER TABLE news_data
MODIFY COLUMN publish_date VARCHAR(255);
"""

def SAVE_DATA_QUERY():
    return """INSERT INTO news_data
        (news_title, media_house, article_link, abstract, thumbnail, large_image, publisher, publish_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
 

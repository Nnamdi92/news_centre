import requests
from bs4 import BeautifulSoup
from constants.scrapper_constants import PUNCH_NEWS_URL
from pprint import pprint


def punch_scrapper_loop():
    print("Initializing punch scrapper......")
    final_data = []
    for page_number in range(1, 10):
        url = ""
        if page_number ==1:
            url = "https://punchng.com/topics/news/"
        else:
            url = f"{PUNCH_NEWS_URL}/{page_number}/"
        print(f"scrapping page {page_number} ....url = {url}")
        page_results = punch_scrapper(url)
        print(f".....done with scrapping page {page_number}......scrapping progress page {page_number} / {10}")
        final_data.append(page_results)
        print(f"scrapping done, Scrapping progress page {page_number} / {10}")
    return final_data[0]    

def punch_scrapper(url):
    clean_data = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    article_list = soup.find_all("article")
    
    for article in article_list:
        
        raw_news_title = article.find("h1", class_="post-title")
        if raw_news_title != None:
            news_data = {}
            news_title= raw_news_title.find("a").text.strip()
            news_data["news_title"]= news_title
            post_date = article.find("span", class_="post-date").text.strip()
            news_data["publish_date"] = post_date
            news_data["media_house"]= "punch"
            article_link = raw_news_title.find("a")["href"]
            news_data["article_link"] = article_link
            abstract = article.find("p", class_="post-excerpt").text.strip()
            news_data["abstract"] = abstract
            news_thumbnail = article.find("img", class_="post-image")["data-src"]
            news_data["thumbnail"] = news_thumbnail
            open_article_data = scrapeOpenArticle(article_link)
            news_data["large_image"] = open_article_data["large_image"]
            news_data["publisher"] = open_article_data["publisher"]

            clean_data.append(news_data)
    
    return(clean_data)


#this function opens each article, and pulls out the high resolution  image and the publisher of the news
def scrapeOpenArticle(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    image = soup.find("img", class_="post-image")["src"]
    try:
        raw_article_publisher = soup.find("span", class_="post-author")
        article_publisher = raw_article_publisher.find("a").text
    except Exception as e:
        article_publisher = "default_punch_publisher"
    return {"large_image": image, "publisher": article_publisher}

        
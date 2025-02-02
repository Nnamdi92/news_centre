import requests
from bs4 import BeautifulSoup
from constants.scrapper_constants import SUN_NEWS_URL
from pprint import pprint





def sun_scrappers():
    clean_data = []
    page = requests.get(SUN_NEWS_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    article_list = soup.find_all("a", class_="col-lg-4 archive-grid-single")

    for article in article_list:
        news_data = {}
        raw_news_title = article.find("h3", class_="archive-grid-single-title")
        if raw_news_title != None:
            news_title= raw_news_title.text
            news_data["news_title"]= news_title
            post_date = article.find("p", class_="post-date").find("span").text.strip()
            news_data["publish_date"] = post_date
            news_data["media_house"]= "sun"
            article_link = article["href"]
            news_data["article_link"] = article_link
    #         abstract = article.find("p", class_="post-excerpt").text.strip()
            news_data["abstract"] = "not done at the moment"
            news_thumbnail = article.find("img", class_="archive-grid-single-img")["data-src"]
            news_data["thumbnail"] = news_thumbnail
            open_article_data = scrapeOpenArticle(article_link)
            print(open_article_data)
            news_data["large_image"] = open_article_data["large_image"]
            news_data["publisher"] = open_article_data["publisher"]

        clean_data.append(news_data)
    
    return(clean_data)



def scrapeOpenArticle(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    image = soup.find("img", class_="post-image")["src"]
    try:
        raw_article_publisher = (
            soup.find("div", class_="post-content")
            .find("p", class_="p1")
            .find("b")
            .text
        )
    except Exception as e:
        raw_article_publisher = "sun news"
    return {"large_image": image, "publisher": raw_article_publisher}

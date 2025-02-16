import requests
from bs4 import BeautifulSoup
from constants.scrapper_constants import SUN_NEWS_URL
from pprint import pprint
 
 
def sun_scrappers():
    """Scrapes news articles from Sun News."""
    pprint("Initializing the sun scrapper....")
    clean_data = []
 
    try:
        page = requests.get(SUN_NEWS_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        article_list = soup.find_all("a", class_="col-lg-4 archive-grid-single")
 
        for article in article_list:
            news_data = {}
 
            try:
                raw_news_title = article.find("h3", class_="archive-grid-single-title")
                news_data["news_title"] = raw_news_title.text.strip() if raw_news_title else "Not found"
 
                post_date = article.find("p", class_="post-date").find("span")
                news_data["publish_date"] = post_date.text.strip() if post_date else "Not found"
 
                news_data["media_house"] = "Sun News"
 
                article_link = article.get("href", "Not found")
                news_data["article_link"] = article_link
 
                news_data["abstract"] = "Not done at the moment"
 
                news_thumbnail = article.find("img", class_="archive-grid-single-img")
                news_data["thumbnail"] = news_thumbnail["data-src"] if news_thumbnail else "Not found"
 
                if article_link != "Not found":
                    open_article_data = scrape_open_article(article_link)
                    news_data["large_image"] = open_article_data.get("large_image", "Not found")
                    news_data["publisher"] = open_article_data.get("publisher", "Not found")
                else:
                    news_data["large_image"] = "Not found"
                    news_data["publisher"] = "Not found"
 
            except Exception as e:
                pprint(f"Error processing article: {e}")
                continue  # Skip this article if any issue occurs
 
            clean_data.append(news_data)
 
    except requests.exceptions.RequestException as e:
        pprint(f"Error fetching Sun News page: {e}")
    
    return clean_data
 
 
def scrape_open_article(url):
    """Extracts high-resolution image and publisher details from an article."""
    pprint(f"Opening second stage scraping for url: {url}")
 
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
 
        # Extract image
        image = soup.find("img", class_="post-image")
        large_image = image["src"] if image else "Not found"
 
        # Extract publisher
        try:
            raw_article_publisher = (
                soup.find("div", class_="post-content")
                .find("p", class_="p1")
                .find("b")
                .text
            )
        except Exception:
            raw_article_publisher = "Not found"
 
        return {"large_image": large_image, "publisher": raw_article_publisher}
 
    except requests.exceptions.RequestException as e:
        pprint(f"Error fetching article {url}: {e}")
        return {"large_image": "Not found", "publisher": "Not found"}
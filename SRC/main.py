from scrappers.punch_scrapper import punch_scrapper_loop
from pprint import pprint
from scrappers.sun_scrapper import sun_scrappers
from database.connect import create_server_connection
from DAO.db_queries import CREATE_TABLE_QUERY, CREATE_DATABASE_QUERY, SAVE_DATA_QUERY, ALTER_TABLE_QUERY
from database.db_utils import execute_query, create_database



connection = create_server_connection("bt-newsapi-db-prod.c3ka2iwk2b6o.us-east-1.rds.amazonaws.com", "root", "Havard1992")
cursor = connection.cursor()
# create_database(connection, CREATE_DATABASE_QUERY)

# execute_query(connection, ALTER_TABLE_QUERY)

def run_scrappers():
    # This function runs all the scrapers, and saves the data to the database.
    punch_data = punch_scrapper_loop()
    print("running the punch scraper... saving the data to the db")
    for item in punch_data:
        data = (
            item["news_title"],
            item["media_house"],
            item["article_link"],
            item["abstract"],
            item["thumbnail"],
            item["large_image"],
            item["publisher"],
            item["publish_date"],
        )
 
        cursor.execute(SAVE_DATA_QUERY(), data)
        connection.commit()
 
    sun_data = sun_scrappers()
    print("running the sun scraper... saving the data to the db")
    for item in sun_data:
        data = (
            item["news_title"],
            item["media_house"],
            item["article_link"],
            item["abstract"],
            item["thumbnail"],
            item["large_image"],
            item["publisher"],
            item["publish_date"],
        )
 
        cursor.execute(SAVE_DATA_QUERY(), data)
        connection.commit()
 
    print(f"scraper done. No of data points added:  {len(punch_data)+len(sun_data)}  ")
 
 
run_scrappers()

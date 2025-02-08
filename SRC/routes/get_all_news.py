from DAO.db_queries import GET_ALL_NEWS_QUERY
from database.db_utils import execute_query


def get_all_news(db_connection):
    news_data = execute_query(db_connection, GET_ALL_NEWS_QUERY)
    print(news_data)
    return news_data
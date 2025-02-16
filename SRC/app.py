from flask import Flask, jsonify
from flask_cors import CORS
from database.connect import create_server_connection
from database.db_utils import execute_query, fetch_one, drop_database
from DAO.db_queries import CREATE_TABLE_QUERY, CREATE_DATABASE_QUERY, SAVE_DATA_QUERY, CHECK_DATA_EXIST_QUERY
from scrappers.punch_scrapper import punch_scrapper_loop
from scrappers.sun_scrapper import sun_scrappers
 
# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
 
# Database connection
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "Havard@1992"
DB_NAME = "news_db"
 
# Create database if not exists
connection = create_server_connection(DB_HOST, DB_USER, DB_PASSWORD)
# drop_database(connection, DB_NAME)
execute_query(connection, CREATE_DATABASE_QUERY)
connection.database = DB_NAME  # Switch to the database
 
# Create table if it does not exist
execute_query(connection, CREATE_TABLE_QUERY)
 
# Check if data exists before running scrapers
data_exists = fetch_one(connection, CHECK_DATA_EXIST_QUERY)  # Returns None if table is empty
 
if not data_exists:
    print("No data found in the database. Running scrapers...")
    
    cursor = connection.cursor()
 
    def run_scrapers():
        """Runs the web scrapers and saves data to the database if empty."""
        punch_data = punch_scrapper_loop()
        print("Running Punch scraper... saving data to the database")
        for item in punch_data:
            data = (
                item["news_title"], item["media_house"], item["article_link"],
                item["abstract"], item["thumbnail"], item["large_image"],
                item["publisher"], item["publish_date"]
            )
            cursor.execute(SAVE_DATA_QUERY, data)
            connection.commit()
 
        sun_data = sun_scrappers()
        print("Running Sun scraper... saving data to the database")
        for item in sun_data:
            data = (
                item["news_title"], item["media_house"], item["article_link"],
                item["abstract"], item["thumbnail"], item["large_image"],
                item["publisher"], item["publish_date"]
            )
            cursor.execute(SAVE_DATA_QUERY, data)
            connection.commit()
 
        print(f"Scraper completed. Data points added: {len(punch_data) + len(sun_data)}")
 
    run_scrapers()
else:
    print("Data already exists in the database. Skipping scrapers.")
 
# API Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to our News API")
 
 
@app.route("/allnews", methods=["GET"])
def getnews():
    """Fetch all news from the database."""
    from routes.get_all_news import get_all_news
    data = get_all_news(connection)
    return jsonify(message=data)
 
 
# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
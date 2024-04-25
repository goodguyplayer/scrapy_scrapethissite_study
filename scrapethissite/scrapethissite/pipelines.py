import mysql.connector
from dotenv import dotenv_values
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapethissitePipeline:
    def process_item(self, item, spider):
        return item


class CountriesToMySQLPipeline(object):
    def __init__(self) -> None:
        self.create_connection()
        self.create_table_if_not_exists()


    def create_connection(self):
        config = dotenv_values(".env")
        self.conn = mysql.connector.connect(
            host = config["MYSQL_HOST"],
            user = config["MYSQL_USER"],
            password = config["MYSQL_PASSWORD"],
            database = config["MYSQL_DATABASE"]
        )
        self.curr = self.conn.cursor()

    
    def create_table_if_not_exists(self):
        create_table = """
                        CREATE TABLE IF NOT EXISTS countries_scrapy(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            capital VARCHAR(255),
                            populations INTEGER,
                            area DECIMAL
                        );
                        """
        self.curr.execute("""
                        CREATE TABLE IF NOT EXISTS countries_scrapy(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            capital VARCHAR(255),
                            population VARCHAR(255),
                            area VARCHAR(255)
                        );
                        """)
        self.conn.commit()
    

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    
    def store_db(self, item):
        self.curr.execute("""INSERT INTO countries_scrapy (name, capital, population, area) values (%s, %s, %s, %s)""",
        (
            item["name"],
            item["capital"],
            item["population"],
            item["area"]
        ))
        self.conn.commit()

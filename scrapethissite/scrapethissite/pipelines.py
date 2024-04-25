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


class HockeysToMySQLPipeline(object):
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
                        CREATE TABLE IF NOT EXISTS hockeys_scrapy(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            year VARCHAR(255),
                            wins VARCHAR(255),
                            losses VARCHAR(255),
                            ot_losses VARCHAR(255),
                            win_perc VARCHAR(255),
                            goals_for VARCHAR(255),
                            goals_against VARCHAR(255),
                            more_less VARCHAR(255)
                        );
                        """
        self.curr.execute(create_table)
        self.conn.commit()
    

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    
    def store_db(self, item):
        self.curr.execute("""INSERT INTO hockeys_scrapy (name, year, wins, losses, ot_losses, win_perc, goals_for, goals_against, more_less) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (

            self.item_index_treat(item,"name"),
            self.item_index_treat(item,"year"),
            self.item_index_treat(item,"wins"),
            self.item_index_treat(item,"losses"),
            self.item_index_treat(item,"ot_losses"),
            self.item_index_treat(item,"win_perc"),
            self.item_index_treat(item,"goals_for"),
            self.item_index_treat(item,"goals_against"),
            self.item_index_treat(item,"more_less")
            
        ))
        self.conn.commit()

    
    def item_index_treat(self, item, value):
        to_return = ""
        try:
            to_return = item[value]
        except:
            pass
        finally:
            return to_return


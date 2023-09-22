import configparser
import mysql.connector
def connector():
    # Đọc thông tin cấu hình từ tệp .properties
    config = configparser.ConfigParser()
    config.read('config.properties')

    db_config = {
        'user': config.get('Database', 'user'),
        'password': config.get('Database', 'password'),
        'host': config.get('Database', 'host'),
        'database': config.get('Database', 'database')
    }

    # Kết nối đến MySQL
    try:
        cnx = mysql.connector.connect(**db_config)
        print("Connect to MySQL database name: ",config.get('Database', 'database')," successfully!!")
        return cnx
    except Exception:
        print("DBConnector error: "+ str(Exception))
        return None

    # cursor = cnx.cursor()
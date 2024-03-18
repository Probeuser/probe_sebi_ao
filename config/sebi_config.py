import mysql.connector
from datetime import datetime
from functions import get_data_count
from selenium import webdriver



source_status = "Active"
log_list = [None] * 8
no_data_avaliable = 0
no_data_scraped = 0
source_name = "sebi_ao"
table_name = "sebi_orders"

host = '4.213.77.165'
user = 'root1'
password = 'Mysql1234$'
database = 'sebi'


def db_connection():
    mydb = mysql.connector.connect(
        host="4.213.77.165",
        user="root1",
        password="Mysql1234$",
        database="sebi"
    )

    return mydb

connection = mysql.connector.connect(
     host = '4.213.77.165',
        user = 'root1',
        password = 'Mysql1234$',
        database = 'sebi'
)



connection1 = mysql.connector.connect(
     host = '4.213.77.165',
        user = 'root1',
        password = 'Mysql1234$',
        database = 'sebi'
    )

cursor = connection.cursor()

log_cursor = connection1.cursor()


current_date = datetime.now().strftime("%Y-%m-%d")





download_folder = r"C:\inetpub\wwwroot\Sebi_apiproject\pdfdownload"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--disable-notifications")  
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})

browser = webdriver.Chrome(options=chrome_options)

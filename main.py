from pprint import pprint
import extract_data
import save_to_csv
import request_connect
import read_resource
from datetime import datetime

def Run():

    output_path = read_resource.read_props().get('CSV_PATH')
    row_elements = request_connect.Connect()
    list_leagues, clubs = extract_data.extract_data_from_web(row_elements)
    save_to_csv.save_to_excel(list_leagues, output_path)

Run()
# import read_data
# output_path= read_resource.read_props().get('CSV_PATH')
# read_data.read_backup_data_directory()
# URL của trang web bạn muốn thu thập dữ liệu


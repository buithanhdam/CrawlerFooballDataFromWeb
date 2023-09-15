from pprint import pprint
import extract_data
import save_to_csv
import request_connect
import read_resource
from datetime import datetime

def Run():
    date = '12/09/2023'
    [output_path] = read_resource.read_csv_props()
    row_elements = request_connect.Connect(date)
    list_leagues, clubs = extract_data.extract_data_from_web(row_elements)
    save_to_csv.save_to_excel(list_leagues, output_path, date)

Run()
# import read_from_csv
#
# [output_path] = read_resource.read_csv_props()
# read_from_csv.read_data_from_excel(output_path)
# URL của trang web bạn muốn thu thập dữ liệu

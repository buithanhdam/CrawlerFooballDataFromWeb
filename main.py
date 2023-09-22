# from crawler import extract_data, request_connect
# import save_to_csv
# import read_resource
#
#
#
# def Run(date_string=''):
#
#     output_path = read_resource.read_props().get('CSV_PATH')
#     row_elements = request_connect.Connect(date_string)
#     list_leagues, clubs = extract_data.extract_data_from_web(row_elements)
#     save_to_csv.save_to_excel(list_leagues, output_path,date_string)
#
# Run()
# import database.DBConnector as dbconnect
# dbconnect.connector()
# import database.load_data_to_DB as load
# load.load_data_to_stagging(date_string='19/9/2023')
# import read_resource
#
# pprint(read_resource.read_props())

# import read_data
# output_path= read_resource.read_props().get('CSV_PATH')
# read_data.read_backup_data_directory()
# URL của trang web bạn muốn thu thập dữ liệu


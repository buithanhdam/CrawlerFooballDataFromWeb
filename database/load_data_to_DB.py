def load_data_to_stagging(date_string=''):
    import csv
    from database import DBConnector
    import read_resource
    from datetime import datetime


    # Kết nối đến cơ sở dữ liệu MySQL
    cnx = DBConnector.connector()
    cursor = cnx.cursor()
    date_format = '%Y-%m-%d'
    if date_string == '':
        today = datetime.today()
        month_path = str(today.month)
        year_path = str(today.year)
        day_path = str(today.day)
        now = datetime.now()
        dt_string = now.strftime(date_format)
    else:
        str_tokens = date_string.split('/')
        year_path = str_tokens[2]
        month_path = str_tokens[1]
        day_path = str_tokens[0]
        date_obj = datetime.strptime(date_string, '%d/%m/%Y')
        dt_string = date_obj.strftime(date_format)

    data_path = read_resource.read_props().get('DATA_PATH')
    csv_path = read_resource.read_props().get('CSV_PATH')

    path =  data_path + "/" + year_path + "/" + month_path + '/' + day_path + "/" + csv_path
    try:
        query_path = read_resource.read_props().get('QUERY_PATH')
        with open(query_path, 'r') as sql_file:
            # query = sql_file.read().format(**row)
            # cursor.execute(query)
            sql_content = sql_file.read()

            # Tìm câu truy vấn CREATE TABLE
            create_table_start = sql_content.find("CREATE TABLE IF NOT EXISTS")
            create_table_end = sql_content.find(";", create_table_start)
            create_table_query = sql_content[create_table_start:create_table_end + 1]

            # Tìm câu truy vấn INSERT
            insert_start = sql_content.find("INSERT INTO")
            insert_end = sql_content.find(";", insert_start)
            insert_query = sql_content[insert_start:insert_end + 1]

            # Tìm câu truy vấn SELECT
            select_start = sql_content.find("SELECT")
            select_end = sql_content.find(";", select_start)
            select_query = sql_content[select_start:select_end + 1]

            # Tìm câu truy vấn UPDATE
            update_start = sql_content.find("UPDATE")
            update_end = sql_content.find(";", update_start)
            update_query = sql_content[update_start:update_end + 1]
            try:
                # Đọc dữ liệu từ tệp CSV
                with open(path, 'r', encoding='utf-8-sig') as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    formatted_query = select_query.format(date_time=dt_string)
                    cursor.execute(formatted_query)

                    # Lấy kết quả
                    result = cursor.fetchone()
                    if int(result[0]) >0:
                        for row in csv_reader:
                            # Đọc câu truy vấn INSERT từ tệp SQL
                            special_characters = "`~!?'^*,./\|:;-_"

                            # Loại bỏ các ký tự đặc biệt khỏi chuỗi
                            for char in special_characters:
                                row['first_team'] = row['first_team'].replace(char, "")
                            for char in special_characters:
                                row['second_team'] = row['second_team'].replace(char, "")
                            row['first_team_goals'] = int(float(row['first_team_goals'])) if row[
                                                                                                 'first_team_goals'] != '' else 'NULL'
                            row['second_team_goals'] = int(float(row['second_team_goals'])) if row[
                                                                                                   'second_team_goals'] != '' else 'NULL'
                            row['full_match_goals'] = row['full_match_goals'] if row[
                                                                                     'full_match_goals'] != '' else 'NULL'
                            row['half_match_goals'] = row['half_match_goals'] if row[
                                                                                     'half_match_goals'] != '' else 'NULL'
                            formatted_update_query = update_query.format(
                                full_match_goals=row['full_match_goals'],
                                half_match_goals=row['half_match_goals'],
                                first_team_goals =row['first_team_goals'],
                                second_team_goals = row['second_team_goals'],
                                match_href = row['match_href'],
                                region = row['region'],
                                tournament=row['tournament'],
                                begin_time=row['begin_time'],
                                first_team=row['first_team'],
                                second_team=row['second_team']
                            )
                            formatted_update_query = formatted_update_query.replace("'NULL'", "NULL")
                            cursor.execute(formatted_update_query)
                        print('[INFO]: Update new ',result[0],' data to Database successfully!!')
                    else:
                        cursor.execute(create_table_query)
                        for row in csv_reader:
                            # Đọc câu truy vấn INSERT từ tệp SQL
                            special_characters = "`~!?'^*,./\|:;-_"

                            # Loại bỏ các ký tự đặc biệt khỏi chuỗi
                            for char in special_characters:
                                row['first_team'] = row['first_team'].replace(char, "")
                            for char in special_characters:
                                row['second_team'] = row['second_team'].replace(char, "")
                            # row['first_team'] = re.sub(r"[^a-zA-Z0-9\s]", "", row['first_team'])
                            # row['second_team'] = re.sub(r"[^a-zA-Z0-9\s]", "", row['second_team'])
                            row['first_team_goals'] = int(float(row['first_team_goals'])) if row['first_team_goals'] != '' else 'NULL'
                            row['second_team_goals'] = int(float(row['second_team_goals'])) if row['second_team_goals'] !='' else 'NULL'
                            row['full_match_goals'] = row['full_match_goals'] if row['full_match_goals'] != '' else 'NULL'
                            row['half_match_goals'] = row['half_match_goals'] if row['half_match_goals'] != '' else 'NULL'
                            query = insert_query.format(**row)
                            query = query.replace("'NULL'", "NULL")
                            cursor.execute(query)
                        print('[INFO]: Load data to Database successfully!!')
            except Exception as e:
                print("[ERROR]: Read csv file error: " + str(e))
    except Exception as e:
        print("[ERROR]: Read query sql error: " + str(e))

    # Lưu các thay đổi vào cơ sở dữ liệu
    cnx.commit()

    # Đóng kết nối với cơ sở dữ liệu
    cursor.close()
    cnx.close()

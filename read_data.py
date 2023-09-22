def read_data_from_excel(output_path, date_string=''):
    import pandas as pd
    import os.path

    data_output_path = read_data_directory(date_string) + "/" + output_path
    check_file = os.path.isfile(data_output_path)
    if check_file:
        df = pd.read_csv(data_output_path)
        try:
            df['date_time'] = pd.to_datetime(df['date_time'], format='mixed')
            df['date_time'] = pd.to_datetime(df['date_time'], format='%m/%d/%Y')
            print("Read csv successfully!!")
        except Exception:
            print("[ERROR]: Read Data Error: " + str(Exception))
            return []
    else:
        return []
    return df


# lỗi đọc cột date_time ####

def read_data_directory(date_string=''):
    import os
    from datetime import datetime
    import read_resource

    if date_string == '':
        today = datetime.today()
        month_path = str(today.month)
        year_path = str(today.year)
        day_path = str(today.day)
    else:
        str_tokens = date_string.split('/')
        year_path = str_tokens[2]
        month_path = str_tokens[1]
        day_path = str_tokens[0]

    data_month_path = read_resource.read_props().get('DATA_PATH') + "/" + year_path + "/" + month_path + "/"+ day_path
    # Check whether the specified path exists or not
    isExist = os.path.exists(data_month_path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(data_month_path)
        print("The new month directory is created!")
    return data_month_path


def read_backup_data_directory(date_string=''):
    import read_resource
    from datetime import datetime
    import os

    backup = read_resource.read_props().get('BACKUP_PATH')
    if date_string == '':
        today = datetime.today()
        month_path = str(today.month)
        year_path = str(today.year)
        day_path = str(today.day)
    else:
        str_tokens = date_string.split('/')
        year_path = str_tokens[2]
        month_path = str_tokens[1]
        day_path = str_tokens[0]

    backup_data_path = backup + "/" + year_path + "/" + month_path+"/"+day_path
    # Check whether the specified path exists or not
    isExist = os.path.exists(backup_data_path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(backup_data_path)
        print("The new month directory is created!")
    return backup_data_path

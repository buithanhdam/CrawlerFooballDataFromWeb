def transform_data(list_leagues, date_string ):
    from datetime import datetime
    new_leagues = []
    date_format = '%m/%d/%Y'
    dt_string = ''
    if date_string  == '':
        now = datetime.now()
        dt_string = now.strftime(date_format)
    else:
        date_obj = datetime.strptime(date_string , '%d/%m/%Y')
        dt_string = date_obj.strftime(date_format)

    for league in list_leagues:
        matchs = league.get("matchs")
        for m in matchs:
            lm = {}
            hl = {}
            hl.update(league)
            hl.pop("matchs")
            lm.__setitem__("date_time", dt_string)
            lm.update(hl)
            lm.update(m)
            match_dict = lm
            new_leagues.append(match_dict)
    return new_leagues


def save_to_excel(list_leagues, output_path, date_string =''):
    import os
    import pandas as pd
    import read_data
    import datetime
    import update_to_csv
    import backup_data
    import read_resource

    new_leagues = transform_data(list_leagues, date_string )
    old_df = read_data.read_data_from_excel(output_path,date_string)

    specific_date = ''
    if date_string  =='':
        now = datetime.datetime.now()
        specific_date = now.strftime('%m/%d/%Y')
    else:
        date_obj = datetime.datetime.strptime(date_string , '%d/%m/%Y')
        specific_date = date_obj.strftime('%m/%d/%Y')

    # Chuyển đổi ngày thành định dạng datetime
    specific_date = pd.to_datetime(specific_date, format='%m/%d/%Y')

    data_output_path = read_data.read_data_directory(date_string) + "/"+output_path

    # Lọc dữ liệu theo ngày cụ thể
    # recent_df = old_df[old_df['date_time'].dt.date == specific_date.date()]
    df = pd.DataFrame(new_leagues)
    try:
        print(len(old_df))
        if len(old_df) < 1:
            df.to_csv(data_output_path, mode='a', index=False, encoding='utf-8-sig', header=not os.path.exists(data_output_path))
            backup_data.backup_csv_data(output_path, date_string)
            print("Save new data to csv file successfully!!")
        else:
            backup_data.backup_csv_data(output_path,date_string)
            n_df = update_to_csv.update_data_from_web(df, output_path, date_string)
            n_df.to_csv(data_output_path, mode='w', index=False, encoding='utf-8-sig')
            print("Update new data to csv file successfully!!")
    except Exception:
        print("[ERROR]: Save Error: ", str(Exception))

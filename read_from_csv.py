def read_data_from_excel(output_path):
    import pandas as pd

    df = pd.read_csv(output_path)
    try:
        df['date_time'] = pd.to_datetime(df['date_time'], format='ISO8601')
        df['date_time'] = pd.to_datetime(df['date_time'], format='%m/%d/%Y %H:%M')
        print("Read csv successfully!!")
    except NameError:
        print("Read Data Error: "+NameError)
        return None
    return df
# lỗi đọc cột date_time ####
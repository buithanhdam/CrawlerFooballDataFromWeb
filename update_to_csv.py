def update_data_from_web(new_df, output_path, date_string  = ''):
    import read_data
    import pandas as pd
    import datetime
    import numpy as np
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

    for i, r in new_df.iterrows():
        # cols = ['region', 'tournament', 'begin_time', 'first_team', 'second_team']

        values = [r['region'], r['tournament'], r['begin_time'], r['first_team'], r['second_team']]

        # row = old_df.loc[
        #     (old_df['date_time'].dt.date == specific_date.date()) & (old_df['region'] == values[0]) & (
        #                 old_df['tournament'] == values[1]) & (
        #             old_df['begin_time'] == values[2]) & (old_df['first_team'] == values[3]) & (
        #                 old_df['second_team'] == values[4])]
        # Cập nhật cột 'score' cho dòng dữ liệu tìm thấy
        # row['full_match_goals'] = r['full_match_goals']
        # row['half_match_goals'] = r['half_match_goals']
        # row['first_team_goals'] = r['first_team_goals']
        # row['second_team_goals'] = r['second_team_goals']

        index = old_df[
            (old_df['date_time'].dt.date == specific_date.date()) & (old_df['region'] == values[0]) & (
                        old_df['tournament'] == values[1]) & (
                    old_df['begin_time'] == values[2]) & (old_df['first_team'] == values[3]) & (
                    old_df['second_team'] == values[4])].index


        old_df.loc[index, 'date_time'] = r['date_time']
        old_df.loc[index, 'match_href'] = r['match_href']
        old_df.loc[index, 'full_match_goals'] = r['full_match_goals']
        old_df.loc[index, 'half_match_goals'] = r['half_match_goals']
        old_df.loc[index, 'first_team_goals'] = int(r['first_team_goals']) if r['first_team_goals'] is not None else np.nan
        old_df.loc[index, 'second_team_goals'] = int(r['second_team_goals']) if r['second_team_goals'] is not None else np.nan


    return old_df

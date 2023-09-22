def tranform_date(date):
    #2023 / aug / 12 /
    from datetime import datetime
    # Chuỗi ngày ban đầu
    # date_string = '14/9/2023'
    # Chuyển đổi chuỗi thành đối tượng datetime
    formatted_date = ''
    if date != '':
        date_obj = datetime.strptime(date, '%d/%m/%Y')
    # Định dạng lại ngày theo định dạng mong muốn
        formatted_date = date_obj.strftime('%Y/%b/%d')
    return formatted_date


def Connect(date=''):
    import read_resource
    import requests
    from bs4 import BeautifulSoup

    formatted_date = tranform_date(date)

    url = read_resource.read_props().get('WEB_URL')
    matches_today = read_resource.read_props().get('TODAY_PATH')
    # Gửi yêu cầu GET đến trang web
    response = requests.get(url + matches_today+formatted_date)

    # Kiểm tra mã trạng thái của yêu cầu
    if response.status_code == 200:
        # Tạo đối tượng BeautifulSoup từ nội dung trang web
        soup = BeautifulSoup(response.content, "html.parser")

        # Tìm các phần tử HTML chứa dữ liệu bạn muốn thu thập
        parent_elements = soup.find("div", class_="content")

        table_element = parent_elements.find("table", class_="standard_tabelle")
        row_elements = table_element.find_all("tr")
        return row_elements
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
        return None
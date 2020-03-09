from bs4 import BeautifulSoup
import csv
from menus_parser import get_rest_dishes
from get_html import get_html

result_rests = []


def get_rests(html):
    # получаем название и урл заведения
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_rests = soup.find(
            'ul', class_='service-items-medium').findAll('div', class_='service-description')
        for rest in all_rests:
            rest_url = rest.find('div', class_='H3').find('a')['href']
            if 'night_clubs' in rest_url:
                continue
            rest_name = rest.find('div', class_='H3').find('a').text
            # rest_places = rest.findAll('address')[1]
            # rest_adress = rest_places.text
            # if rest_places.find('a'):
            #     rest_metro = rest_places.find('a').text
            # else:
            #     rest_metro = ''
            result_rests.append({
                'rest_name': rest_name.replace(u'\xa0', u' ').replace('\t', '').replace('\n', ' '),
                # 'rest_metro': rest_metro.replace(u'\xa0', u' ').replace('\t', '').replace('\n', ' '),
                # 'rest_adress': rest_adress.replace(u'\xa0', u' ').replace('\t', '').replace('\n', ' ').strip(),
                'rest_url': rest_url,
            })
    return False


# забираем список заведений постранично
for page in range(1, 2):  # 10
    url = "https://spb.zoon.ru/restaurants/?action=list&type=service&search_query_form=1&sort_field=rating&need%5B%5D=items&page=1"
    get_rests(get_html(url, 'post'))

# переходим на страницу заведения
for rest in result_rests:
    url = f"{rest['rest_url']}/menu"
    html = get_html(url, 'get')
    # if html:
    #     soup = BeautifulSoup(html, 'html.parser')
    get_rest_dishes(html)
    get_rest_info(html)


# запись в файл csv
# with open('rests.csv', 'w', encoding='utf-8', newline='') as f:
#     fields = ['rest_name', 'rest_url', 'rest_metro', 'rest_adress']
#     writer = csv.DictWriter(f, fields, delimiter='|')
#     writer.writeheader()
#     for rest in result_rests:
#         writer.writerow(rest)

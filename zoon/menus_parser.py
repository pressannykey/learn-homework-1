from bs4 import BeautifulSoup
from get_html import get_html


def get_rest_dishes(html):
    # здесь функция чтобы забрать меню
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        try:
            all_dishes = soup.find(
                'div', class_='pricelist-group').findAll('div', class_='title fs-large oh')
            result_dishes = []
            for dish in all_dishes:
                if dish.find('a'):
                    title = dish.find('a').text
                    category_url = dish.find('a')['href']
                else:
                    title = dish.find('span').text
                    category_url = ''
                result_dishes.append({
                    'title': title.replace(u'\xa0', u' ').replace('\t', '').replace('\n', ''),
                    'category_url': category_url,
                })
            return result_dishes
        except AttributeError:
            return False  # ДОПИСАТЬ! добавляем к меню колонку про отношение к ресту и хев-меню колонку, если нет - хев-меню false
    return False


def get_rest_info(html):
    # затем забрать инфу по ресту
    pass

# get_rest_dishes(get_html(
#     'https://spb.zoon.ru/entertainment/antikafe_nonamelounge_na_moskovskom_prospekte/menu', 'get'))

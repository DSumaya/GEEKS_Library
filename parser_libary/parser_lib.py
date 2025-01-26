import requests
from bs4 import BeautifulSoup as BS


URL = 'https://litnet.com/'


HEADERS = {

   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


# №1 этап
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request
#row book-item  col-xs-2
# №2 этап
def get_data(html):
    bs = BS(html, features="html.parser")
    items = bs.find_all('div', class_= 'row book-item' )
    library_list =[]
    for item in items:
        description = item.find('div', class_='col-xs-2').get_text()
        href = item.find('a').get('href')
        library_list.append({
            'description': description,
            'href': href
        })
    return library_list


# №3 этап
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        library_list2 = []
        for page in range(1, 3):
            response = get_html(f"https://litnet.com/ru/top/best?period=1days", params={"page": page})
            library_list2.extend(get_data(response.text))
        return library_list2
    else:
            raise Exception('Error in parsing')
#print(parsing())



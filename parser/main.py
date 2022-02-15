import getcurrence

def main():
    val = input('Код валюты: ').split()
    content = request()
    parser(content, val)


def request():
    import requests as req
    url = 'https://www.cbr.ru/currency_base/daily/'
    content = req.get(url)
    return content.text


def parser(content: str, val: list):
    from bs4 import BeautifulSoup as bs
    soup = bs(content, 'html.parser')
    table = soup.table

    for i in val:
        needle_td = table.find(name='td', text=i.upper())
        if needle_td == None:
            print(f'Валюта с кодом: {i} не найдена \n')
            continue
        else:
            s = needle_td.parent
            string_td = s.find_all(name='td')
            currence_list = list()

            for string in string_td:
                temp_string = str(string).replace('<td>', '').replace('</td>', '')
                currence_list.append(temp_string)
            print('Название: ' + str(currence_list[3]) + '\n'
                  'Цена: ' + str(currence_list[4]) + '\n')
    main()


if __name__ == '__main__':
    main()
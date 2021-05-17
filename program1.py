import requests
import bs4


def main():
    print_the_header()

    city = input('What city do you want the weather for?')

    print(city)
    html = get_html_from_web(city)

    get_weather_from_html(html)

    # print the header
    # get zipcode from user
    # get html from web
    # parse the html
    # display for the forecast


def print_the_header():
    print('------------------------------')
    print('         weather app')
    print('=-----------------------------=')
    print()


def get_html_from_web(city):
    url = 'https://world-weather.ru/pogoda/russia/{}'.format(city)
    # print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' \
                             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                             'Chrome/75.0.3770.80 Safari/537.36'}
    response = requests.get(url, headers=headers)
    #print(response.status_code)
    #print(response.text[250:700])
    return response.text


def get_weather_from_html(html):

    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(id='content-left').find('h1').get_text()
    tem = soup.find(id='weather-now-number').get_text()
    cond = soup.find(id='weather-now-icon').get('title')
    print('------------------------')
    print(loc)
    print(tem + 'C' + ' ' + cond)
    print('------------------------')


if __name__ == '__main__':
    main()

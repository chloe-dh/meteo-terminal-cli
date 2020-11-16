import urllib.request
from bs4 import BeautifulSoup
import sys
import argparse

# template for printing
my_str = '''
{0:<8}: {1:>2}°C   --   {2:<}
          {3:<}'''

days_option = ["Hier : ", "Aujourd'hui", "Demain"]

default_site_url = 'https://www.meteo-toulouse.org/'


def soup_url(url):
    # Fetch the html file
    with urllib.request.urlopen(url) as response:
        html = response.read()
    # Parse the html file
    return BeautifulSoup(html, 'html.parser')


def assessed_cities(soup):
    select_city = soup.select(".header-search__city-select--form option")
    cities = {}
    for option in select_city[1:]:
        cities[option.text.casefold()] = option['value']
    return cities


def get_date(soup, date_index=1):
    date_day = soup.select(".home-carousel-item")[date_index]['data-date']
    date_day = ' '.join([i.capitalize() for i in date_day.split()])
    return date_day


def extract_info(soup, date_index=1, day_period=0):
    index = date_index * 4 + day_period
    time_of_day = soup.select(".forecasts__item--label")[index].get_text(strip=True)
    temp_of_day = soup.select(".forecasts__item--temp")[index].get_text(strip=True)
    previous_day_tag = soup.select(".forecasts__item--previous")[index]
    previous_day = previous_day_tag.get_text(strip=True).casefold()
    text_forecast = soup.select(".forecasts__item--picto")[index]['data-tippy']

    return time_of_day, temp_of_day, previous_day, text_forecast


def main(args):
    parser = argparse.ArgumentParser(
        description="display weather forecast CLI"
        )
    parser.add_argument(
        '-c', '--city', nargs='?', const='list_city',
        help='Default city is Toulouse. If not argument is given,'
             ' prints the list of options and prompt again'
    )
    parser.add_argument(
        '-t', '--tomorrow', action='store_true',
        help='Print tomorrow rather than today'
    )
    parser.add_argument(
        '-y', '--yesterday', action='store_true',
        help='Print yesterday rather than today. If -t is present, -y is ignored'
    )
    args = parser.parse_args(args)
    print(args)
    if args.tomorrow:
        date_index = 2
    elif args.yesterday:
        date_index = 0
    else:
        date_index = 1

    soup = soup_url(default_site_url)

    if args.city:
        cities = assessed_cities(soup)
        while True:
            try:
                website = cities[args.city.casefold()]
            except KeyError:
                print("Here is a list of cities with professionally assessed weather forecast.")
                print('Try again with one them: ')
                for key in cities:
                    print(key)
                args.city = input('Try again: ')
            else:
                soup = soup_url(website)
                break
    else:
        args.city = 'toulouse'

    date_day = get_date(soup, date_index=date_index)

    print('\n' + '{} : {} -- {}'.format(days_option[date_index], date_day, args.city.capitalize()))

    # morning to night
    for day_period in range(0, 4):
        result = extract_info(soup, date_index=date_index, day_period=day_period)
        print(my_str.format(*result) + '\n')


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == '__main__':
    run()

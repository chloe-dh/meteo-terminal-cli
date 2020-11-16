import urllib.request
import datetime
from displaymeteo.app import extract_info, soup_url, default_site_url, get_date, assessed_cities


def test_url_exists():
    try:
        urllib.request.urlopen(default_site_url)
    except urllib.error.HTTPError:
        assert False
    except urllib.error.URLError:
        assert False
    else:
        assert True


def test_assessed_city():
    soup = soup_url(default_site_url)
    cities = assessed_cities(soup)
    for i in range(4):
        name, website = cities.popitem()
        try:
            urllib.request.urlopen(website)
        except urllib.error.HTTPError:
            assert False
        except urllib.error.URLError as e:
            assert False
        else:
            assert True


def test_format_page():
    result = extract_info(soup_url(default_site_url), date_index=2, day_period=3)
    try:
        int(result[1])
    except ValueError as v:
        pass
    assert 'v' not in locals()
    assert result[0] == 'Nuit'
    assert 'veille' in result[2]


def test_date():
    # datetime expanded names depend on the locale language
    month_fr = 'janvier février mars avril mai juin juillet ' \
               'aout septembre octobre novembre décembre'.split()

    month_fr = dict(enumerate(month_fr))
    soup = soup_url(default_site_url)
    date_day = get_date(soup).split()
    print(date_day)
    today = datetime.date.today()
    assert date_day[1] == str(int(today.strftime('%d')))
    assert date_day[2].casefold() == month_fr[int(today.strftime('%m'))-1]

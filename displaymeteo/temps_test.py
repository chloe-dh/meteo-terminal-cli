from displaymeteo.app import extract_info, soup_url, default_site_url, assessed_cities

soup = soup_url('https://www.meteo-villes.com')

# print(soup)

tags = soup.select(".header-search__city-select--form option")

cities = assessed_cities(soup)
print(cities)

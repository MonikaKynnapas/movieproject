from urllib.request import urlopen
import os
import json
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproject.settings')
django.setup()
from movieapp.models import Country

url = "https://restcountries.com/v3.1/all"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())
counter = 0

Country.objects.all().delete()  # Delete data from model

for country in data_json:
    if 'capital' in country:
        # Lisa nimi listi
        common = country['name']['common']
        official = country['name']['official']
        capital = country["capital"][0]
        region = country["region"]
        if "subregion" in country:
            subregion = country["subregion"]
        else:
            subregion = None

        flag = country["flags"]["png"]
        maps = country["maps"]["googleMaps"]

        Country.objects.get_or_create(common=common, official=official, capital=capital, region=region,
                                      subregion=subregion, flag=flag, map=maps)

        # Country.objects.create(common=common, official=official, capital=capital, region=region,
        #                                       subregion=subregion, flag=flag, map=maps)
        # Vajab eelnevalt kustutamist, muidu kirjutab igakord andmeid juurde

        counter += 1

print(f'Total {counter} countries.')



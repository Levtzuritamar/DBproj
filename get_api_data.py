import requests
import json
import time
import pandas as pd 

list_url = "https://countries-cities.p.rapidapi.com/location/country/list/"

headers = {
	"X-RapidAPI-Key": "b1da3a5c86msh6600e80493ae515p1b4ac4jsnec30b44eda90",
	"X-RapidAPI-Host": "countries-cities.p.rapidapi.com"
}

response = requests.request("GET", list_url, headers=headers)

country_populations_names = []

country_meta_data = json.loads(response.text)["countries"]
for key in country_meta_data.keys():
    time.sleep(1.5)
    country_data_url = f"https://countries-cities.p.rapidapi.com/location/country/{key}/"
    response = requests.request("GET", country_data_url, headers=headers)
    country_data = json.loads(response.text)
    country_populations_names.append(tuple(country_data["name"],country_data["population"]))


sorted(country_populations_names , key = lambda x: x[1])
country_names = []
populations = []
for tup in country_populations_names:
    country_names.append(tup[0])
    populations.append(tup[1])

pd_df = pd.DataFrame.from_dict({"country_name":country_names, "Population":populations})
pd_df.to_csv("population_by_country")


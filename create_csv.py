import pandas as pd
import numpy as np
#import geopandas as gpd
import matplotlib.pyplot as plt
import datetime as dt

# Preparamos los dataframes

cities = ['barcelona', 'madrid', 'malaga', 'mallorca', 'menorca', 'sevilla', 'valencia']
dir_data = "~/uni/segundo/magd/airbnb_data/"
calendar = pd.DataFrame()
listings = pd.DataFrame()
neighbourhoods = pd.DataFrame()
reviews = pd.DataFrame()
reviews_gz = pd.DataFrame()
listings_gz = pd.DataFrame()

# Vamos encadenando los csv de las distintas ciudades, añadiendo la columna city y su numero correspondiente
# (barcelona = 1, madrid = 2, malaga = 3, mallorca = 4, menorca = 5, sevilla = 6, valencia = 7)

for city in cities:
    temp_calendar = pd.read_csv(f'{dir_data}{city}/calendar.csv', parse_dates=['date'], low_memory=False)
    temp_calendar['city'] = cities.index(city) + 1
    calendar = pd.concat([temp_calendar, calendar])

    temp_listings = pd.read_csv(f'{dir_data}{city}/listings.csv')
    temp_listings['city'] = cities.index(city) + 1
    listings = pd.concat([temp_listings, listings])

    temp_neighbourhoods = pd.read_csv(f'{dir_data}{city}/neighbourhoods.csv')
    temp_neighbourhoods['city'] = cities.index(city) + 1
    neighbourhoods = pd.concat([temp_neighbourhoods, neighbourhoods])

    temp_reviews = pd.read_csv(f'{dir_data}{city}/reviews.csv')
    temp_reviews['city'] = cities.index(city) + 1
    reviews = pd.concat([temp_reviews, reviews])

    # Added the compressed files 

    temp_reviews_gz = pd.read_csv(f'{dir_data}{city}/reviews_gz.csv')
    temp_reviews_gz['city'] = cities.index(city) + 1
    reviews_gz = pd.concat([temp_reviews_gz, reviews_gz])

    temp_listings_gz = pd.read_csv(f'{dir_data}{city}/listings_gz.csv')
    temp_listings_gz['city'] = cities.index(city) + 1
    listings_gz = pd.concat([temp_listings_gz, listings_gz])


# Guardamos los dataframes creados en archivos csv

calendar.to_csv('calendar_fin.csv', index=False)
listings.to_csv('listings_fin.csv', index=False)
neighbourhoods.to_csv('neighbourhoods_fin.csv', index=False)
reviews.to_csv('reviews_fin.csv', index=False)
reviews_gz.to_csv('reviews_gz_fin.csv', index=False)
listings_gz.to_csv('listings_gz_fin.csv', index=False)

print("Program completed")
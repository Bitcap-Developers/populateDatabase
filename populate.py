# !/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Documentation for this module:
This module is used to populate the database with the name of the countries in the country table and state, countries(foreign Key), timezone and language in the state table.
The data is populated for the places where DHL provides services.
"""
# importing the required module
import json , requests , pycountry , pycountry
from urllib2 import urlopen
from timezonefinder import TimezoneFinder

# Array of countries along with there languages imported 
import countryLanguage.py

from messengerbot.models import user , status_code , status , type_of_service , mode_of_contact , type_of_shipment , type_of_collection , type_of_box , address , language , country , place , order
import sys
reload(sys)
sys.setdefaultencoding("utf-8")




def populate_database():
    """
    This function is used to populate the database by iterating over the list of DHL centres in various states and cities.
    """
    url = 'https://gist.githubusercontent.com/mayurah/1302855181e4b5e3b05211d242ae592a/raw/7034304a7efdac74011790227ca6c8aa7ca994b1/countriesToCities.json'
    response = urlopen(url)
    json_countries = json.load(response)


    for countries in json_countries:
        print countries
        country = country.objects.get_or_create(name = countries)[0]
        country.save()
        for place_in_country in json_countries[countries]:
            print place_in_country
            placeName = place.objects.get_or_create(name = place_in_country)
            placeName.country = country
            placeName.timezone = timezoneOfPlace(place_in_country , country)
            array_of_languages = language(country)
            for item in array_of_languages:
                language = Category.objects.get_or_create(name = item)[0]
                placeName.languages.add(language)
            placeName.save()



def timezone_of_place(place , country):
    """
    This function uses google api to find the timezone of various countries.
    """
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + place + ',' + country)
    resp_json_payload = response.json()
    latitude = (resp_json_payload['results'][0]['geometry']['location']['lat'])
    longitude = (resp_json_payload['results'][0]['geometry']['location']['lng'])


  tf = TimezoneFinder()
  return =  tf.timezone_at(lng=longitude, lat=latitude)


def language(country):
    """
    This function provies a array of languages spoken in a particular country
    """
    array_languages = []
    for i in country_language:
        print i['country']
        if country.lower()  == i['country'].lower():
            array_languages.append(i['language'])

    return array_languages
















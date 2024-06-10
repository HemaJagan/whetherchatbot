import json
import requests
import streamlit as st

API_KEY = '696e115d2011a4c6936e836ba8aa9619'
city_name=input('Enter a City Name: ')
apiurl=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
get_info=requests. get (apiurl)
print(get_info)
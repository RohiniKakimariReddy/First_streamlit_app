import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣  Omega 3 & Blue Berry Oat meal')
streamlit.text('🥗  Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-range eggs')
streamlit.text('🥑🍞 Avacado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick your fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# Normalize the API response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# convert the API response to a dataframe
streamlit.dataframe(fruityvice_normalized)

import streamlit
import pandas
import requests

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

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

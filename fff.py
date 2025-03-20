import pandas as pd
import streamlit as st
st.title("hi")
car=pd.read_csv(r"C:\Users\Shivani\Downloads\quikr_car.csv")
car.head()
car.shape
car.info()
car["year"].unique()
car["Price"].unique()
car["fuel_type"].unique()
#cleaning
backup=car.copy()
car=car[car["year"].str.isnumeric()]
car["year"]=car["year"].astype(int)
car=car[car["Price"]!="Ask For Price"]
car["Price"]=car["Price"].str.replace(",","")

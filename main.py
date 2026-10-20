import streamlit as st
from random import randint as ri
from time import sleep as sl
from utils import *
st.set_page_config(page_title="Missions", layout='centered')
st.title("Missions")
missions = [
"AI Study Buddy (Mission 1)",
"BlazeX Email Creator (Mission 2)",
"National Id Validator (Mission 3)"
]
m = st.selectbox("Chosse Which Mission to show", options=missions)
st.divider()

if m == "AI Study Buddy (Mission 1)":
    stud()
elif m == "BlazeX Email Creator (Mission 2)":
    blaze()
else:
    niv()

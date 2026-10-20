# Import Libraries and Modules
import streamlit as st
from random import randint as ri
from time import sleep as sl
from utils import *

# Configure Page
st.set_page_config(page_title="Missions", layout='centered')
st.title("Missions")
# Create Missions select box
missions = [
"AI Study Buddy (Mission 1)",
"BlazeX Email Creator (Mission 2)",
"National Id Validator (Mission 3)"
]
m = st.selectbox("Chosse Which Mission to show", options=missions)

st.divider()

# Check Which Mission To display
if m == "AI Study Buddy (Mission 1)":
    stud()
elif m == "BlazeX Email Creator (Mission 2)":
    blaze()
else:
    niv()

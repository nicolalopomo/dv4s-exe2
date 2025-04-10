import streamlit as st
import numpy as np

st.title('This is page 2')

# Get info from sidebar
st.title('Gettin info from the sidebar')

player = st.session_state['Players']
team = st.session_state['Teams']

st.write('The player is:', player)
st.write('The team is:', team)


# Columns
st.title('We are using columns')

# Object notation
col1, col2 = st.columns([0.6, 0.4])

col1.header('Tennis')
col1.image("https://www.mouratoglou.com/wp-content/uploads/2024/11/11dd1227-f3e1-4903-8755-cdbeeea0d97b-JUL01675-1534x1534-c-center.webp")

col2.header('Soccer')
col2.image("https://assets.bizclikmedia.net/1336/ae6b6628be6c1a091f59ab494861e4eb:052754c37c1000c0cf9e8ac4ca83d202/article-im2219-soccer-ball-jpeg.webp")

# With notation
st.title('More columns')

data = np.random.rand(20, 1)

colA, colB = st.columns([3, 1])

with colA:
    st.header('Data Viz')
    st.bar_chart(data)
with colB:
    st.header('Table')
    st.table(data)


# Tabs
st.title("Here we are using tabs!")

tab1, tab2 = st.tabs(['Football', 'Skiing'])
tab1.subheader("Footbal")
tab1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Larry_Fitzgerald_catches_TD_at_2009_Pro_Bowl.jpg/1280px-Larry_Fitzgerald_catches_TD_at_2009_Pro_Bowl.jpg")
tab2.subheader("Football")
tab2.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Ski_Famille_-_Family_Ski_Holidays.jpg")


# Expanders
st.title("We are working with expanders")

with st.expander("Data Viz", expanded=True):
    st.subheader('My data')
    st.line_chart(data)

with st.expander("Table", expanded=False):
    st.subheader('My table')
    st.table(data)
import streamlit as st

page1 = st.Page('page1.py', title='Page 1')
page2 = st.Page('page2.py', title='Page 2')

pg = st.navigation([page1, page2])
st.set_page_config(page_title="DV4S - Exe")

# Selectbox
# Object-like
st.sidebar.selectbox(
    "Select your player",
    ('Maradona', 'Pelè', 'Fonseca'),
    key='Players'
    )

# with-like
with st.sidebar:
    rb = st.radio(
        "Team",
        ('Napoli', 'Milan', 'Roma'),
        key='Team'
    )

pg.run()






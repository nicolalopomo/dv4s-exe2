import streamlit as st

# Data
team_name = "Roma"
seasons = ["1994-95", "1995-96", "1996-97", "1997-98"]
wins = [10, 20, 3, 4]
losses = [34, 23, 34, 4]
over_goals = [56, 56, 49, 92]
top_scorers = {
    "Fonseca": 25,
    "Giannini": 21,
    "Balbo": 15
    }

st.title("Columns")

col1, col2 = st.columns([2, 1])
with col1:
    st.header("Wins")
    st.bar_chart(wins)
with col2:
    st.header("Goals")
    st.table(over_goals)


# Tabs
st.title("Tabs")

tab1, tab2, tab3 = st.tabs(['Wins', 'Losses', 'Players'])

with tab1:
    st.subheader('Wins')
    wins_data = {
        "Seasons": seasons,
        "Wins": wins,
    }
    st.line_chart(wins_data, x="Seasons", y="Wins")

with tab2:
    st.subheader('Losses')
    losses_data = {
        "Seasons": seasons,
        "Losses": losses,
    }
    st.bar_chart(losses_data, x="Seasons", y="Losses")

with tab3:
    st.subheader("Top Players")
    st.area_chart(top_scorers)


st.title("Expanders")
with st.expander("Goals"):
    st.subheader("Goals")
    for i in range(len(seasons)):
        st.write(f"Season {seasons[i]}: Overall Goal Scored: {over_goals[i]}")


st.title("More Columns")

col1img, col2img = st.columns(2, gap='large')
with col1img:
    st.header("Balbo")
    st.image("https://it.wikipedia.org/wiki/File:Abel_Balbo_-_AS_Roma_1995-96.jpg")
with col2img:
    st.header("Fonseca")
    st.image("https://it.wikipedia.org/wiki/File:Daniel_Fonseca_-_AS_Roma_1994-95.jpg")
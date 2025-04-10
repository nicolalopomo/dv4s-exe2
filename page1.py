import streamlit as st
import pandas as pd
import numpy as np

# Metrics
st.title("Metric")

st.metric(label="Nmber of Assists", value="25", delta="+6")

st.metric(label="Goals", value="13", delta="-5")


# Dataframe
st.title(":blue[Dataframe]")

data = {
    "Player's Name": ["Pelè", "Maradona", "Baggio"],
    "Goals": [13, 25, 24],
    "Team": ["Juve","Napoli","Inter"]
}

df1 = pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df1) # display the dataframe

st.subheader("Static Table")
st.table(df1)


# Data
n_goals = np.random.randint(4, 21, size=(38, 3))
player_names = ['Baggio', 'Fonseca', 'Maradona']
df2 = pd.DataFrame(n_goals, columns=player_names)

# Line chart
st.title('Line Chart')
st.line_chart(df2)

# Area chart
st.title('Area chart')
st.area_chart(df2)

# Bar chart
st.title('**Bar** chart')
st.bar_chart(df2)


# Scatter chart
n_matches = 38
x_coord = np.random.rand(n_matches)*100
y_coord = np.random.rand(n_matches)*100
goal_values = np.random.randint(0, 15, size=(n_matches))

goal_colors = np.random.rand(n_matches, 3) # RGB colors
goal_colors_lot = [tuple(c) for c in goal_colors]


goal_data = {
    "X": x_coord,
    "Y": y_coord,
    "Goals": goal_values,
    "Colors": goal_colors_lot
}

df3 = pd.DataFrame(goal_data)

st.scatter_chart(df3, x="X", y="Y", size="Goals", color="Colors")

# Map
n_pos = 100
latitude = np.random.uniform(45.8, 45.9, n_pos) # Latitude of Lecco
longitude = np.random.uniform(9.35, 9.45, n_pos) # Longitude
locations = {
    "lat": latitude,
    "lon": longitude
}

df4 = pd.DataFrame(locations)

st.map(df4)


# Session State
st.title("Session State")
st.session_state['Player'] = "Diego"
st.session_state['Goals'] = 35

st.write("The name is:", st.session_state['Player'])


# Error
st.error('This is an error message')

# Warning
st.warning('This is a warning message!')

# Success
st.success('This is a success message!')

# Info
st.info('This is an info message!')


# Progress bar
import time as t

st.title("Progress Bar")

progress_bar = st.progress(0)

for i in range(101):
    t.sleep(0.01)
    progress_bar.progress(i)

st.success('Computation is complete')


# Spinner
st.title("Here we have a spinner")
with st.spinner('You have to wait!', show_time=True):
    t.sleep(5)

st.success("Task was completed")
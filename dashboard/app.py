import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('Interactive Data Visualization App')

st.markdown('**By Chandra MS**') 
st.markdown('Email:[ ChandraWork23@gmail.com](mailto:ChandraWork23@gmail.com)')

# Load the dataset from a local CSV file
@st.cache_data
def load_data():
    data = pd.read_csv('day.csv')
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

data = load_data()

# Display the dataset
st.write('Dataset:', data.head())

# Check if the required columns exist
required_columns = ['dteday', 'cnt', 'temp', 'atemp', 'hum', 'windspeed']
for col in required_columns:
    if col not in data.columns:
        st.error(f"Column '{col}' not found in the dataset.")
        st.stop()

# Select variable for plotting
variable = st.selectbox('Select variable to plot against daily bike rentals (cnt):', 
                        ['temp', 'atemp', 'hum', 'windspeed'])

# Create a line plot over time
st.write('Total Bike Rentals Over Time')
fig, ax = plt.subplots()
ax.plot(data['dteday'], data['cnt'], label='Total Rentals')
ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.legend()
st.pyplot(fig)

# Create a scatter plot for the selected variable
st.write(f'{variable.capitalize()} vs. Total Bike Rentals')
fig, ax = plt.subplots()
ax.scatter(data[variable], data['cnt'])
ax.set_xlabel(variable.capitalize())
ax.set_ylabel('Count of Bike Rentals')
ax.grid(True)
st.pyplot(fig)

# Create a boxplot for the selected variable
st.write(f'Boxplot of {variable.capitalize()}')
fig, ax = plt.subplots()
ax.boxplot(data[variable])
ax.set_xlabel(variable.capitalize())
ax.set_ylabel('Value')
#ax.grid(True)
st.pyplot(fig)

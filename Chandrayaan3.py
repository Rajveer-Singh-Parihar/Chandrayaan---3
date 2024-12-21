# Exploring and Data Analysis of Chandrayaan 3

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Reading the data
df = pd.read_csv(r"C:\Users\rajve\Downloads\propulsion_module.csv")
#print(df)

# Convert structured data to Data Raw data reconstruction into structured format


# Data for Chandrayaan-3 modules
data = {
    'Module': ['Orbiter', 'Lander', 'Rover'],
    'Mission Life': ['From 170 x 36500 km to lunar polar orbit', '1 Lunar day (14 Earth days)', '1 Lunar day'],
    'Mass (kg)': [448.62, 1749.86, 26],
    'Power Generation (W)': [738, 738, 50],
    'Payloads': [0, 3, 2],
    'Dimensions (mm3)': ['N/A', '2000 x 2000 x 1166', '917 x 750 x 397'],
    'Communication': ['S-Band Transponder (IDSN)', 'ISDN, Ch-2 Orbiter, Rover', 'Lander']
}

# Convert data to DataFrame
df = pd.DataFrame(data)
print("Chandrayaan-3 Data:\n", df)

# Visualization 1: Mass Comparison
plt.figure(figsize=(8, 5))
plt.bar(df['Module'], df['Mass (kg)'], color=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Mass of Orbiter, Lander, and Rover (kg)')
plt.ylabel('Mass (kg)')
plt.show()

# Visualization 2: Power Generation
plt.figure(figsize=(8, 5))
plt.bar(df['Module'], df['Power Generation (W)'], color=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Power Generation for Orbiter, Lander, and Rover (W)')
plt.ylabel('Power (W)')
plt.show()

# Visualization 3: Payloads
plt.figure(figsize=(8, 5))
plt.bar(df['Module'], df['Payloads'], color=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Number of Payloads on Modules')
plt.ylabel('Payloads')
plt.show()

# Visualization 4: Mission Life (Textual)
plt.figure(figsize=(8, 5))
plt.barh(df['Module'], [1, 1, 1], color='lightgrey')
for i, life in enumerate(df['Mission Life']):
    plt.text(0.5, i, life, ha='center', va='center', fontsize=10)
plt.title('Mission Life of Modules')
plt.xticks([])
plt.show()

# Visualization 5: Dimensions (Textual)
plt.figure(figsize=(8, 5))
plt.barh(df['Module'], [1, 1, 1], color='lightgrey')
for i, dim in enumerate(df['Dimensions (mm3)']):
    plt.text(0.5, i, dim, ha='center', va='center', fontsize=10)
plt.title('Dimensions of Modules')
plt.xticks([])
plt.show()

# Plotly Visualization: Combined Mass and Power
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df['Module'], y=df['Mass (kg)'],
    name='Mass (kg)', marker_color='lightskyblue'
))
fig.add_trace(go.Bar(
    x=df['Module'], y=df['Power Generation (W)'],
    name='Power Generation (W)', marker_color='lightgreen'
))
fig.update_layout(
    title='Comparison of Mass and Power for Orbiter, Lander, and Rover',
    xaxis_title='Modules',
    yaxis_title='Values',
    barmode='group'
)
fig.show()


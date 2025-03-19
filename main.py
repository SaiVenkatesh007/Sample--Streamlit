import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Create a dataframe with date, value, and platform data
np.random.seed(42)
df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=100),
    'value': np.random.randn(100).cumsum(),
    'platform': np.random.choice(['Android', 'iOS'], size=100)
})

# Create another dataframe for additional data
df2 = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=100),
    'metric': np.random.randint(50, 150, size=100),
    'platform': np.random.choice(['Android', 'iOS'], size=100)
})

# Streamlit app
st.title("Mini Dashboard")

# Date filter
start_date = st.date_input('Start date', df['date'].min())
end_date = st.date_input('End date', df['date'].max())

# Platform filter
platform_filter = st.selectbox('Select platform', ['All', 'Android', 'iOS'])

# Filter the dataframes based on the date range and platform
df['date'] = pd.to_datetime(df['date']).dt.date
df2['date'] = pd.to_datetime(df2['date']).dt.date

filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
filtered_df2 = df2[(df2['date'] >= start_date) & (df2['date'] <= end_date)]

if platform_filter != 'All':
    filtered_df = filtered_df[filtered_df['platform'] == platform_filter]
    filtered_df2 = filtered_df2[filtered_df2['platform'] == platform_filter]

# Display the filtered dataframes
st.subheader("Engagement Trends")
st.write(filtered_df)

st.subheader("Performance Metrics")
st.write(filtered_df2)

# Plot graphs
st.subheader("Visual Insights")

# Line plot for 'value' over time
st.write("Engagement Over Time")
fig, ax = plt.subplots(figsize=(12, 6))  # Increase the width and height of the graph
for platform in filtered_df['platform'].unique():
    platform_data = filtered_df[filtered_df['platform'] == platform]
    ax.plot(platform_data['date'], platform_data['value'], label=platform, linewidth=2)  # Thicker lines
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Engagement Value", fontsize=12)
ax.set_title("Engagement Trends Over Time", fontsize=16, fontweight='bold')  # Add a title
ax.legend(title="Platform", fontsize=10, title_fontsize=12)  # Add legend title
ax.grid(True, linestyle='--', alpha=0.6)  # Add grid lines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
st.pyplot(fig)

# Bar plot for 'metric' over time
st.write("Performance Over Time")
fig, ax = plt.subplots(figsize=(12, 6))  # Increase the width and height of the graph
for platform in filtered_df2['platform'].unique():
    platform_data = filtered_df2[filtered_df2['platform'] == platform]
    ax.bar(platform_data['date'], platform_data['metric'], label=platform, alpha=0.7, width=0.8)  # Adjust bar width
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Performance Metric", fontsize=12)
ax.set_title("Performance Metrics Over Time", fontsize=16, fontweight='bold')  # Add a title
ax.legend(title="Platform", fontsize=10, title_fontsize=12)  # Add legend title
ax.grid(axis='y', linestyle='--', alpha=0.6)  # Add grid lines for y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
st.pyplot(fig)

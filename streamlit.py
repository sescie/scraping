import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

# Load the clustered data
clustered_data = pd.read_csv("cluster.csv")

# Sidebar title
st.sidebar.title("Cluster Selection")

# Select cluster
selected_cluster = st.sidebar.selectbox("Select Cluster", sorted(clustered_data['cluster'].unique()))

# Display records for selected cluster
st.write(f"Records for Cluster {selected_cluster}:")
cluster_data = clustered_data[clustered_data['cluster'] == selected_cluster]
st.write(cluster_data[['category', 'link']])

# Display additional information if needed
# st.write(cluster_data[['category', 'URL', 'headline', 'summary']])

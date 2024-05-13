from sklearn.cluster import KMeans
import pandas as pd

# Load the data
data = pd.read_csv("spider1.csv")

data.head()

from sklearn.preprocessing import LabelEncoder

# Instantiate LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'Category' column
data['Category_encoded'] = label_encoder.fit_transform(data['category'])

num_clusters = 4

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data[['Category_encoded']])

# Get cluster assignments
cluster_assignments = kmeans.labels_

# Add cluster assignments to the DataFrame
data['cluster'] = cluster_assignments

# Store the updated DataFrame with cluster assignments
data.to_csv('cluster.csv', index=False)
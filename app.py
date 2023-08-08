import streamlit as st
import pandas as pd
import gzip
import json
import matplotlib.pyplot as plt

product_database_path = "data/meta_AMAZON_FASHION.json.gz"

# Function to load and preprocess the data
def load_and_preprocess_data(product_database_path):
    records = []
    with gzip.open(product_database_path, 'r') as file:
        for line in file:
            record = json.loads(line)
            title = record.get('title', '')
            brand = record.get('brand', '')
            price = record.get('price', None)
            asin = record.get('asin', '')
            records.append((title, brand, price, asin))

    df = pd.DataFrame(records, columns=['Title', 'Brand', 'Price', 'ASIN'])
    df['Price'] = pd.to_numeric(df['Price'].str.replace('$', ''), errors='coerce')
    df['Brand'] = df['Brand'].fillna('Unknown')
    return df

# Function to recommend products based on shopper preferences
def recommend_products(df, preferences):
    if preferences['Brand'] and preferences['Brand'] != 'Any':
        df = df[df['Brand'] == preferences['Brand']]
    if preferences['Min_Price']:
        df = df[df['Price'] >= preferences['Min_Price']]
    if preferences['Max_Price']:
        df = df[df['Price'] <= preferences['Max_Price']]
    return df

# Function to create a bar chart of top brands
def plot_top_brands(df):
    top_brands = df['Brand'].value_counts().nlargest(10)
    plt.bar(top_brands.index, top_brands.values)
    plt.xticks(rotation=45)
    plt.title('Top 10 Brands')
    plt.show()

# Main Streamlit interface
st.title('Product Recommendation System')

# Load product database
product_database_path = 'Dataset\meta_AMAZON_FASHION.json.gz' # Update path if needed
product_database = load_and_preprocess_data(product_database_path)

# Plot top brands
st.subheader('Top Brands')
plot_top_brands(product_database)

# Collect preferences
selected_brand = st.selectbox('Select a Brand', options=['Any'] + product_database['Brand'].unique().tolist())
min_price = st.slider('Minimum Price', min_value=0, max_value=1000, value=0)
max_price = st.slider('Maximum Price', min_value=0, max_value=1000, value=500)

preferences = {
    'Brand': selected_brand,
    'Min_Price': min_price,
    'Max_Price': max_price
}

# Recommend products
recommended_products_df = recommend_products(product_database, preferences)
st.subheader('Recommended Products')
st.dataframe(recommended_products_df)

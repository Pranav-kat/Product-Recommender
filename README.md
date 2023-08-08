# Product Recommendation System

## Overview

The Product Recommendation System is a web-based application that provides personalized product recommendations based on user preferences. It allows users to filter products by brand, price range, and other attributes to receive tailored recommendations.

![System Overview](images/overview.png) <!-- Add an image illustrating the overview of the system -->

## Features

- **Product Database**: A comprehensive database of products with attributes such as name, brand, category, and price.
- **User Preferences Interface**: An interactive interface for users to select their product preferences.
- **Recommendation Engine**: Utilizes filtering algorithms to provide personalized product recommendations.

## How It Works

1. **Select Preferences**: Users select their preferences using intuitive dropdowns and sliders.
2. **Get Recommendations**: Based on selected preferences, the system recommends matching products.
3. **Explore Products**: Users can explore the recommended products, view details, and make a purchase.

![How It Works](images/how_it_works.png) <!-- Add an image illustrating how the system works -->

## Technology Stack

- **Data Processing**: Python, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Web Interface**: Streamlit
- **Deployment**: Streamlit Sharing, Heroku

## Installation & Usage

### Prerequisites

- Python 3.x
- Streamlit

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/product-recommendation-system.git
cd product-recommendation-system
```
### Install the required dependencies:

`pip install -r requirements.txt`

#### Run the Streamlit app:

`streamlit run app.py`

Open your browser and navigate to `http://localhost:8501` to access the application.

# Workflow and Model Outline:
### 1. **Loading and Preprocessing Product Data**
   - **Data Source**: The system uses the Amazon Fashion metadata, containing information about various products such as title, brand, and price.
   - **Preprocessing**: The raw data is preprocessed to extract relevant attributes, handle missing values, and convert data types as needed.

### 2. **Shopper Preferences Interface**
   - **Brand Selection**: Users can choose a specific brand from a dropdown menu or select "Any" if they have no brand preference.
   - **Price Range Selection**: Users can define a price range for the products they want to see using two sliders for the minimum and maximum price.
   - **Interactive Interface**: The system uses Streamlit to create an interactive web interface, allowing users to easily input their preferences.

### 3. **Recommendation Engine**
   - **Filtering by Brand**: If a specific brand is chosen, only products from that brand are considered.
   - **Filtering by Price Range**: Products within the specified price range are included in the recommendations.
   - **Result Presentation**: The recommended products are displayed in a table, showing details like the title, brand, and price.

### 4. **Data Visualization**
   - **Top Brands Visualization**: A bar chart displays the top 10 most common brands in the dataset, providing insights into the product landscape.
   - **(Optional) Additional Visualizations**: More visualizations can be added as needed to provide further insights, such as price distribution, category breakdown, etc.

### 5. **Web Deployment**
   - **Streamlit App**: The system is designed as a web application using Streamlit, allowing users to interact with it through a web browser.
   - **Deployment Options**: The app can be deployed to various platforms like Streamlit Sharing or Heroku, making it accessible online.

### Summary

The product recommendation system offers a personalized shopping experience by allowing users to filter products based on their preferences. It leverages a robust dataset, intuitive interface, and straightforward filtering algorithms to provide relevant recommendations.

This prototype offers a foundation that can be further expanded with more advanced recommendation algorithms, additional user preference options, user accounts, integration with e-commerce platforms, and more.
## Contribution

Feel free to fork the project, create a feature branch, and send me a pull request. For bugs, questions, and discussions, please use the [GitHub Issues](https://github.com/yourusername/product-recommendation-system/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/LICENSE.md) file for details.

## Acknowledgments

- Amazon Product Review Dataset
- Streamlit Community

## Contact

Pranav Katte - [pranavkatte07@gmail.com](mailto:pranavkatte07@gmail.com)

Project Link: [https://github.com/yourusername/product-recommendation-system](https://github.com/yourusername/product-recommendation-system)

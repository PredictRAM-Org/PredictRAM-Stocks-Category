import streamlit as st
import pandas as pd

# Load data from categorized_stocks.xlsx
data_path = "categorized_stocks.xlsx"
df = pd.read_excel(data_path)

# Sidebar for user input
st.sidebar.header("Search Stocks")
search_query = st.sidebar.text_input("Enter stock name:")

# Filter data based on user input
filtered_df = df[df['Symbol'].str.contains(search_query, case=False)]

# Display results
if not filtered_df.empty:
    st.subheader("Search Results")
    st.table(filtered_df[['Symbol', 'Volatility', 'Beta', 'Return_on_Investment', 'Debt_to_Equity_Ratio', 'Category']])
else:
    st.warning("No results found.")

# Additional information
st.sidebar.markdown("---")
st.sidebar.markdown("### Additional Information")
st.sidebar.write("This app fetches data from categorized_stocks.xlsx and allows you to search for stocks.")
st.sidebar.write("Columns displayed: Volatility, Beta, Return_on_Investment, Debt_to_Equity_Ratio, Category.")

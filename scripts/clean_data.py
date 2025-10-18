import pandas as pd
import os

# Define file paths
DATA_DIR = '../data/'
ORDERS_FILE = os.path.join(DATA_DIR, 'orders.csv')
CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.csv')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.csv')
OUTPUT_FILE = os.path.join(DATA_DIR, 'merged_data.csv')

def clean_data():
    """
    Reads, cleans, and merges orders, customers, and products CSV files.
    """
    print("Reading CSV files...")
    
    # Read CSV files
    orders_df = pd.read_csv(ORDERS_FILE)
    customers_df = pd.read_csv(CUSTOMERS_FILE)
    products_df = pd.read_csv(PRODUCTS_FILE)
    
    print(f"Orders: {len(orders_df)} rows")
    print(f"Customers: {len(customers_df)} rows")
    print(f"Products: {len(products_df)} rows")
    
    # Clean data
    print("\nCleaning data...")
    
    # Remove duplicates
    orders_df = orders_df.drop_duplicates()
    customers_df = customers_df.drop_duplicates(subset=['CustomerID'])
    products_df = products_df.drop_duplicates(subset=['ProductID'])
    
    # Handle missing values
    orders_df = orders_df.dropna(subset=['OrderID', 'CustomerID', 'ProductID'])
    customers_df = customers_df.fillna({'Location': 'Unknown', 'Email': 'N/A'})
    products_df = products_df.fillna({'Stock': 0})
    
    # Convert date columns
    orders_df['OrderDate'] = pd.to_datetime(orders_df['OrderDate'])
    customers_df['SignupDate'] = pd.to_datetime(customers_df['SignupDate'])
    
    # Standardize text columns
    orders_df['Status'] = orders_df['Status'].str.strip().str.title()
    orders_df['Platform'] = orders_df['Platform'].str.strip().str.title()
    customers_df['Location'] = customers_df['Location'].str.strip().str.title()
    products_df['Category'] = products_df['Category'].str.strip().str.title()
    
    print("Data cleaned successfully.")
    
    # Merge dataframes
    print("\nMerging data...")
    
    # Merge orders with customers
    merged_df = orders_df.merge(customers_df, on='CustomerID', how='left')
    
    # Merge with products
    merged_df = merged_df.merge(products_df, on='ProductID', how='left')
    
    # Calculate revenue
    merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']
    merged_df['Profit'] = (merged_df['Price'] - merged_df['CostPrice']) * merged_df['Quantity']
    
    print(f"Merged data: {len(merged_df)} rows")
    
    # Save merged data
    merged_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nMerged data saved to {OUTPUT_FILE}")
    
    # Display summary statistics
    print("\n=== Summary Statistics ===")
    print(f"Total Orders: {len(merged_df)}")
    print(f"Total Revenue: ${merged_df['Revenue'].sum():,.2f}")
    print(f"Total Profit: ${merged_df['Profit'].sum():,.2f}")
    print(f"\nOrders by Platform:")
    print(merged_df['Platform'].value_counts())
    print(f"\nOrders by Status:")
    print(merged_df['Status'].value_counts())
    
    return merged_df

if __name__ == "__main__":
    print("Starting data cleaning and merging process...\n")
    merged_data = clean_data()
    print("\nProcess completed successfully!")

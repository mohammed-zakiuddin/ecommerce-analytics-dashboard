# ecommerce-analytics-dashboard

A comprehensive Power BI dashboard for tracking and analyzing sales, orders, and customer behavior across multiple e-commerce platforms including Amazon, Shopify, and Noon.

## Project Overview

This project provides an end-to-end analytics solution for e-commerce businesses operating across multiple platforms. The dashboard enables users to:

- Track sales performance and revenue trends
- Monitor order statuses and fulfillment metrics
- Analyze customer behavior and demographics
- Compare performance across different platforms (Amazon, Shopify, Noon)
- Identify top-performing products and categories

## Repository Structure

### 📁 data/
Contains sample CSV files for testing and demonstration:
- **orders.csv** - Order transactions including OrderID, OrderDate, CustomerID, ProductID, Quantity, Price, Platform, and Status
- **customers.csv** - Customer information including CustomerID, Name, Email, Location, and SignupDate
- **products.csv** - Product catalog with ProductID, ProductName, Category, Stock, and CostPrice

### 📁 scripts/
Python scripts for data processing:
- **clean_data.py** - Data cleaning and transformation script that merges the CSV files and prepares them for analysis in Power BI

### 📁 dashboard/
Power BI files:
- **ecommerce_dashboard.pbix** - Power BI dashboard file with visualizations and reports

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Power BI Desktop
- Required Python packages: pandas, numpy

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohammed-zakiuddin/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard
```

2. Install required Python packages:
```bash
pip install pandas numpy
```

### Using the Scripts

1. **Data Cleaning and Preparation:**
   Navigate to the scripts folder and run the data cleaning script:
   ```bash
   cd scripts
   python clean_data.py
   ```
   This script will:
   - Load data from the CSV files in the data/ folder
   - Clean and validate the data
   - Merge the datasets for comprehensive analysis
   - Output cleaned data ready for Power BI import

2. **Opening the Dashboard:**
   - Open Power BI Desktop
   - Navigate to the dashboard/ folder
   - Open ecommerce_dashboard.pbix
   - Refresh the data connections to load the cleaned data

## Features

- **Multi-platform Analysis**: Compare performance across Amazon, Shopify, and Noon
- **Sales Metrics**: Track revenue, order quantities, and average order values
- **Customer Insights**: Analyze customer demographics and purchasing patterns
- **Product Performance**: Identify best-selling products and inventory levels
- **Order Status Tracking**: Monitor delivered, cancelled, and returned orders

## Data Schema

The dashboard integrates three main data sources:

- **Orders**: Transaction-level data with platform, status, and pricing information
- **Customers**: Customer profiles with location and signup dates
- **Products**: Product catalog with categories, stock levels, and cost prices

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or suggestions, please open an issue in this repository.

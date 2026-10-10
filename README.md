# Customer Churn Analysis

This project analyzes customer churn in a telecom dataset using Python and Jupyter Notebook. The goal is to understand which customer behaviors and attributes are associated with churn and to present the findings through data cleaning, exploratory data analysis, and visualizations.

## Project Overview

Customer churn refers to the percentage of customers who stop using a service during a specific period. In this analysis, we explore patterns in customer data to identify factors that contribute to churn, such as:

- Senior citizenship
- Contract type
- Payment method
- Tenure
- Service usage and billing behavior

## Files in the Project

- `project_customer_analysis.ipynb` — main notebook containing the entire analysis workflow
- `project_customer_churn.csv` — dataset used for the churn analysis
- `akshat.py` — additional Python file in the workspace

## Dataset

The dataset contains customer information related to telecom services, including demographic, billing, and service usage details. It includes fields such as:

- CustomerID
- Gender
- SeniorCitizen
- Tenure
- Contract
- MonthlyCharges
- TotalCharges
- PaymentMethod
- Churn

## Objectives

- Load and clean the dataset
- Identify missing or inconsistent values
- Convert categorical/encoded fields into readable formats
- Perform exploratory data analysis (EDA)
- Visualize customer distribution and churn trends
- Detect key churn drivers from the available data

## Tools and Libraries

The notebook uses the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn

## Workflow

The analysis includes the following steps:

1. Import required libraries
2. Load the CSV dataset
3. Check dataset structure and information
4. Clean the `TotalCharges` column by replacing blank values with 0
5. Convert the `SeniorCitizen` field from numeric values to readable labels (`Yes`/`No`)
6. Explore null values and summary statistics
7. Create visualizations for customer and churn patterns
8. Compare churn across different customer segments
9. Draw conclusions from the observed trends

## Key Insights from the Analysis

The notebook highlights several patterns related to churn:

- A significant percentage of customers are churned, with the analysis showing approximately 26.54% churn in the dataset.
- Senior citizens showed a higher churn rate compared to non-senior citizens.
- Customers on month-to-month contracts were more likely to churn than those on one-year or two-year contracts.
- Payment method also influenced churn, with electronic check users showing a higher likelihood of churn.
- Service-related features such as internet service, online security, tech support, and backup services were associated with churn patterns.

## How to Run

1. Open the notebook in Jupyter Notebook or VS Code with Python support.
2. Ensure the dataset file is available in the same project folder.
3. Run the notebook cells sequentially.

Example:

```bash
jupyter notebook project_customer_analysis.ipynb
```

## Requirements

Make sure the following Python packages are installed:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

## Conclusion

This project demonstrates how exploratory data analysis can be used to identify patterns behind customer churn. The findings suggest that contract type, senior citizen status, payment method, and service usage are key areas to investigate for customer retention strategies.

## Author

This notebook and project documentation were created for a customer churn analysis exercise.

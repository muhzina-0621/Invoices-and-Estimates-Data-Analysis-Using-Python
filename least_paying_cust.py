import pandas as pd

# Load the invoices dataset
invoices = pd.read_csv('final_invoices.csv')

# Clean the 'Amount' column to remove non-numeric characters and convert it to numeric
invoices['Amount'] = invoices['Amount'].replace('[^\d.]', '', regex=True).astype(float)

# Ensure 'Date' column is in datetime format
invoices['Date'] = pd.to_datetime(invoices['Date'])

# Customer Analysis
# Identify top-paying customers based on total amount spent
top_paying_customers = invoices.groupby('Code_Name')['Amount'].sum().sort_values(ascending=False)

# Identify least paying customers based on total amount spent
least_paying_customers = invoices.groupby('Code_Name')['Amount'].sum().sort_values(ascending=True)

# Analyze customer behavior of top-paying customers
top_paying_customer_behavior = invoices[invoices['Code_Name'].isin(top_paying_customers.head(10).index)].groupby('Code_Name').agg(
    total_amount=('Amount', 'sum'),
    frequency=('INVOICE_ID', 'count'),
    average_transaction_amount=('Amount', 'mean')
)

# Analyze customer behavior of least paying customers
least_paying_customer_behavior = invoices[invoices['Code_Name'].isin(least_paying_customers.head(10).index)].groupby('Code_Name').agg(
    total_amount=('Amount', 'sum'),
    frequency=('INVOICE_ID', 'count'),
    average_transaction_amount=('Amount', 'mean')
)

# Print the results
print("Top-Paying Customers:")
print(top_paying_customers.head(10))
print("\nTop-Paying Customer Behavior:")
print(top_paying_customer_behavior)
print("\nLeast-Paying Customers:")
print(least_paying_customers.head(10))
print("\nLeast-Paying Customer Behavior:")
print(least_paying_customer_behavior)
top_paying_customer_behavior.to_csv('top_paying_customer_behavior.csv',index=True)
least_paying_customer_behavior.to_csv('least_paying_customer_behavior.csv',index=True)
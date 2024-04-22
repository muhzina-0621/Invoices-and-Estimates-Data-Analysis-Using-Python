import pandas as pd


invoices = pd.read_csv('final_invoices.csv')


most_frequent_customers = invoices['Code_Name'].value_counts().reset_index()
most_frequent_customers.columns = ['Code_Name', 'Frequency']


most_frequent_customers.to_csv('most_frequent_customers.csv', index=False)

print(" Frequent Customers:")
print(most_frequent_customers)

most_frequent_customers.to_csv('Customer_frequency.csv',index=False)


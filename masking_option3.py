import pandas as pd

estimates_df = pd.read_csv('Estimates.csv')
invoices_df = pd.read_csv('Invoices.csv')

def generate_code_name(customer_name):
    # Generate a unique 3-letter combination code
    code_name = ''.join([c.upper() for c in customer_name.split()])[:3]
    return code_name

def mask_customer_name(customer_name):
    # Mask the customer name with only the first and last letters visible
    return customer_name[0] + '*' * (len(customer_name) - 2) + customer_name[-1]

# Convert Customer Names and generate unique code names for both datasets
estimates_df['Code_Name'] = estimates_df['Customer Name'].apply(generate_code_name)
estimates_df['Customer Name'] = estimates_df['Customer Name'].apply(mask_customer_name)

invoices_df['Code_Name'] = invoices_df['Customer Name'].apply(generate_code_name)
invoices_df['Customer Name'] = invoices_df['Customer Name'].apply(mask_customer_name)

# Now, you need to make sure that the code names are the same in both datasets for the same company
# You may want to use a dictionary to store the mapping between original customer names and code names
customer_mapping = {}

for index, row in estimates_df.iterrows():
    customer_mapping[row['Customer Name']] = row['Code_Name']

for index, row in invoices_df.iterrows():
    # If the customer name from invoices dataset exists in the mapping, use the same code name
    # Otherwise, generate a new code name and add it to the mapping
    if row['Customer Name'] in customer_mapping:
        invoices_df.at[index, 'Code_Name'] = customer_mapping[row['Customer Name']]
    else:
        new_code_name = generate_code_name(row['Customer Name'])
        invoices_df.at[index, 'Code_Name'] = new_code_name
        customer_mapping[row['Customer Name']] = new_code_name

# Print the modified datasets
print("Estimates Dataset:")
print(estimates_df)

print("\nInvoices Dataset:")
print(invoices_df)

# Save the modified datasets
estimates_df.to_csv('final_estimates.csv', index=False)
invoices_df.to_csv('final_invoices.csv', index=False)

import pandas as pd
df = pd.read_csv("my_lab_inventory.csv")
print("--- SHRIKANT lOCAL AI DATABASE ---")
print(df)
total_items = df['Quantity'].sum()
print(f"\nTotal items in stock :{total_items}")

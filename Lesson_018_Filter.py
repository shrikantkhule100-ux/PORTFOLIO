import pandas as pd 

df= pd.read_csv("my_lab_inventory.csv")
print(df)

#finding items <6
low_stock=df[df['Quantity']<6]

print("AI_Aleart_Stock")
if low_stock.empty:
  print("all  items are well stocked!")
else:
  print(low_stock)

  #saving this alert list
  low_stock.to_csv("urgent_buy_list.csv",index=False)
  print("\nsuccess: 'Urgent_buy_list.csv' has been created for your boss.")
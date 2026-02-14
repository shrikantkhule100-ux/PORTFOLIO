import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("my_lab_inventory.csv")

plt.bar(df['Item' ],df ['Quantity'],color='skyblue')


plt.title("Shrikant's lab Inventory Levels")
plt.xlabel("Components")
plt.ylabel("Amouunt in stock")

print("openng the chart window..")
plt.show()
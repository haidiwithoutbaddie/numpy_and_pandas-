import numpy as np
sales = np.array([
    [120, 150, 180, 200],
    [90, 110, 130, 170],
    [250, 230, 280, 300],
    [140, 160, 155, 190],
    [200, 210, 195, 240] 
])
print("sale Data: ",sales)
print("shape:",sales.shape)
print("\nTotal sales per product: ")
print(sales.sum(axis=1))

weekly_sales = sales.sum(axis = 0 )
print("\nTotal sales per week: ")
print(weekly_sales)
print("best sales week:",weekly_sales.argmax() + 1 )

count = (sales > 200).sum(axis=1)
print("\nABove 200: ")
print(count)
print("Qualifying products: ")
print(sales[count >=2])

flat = sales.flatten()
print("\nTop 3 sales: ")
print(np.sort(flat)[::-1][:3])

print("\nStandard Deviation per product: ")
print(np.std(sales, axis =1 ))

average = sales.mean(axis = 1)
print("\nAverage sale per product: ")
print(average)
print("best product:",average.argmax()+1)

print("\nSales entries meeting target: ")
print((sales >= 180).sum())
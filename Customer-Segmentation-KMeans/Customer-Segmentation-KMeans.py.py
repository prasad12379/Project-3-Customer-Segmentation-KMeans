import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Mall_Customers.csv")
x=data.iloc[ : , [3, 4]].values
print(x)

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i , init="k-means++" , random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11) , wcss)
plt.xlabel("No of Clusters")
plt.ylabel("WCSS values")
#plt.show()
#from curve we clearly see there are 5 clusters is no of best clusters we can use

kmeans=KMeans(n_clusters=5 , init="k-means++" , random_state=42)
y_kmeans=kmeans.fit_predict(x)
print(y_kmeans)

plt.scatter(x[y_kmeans==0 , 0] , x[y_kmeans==0 , 1] , s=100 , c="red")
plt.scatter(x[y_kmeans==1 , 0] , x[y_kmeans==1 , 1] , s=100 , c="blue")
plt.scatter(x[y_kmeans==2 , 0] , x[y_kmeans==2 , 1] , s=100 , c="indigo")
plt.scatter(x[y_kmeans==3 , 0] , x[y_kmeans==3 , 1] , s=100 , c="green")
plt.scatter(x[y_kmeans==4 , 0] , x[y_kmeans==4 , 1] , s=100 , c="yellow")
plt.scatter(kmeans.cluster_centers_[ : ,0] , kmeans.cluster_centers_[ : ,1] , s=300 , c="black")
plt.show()
import requests
import numpy as np
import matplotlib.pyplot as plt

#requests 
#Это модуль для языка Python, который используют для упрощения работы с HTTP-запросами..
#Она предоставляет разработчику обширный пул функций для работы со всеми видами HTTP-запросов.
url="https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.json())
print(response.status_code)
print(response.headers)

#numpy
#Это библиотека для работы с многомерными массивами.
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[2,2,5],[6,8,6]])
print(a)
print(a.ndim)
print(a+2)
print(a+b)

#matplotlib
#Это библиотека для визуализации данных в Python. Она используется для создания различных видов графиков.

x=[1,2,3,4,5]
y=[20,34,15,26,58]
plt.plot(x,y)
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.plot(x,y,color='blue',marker='o',markersize=9)
plt.title(' график')
plt.show()
plt.scatter(x,y)
plt.show()

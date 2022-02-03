import pandas as pd


# food = pd.read_csv('data/food.csv')
# print(food.head()) #food 데이터 불러오기

acci = pd.read_csv('data/acci.csv', engine='python', encoding='CP949') #에러 UTF-8 engine, encoding
print(acci)
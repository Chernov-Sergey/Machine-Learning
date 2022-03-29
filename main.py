# -*- coding: utf-8 -*-
"""DS_SkillBox.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Chernov-Sergey/5f632000a65a1b0adc3abceb3c3ec872/ds_skillbox.ipynb
"""


import pandas

trips_data = pandas.read_excel("trips_data.xlsx")

trips_data.head()

trips_data.describe()

trips_data.age.hist()

trips_data.target.hist()

trips_data.city.value_counts()

trips_data.head()

df = pandas.get_dummies(trips_data, columns=["vacation_preference", "transport_preference", "city"])

# Разделить данные на "вход" и "выход"
# Задача модели машиннного обучения - найти заканомерность (X, y)
# X - входные данные, т.е. данные, на основе которых будем делать прогоноз
# y - выходные данные, т.е. то, что пытаемся спрогнозировать


y = df.target # Только колонка target
X = df.drop("target", axis=1) # Берем всё, кроме колонки target

# Разделяем данные на тестовую/тренировочную выборку

# Logistic Regression - самая простая модель (алгоритм) машинного обучения

from sklearn.linear_model import LogisticRegression

model = LogisticRegression() # Настройки
model.fit(X,y) # Обучение модели

LogisticRegression()

{ col:[0] for col in X.columns }

example = {
 'age': [70],
 'city_Екатеринбург': [0],
 'city_Киев': [0],
 'city_Краснодар': [0],
 'city_Минск': [0],
 'city_Москва': [0],
 'city_Новосибирск': [0],
 'city_Омск': [0],
 'city_Петербург': [0],
 'city_Томск': [0],
 'city_Хабаровск': [1],
 'city_Ярославль': [0],
 'family_members': [4],
 'salary': [0],
 'transport_preference_Автомобиль': [0],
 'transport_preference_Космический корабль': [0],
 'transport_preference_Морской транспорт': [0],
 'transport_preference_Поезд': [1],
 'transport_preference_Самолет': [0],
 'vacation_preference_Архитектура': [1],
 'vacation_preference_Ночные клубы': [0],
 'vacation_preference_Пляжный отдых': [0],
 'vacation_preference_Шоппинг': [0]}

example_df = pandas.DataFrame(example)

print (model.predict(example_df))
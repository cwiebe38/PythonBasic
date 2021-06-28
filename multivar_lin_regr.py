# Cody Wiebe
# multivar_lin_regr.py
# Starting to try and learn some ML concepts
# Using an example from https://pub.towardsai.net/machine-learning-algorithms-for-beginners-with-python-code-examples-ml-19c6afd60daa
# Creating a simple multivariable linear regression

#Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

# Reading the csv file:
data = pd.read_csv("FuelConsumptionCo2.csv")
data.head

X = data[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 
                                    'FUELCONSUMPTION_COMB', 'FUELCONSUMPTION_COMB_MPG']]

Y = data["CO2EMISSIONS"]

# Splitting up training data vs testing data
train = data[:(int((len(data)*0.8)))]
test = data[(int((len(data)*0.8))):]

# Not as sure of what this section of code does
# the train and test variables are simply 
regr = linear_model.LinearRegression()

train_x = np.array(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 
                                    'FUELCONSUMPTION_COMB', 'FUELCONSUMPTION_COMB_MPG']])

train_y = np.array(train["CO2EMISSIONS"])

test_x = np.array(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 
                                    'FUELCONSUMPTION_COMB', 'FUELCONSUMPTION_COMB_MPG']])

test_y = np.array(test["CO2EMISSIONS"])

regr.fit(train_x,train_y)

# printing the cooeficient values
coeff_data = pd.DataFrame(regr.coef_, X.columns, columns=["Coefficients"])
print(coeff_data)

#Predicting the test values
Y_pred = regr.predict(test_x)

# Getting the variance
R = r2_score(test_y, Y_pred)
print("R^2:", R)

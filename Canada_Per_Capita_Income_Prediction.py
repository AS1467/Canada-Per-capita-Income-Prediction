import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# Load data
df = pd.read_csv("canada_per_capita_income.csv")

# Plotting
%matplotlib inline
plt.xlabel("year")
plt.ylabel("income")

# Create the linear regression model
reg = linear_model.LinearRegression()

# Fit the model
reg.fit(df[['year']], df['income'])

# Predict for the year 2021
prediction = reg.predict([[2021]])
print(f"Predicted income for 2021: {prediction[0]}")

# Scatter plot
plt.scatter(df['year'], df['income'], color="black", marker="+")
plt.plot(df['year'], reg.predict(df[['year']]), color='blue')  # To show the regression line
plt.show()

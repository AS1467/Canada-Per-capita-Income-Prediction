# Canada Per Capita Income Prediction

This project is a simple machine learning exercise to predict Canada's per capita income based on historical data. The dataset used in this project was sourced from the [CodeBasics GitHub repository](https://github.com/codebasics) and is used here to practice linear regression as part of my machine learning learning process.

## Project Overview
The goal of this project is to apply a linear regression model to predict Canada's per capita income for the year 2021 using data from previous years. The data consists of the year and the corresponding income per capita.

### Steps Involved:
1. **Data Loading**: The dataset is loaded from a CSV file (`canada_per_capita_income.csv`).
2. **Model Training**: A linear regression model is trained using the year as the independent variable and income as the dependent variable.
3. **Prediction**: The model is used to predict the per capita income for the year 2021.
4. **Visualization**: The results are visualized with a scatter plot of the data and the regression line.

## Files:
- `canada_per_capita_income.csv`: The dataset with year and income data.
- `income_prediction.py`: The Python script that implements linear regression to predict the income for 2021.

## Libraries Used:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For data visualization and plotting.
- `scikit-learn`: For implementing the linear regression model.

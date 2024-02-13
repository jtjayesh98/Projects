import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import os

def linear_regression(datafile = 'https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv'):
    data = pd.read_csv(datafile)
    if datafile != 'https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv':
        if not os.path.exists(datafile):
            print("Datafile does not exists")
            return
    print("Please choose one of the following as Predictor and Indicator variables: ")
    print(data.columns)
    predictor = input("Predictor Column: ")
    indicator = input("Indicator Column: ")
    if predictor in data.columns and indicator in data.columns:
        X = data[[indicator]]
        y = data[predictor]
        print(X.shape)
        print(y.shape)
        X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)
        model = LinearRegression()

        model.fit(X_train, y_train)

        model.intercept_
        model.coef_

        y_pred = model.predict(X_test)
        
        return model
    
model = linear_regression()
print(model)

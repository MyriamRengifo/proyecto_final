import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

class GrandMeansForecaster:
    def __init__(self, degree=2):
        """
        Initializes the forecaster with a polynomial regression model.
        degree : Degree of the polynomial to fit.
        """
        self.model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    
    def fit_predict(self, df:pd.DataFrame, year):
        """
        Fits the model to the provided data.
        df : DataFrame with columns "año" and "value" for the sake of simplicity.
        """
        df_ordered = df.sort_values(by=["año"])
        X = df_ordered[['año']].values
        y = df_ordered['value'].values
        self.model.fit(X, y)

        pr = self.model.predict([[year]])[0]
        if pr>5:
            pr = 5.0
        elif pr<0:
            pr = 0.0
        
        if year-1 in X:
            prev = df_ordered[df_ordered['año']== year-1 ]["value"].values[0]
        else:
            prev = self.model.predict([[year-1]])[0]
            if prev>5:
                prev = 5.0
            elif prev<0:
                prev = 0.0

        diff = pr - prev
        return [pr, diff]
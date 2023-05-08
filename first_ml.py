import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# Loading the data
oced_bli = pd.read_csv("BLI_24032023162750898.csv", thousands=',')
gdp_per_capita = pd.read_csv("WEOOct2022all.csv", thousands=',', delimeter='\t', encoding='latin1', na_values="n/a")

# Prepare the data
country_stats = prepare_country_stats(oced_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
Y = np.c_[country_stats["Life satisfaction"]]

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
plt.show()

# Select a linear model
model = sklearn.linear_model.LinearRegression()

# Train the model
model.fit(X,Y)

# Make a prediction for Cyprus
X_new = [[22587]]
print(model.predict(X_new))
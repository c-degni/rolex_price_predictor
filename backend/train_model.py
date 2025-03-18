import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data from csv into data frame and drop rows/cols with missing values inplace
df = pd.read_csv('rolex_prices.csv')
df.dropna(inplace = True)

# Specify features
df['year'] = df['year'].replace('Unknown', 0).astype(int)
X = df[['year'], ['condition']]
y = df[['price']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 42)

# Train model using random forest
model = RandomForestRegressor(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)

# Save model as .pkl file
joblib.dump(model, 'rolex_pricing_model.pkl')
print('Model trained and saved as rolex_pricing_model.pkl')
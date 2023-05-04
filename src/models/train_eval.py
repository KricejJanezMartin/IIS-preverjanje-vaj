import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib


df = pd.read_csv('../../data/processed/current_data.csv')

print(df.columns)
print(df.iloc[0])
print(df.dtypes)

cat_cols = df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=['int64']).columns

# Split
X_train, X_test, y_train, y_test = train_test_split(df.drop('final_grade', axis=1),
                                                    df['final_grade'],
                                                    test_size=0.3,
                                                    random_state=42)


preprocessor = ColumnTransformer(transformers=[ ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='error'), cat_cols)
], remainder='passthrough')

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('imputer', SimpleImputer(strategy='median')),
    ('regressor', RandomForestRegressor())
])

pipeline.fit(X_train, y_train)

score = pipeline.score(X_test, y_test)
print(f'Test score: {score:.3f}')

scores = cross_val_score(pipeline, df.drop('final_grade', axis=1), df['final_grade'], cv=5)
mean_score = np.mean(scores)

print(f'Mean score: {mean_score:.3f}')

#shramba modela
joblib.dump(pipeline, '../../models/model.pkl')

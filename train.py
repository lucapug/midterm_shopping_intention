#all imports here..
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('online_shoppers_intention.csv')

df.columns = df.columns.str.replace(r'([a-z])([A-Z])', r'\1_\2', regex=True).str.lower()

strings = list(df.dtypes[df.dtypes == 'object'].index)
for col in strings:
    df[col] = df[col].str.lower()

numeric_features = ['administrative', 'administrative_duration', 'informational',
       'informational_duration', 'product_related', 'product_related_duration',
       'bounce_rates', 'exit_rates', 'page_values', 'special_day',
                    'operating_systems', 'browser', 'region', 'traffic_type']

categorical_features = list(df.dtypes[df.dtypes == 'object'].index)

boolean_features = ['weekend']

target_name = 'revenue'  #True if session ended in a buy

data, target = df.drop(columns=target_name), df[target_name]
target = (target == True).astype(int)

#in splitting, adopted stratify = <target column> , because of the unbalanced distribution
df_train, df_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1,
                                         stratify = target)


train_dict = df_train[numeric_features + categorical_features + boolean_features].to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dict)

model = RandomForestClassifier(max_depth = 15, n_estimators = 1000,
                                    min_samples_leaf = 5, n_jobs = -1, random_state = 1)

model.fit(X_train, y_train)
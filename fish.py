#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
fish_data = pd.read_csv('Fish.csv')

# Preprocessing (example)
# Replace with your own preprocessing steps
X = fish_data[['Length1', 'Length2', 'Length3', 'Height', 'Width']]
y = fish_data['Species']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Save the model
joblib.dump(model, 'fish_model.pkl')


# In[ ]:





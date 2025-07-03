# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('breast_cancer_wisconsin_data.csv')

# Inspect data
print(data.head())

# Drop irrelevant columns
data = data.drop(['id'], axis=1)

# Check for missing values
print(data.isnull().sum())

# Encode target variable (diagnosis: M = Malignant, B = Benign)
le = LabelEncoder()
data['diagnosis'] = le.fit_transform(data['diagnosis'])  # Malignant=1, Benign=0

# Define features and target
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Predict on test set
y_pred = rf.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")

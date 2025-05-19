import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load your dataset
data = pd.read_csv("student_data.csv")  # You need a dataset with 'pass' column

X = data.drop("pass", axis=1)
y = data["pass"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "student_model.pkl")
print("✅ Model trained and saved.")

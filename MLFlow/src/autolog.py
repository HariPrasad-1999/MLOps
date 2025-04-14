import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import dagshub


# Initialize dags repo
dagshub.init(repo_owner='HariPrasad-1999', repo_name='MLOps', mlflow=True)

# Connect to Remote MLFlow 
mlflow.set_tracking_uri("https://dagshub.com/HariPrasad-1999/MLOps.mlflow")


# Load wine dataset
wine = load_wine()
X = wine.data
Y = wine.target

# Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=42)

# Define the params for Random Forest Model
max_depth = 20
n_estimators = 14


# Mention your experiment below
mlflow.autolog()
mlflow.set_experiment('Localtest-1')

with mlflow.start_run():
    rf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rf.fit(X_train, Y_train)

    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(Y_test, y_pred)

    # Creating a Confusion matrix plot
    cm = confusion_matrix(Y_test, y_pred)
    plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')

    # Save Plot
    plt.savefig("Confusion-matrix.png")

    # log artifacts using mlflow
    mlflow.log_artifact(__file__)

    # Tags
    mlflow.set_tags({"Author": 'Hari', "Project": "Wine Classification"})

    print("Accuracy: ", accuracy)

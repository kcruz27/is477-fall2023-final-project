import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
dataset_path = 'data/winequality-red.csv'
df = pd.read_csv(dataset_path, delimiter=';')

# Ensure the 'quality' column is numeric for analytical tasks
df['quality'] = pd.to_numeric(df['quality'], errors='coerce')

# Output directory
output_dir = 'results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# a. Compute summary statistics for 'alcohol' and 'quality'
summary_stats = df[['alcohol', 'quality']].describe()
summary_stats.to_csv(os.path.join(output_dir, 'summary_statistics.csv'))
print("Summary statistics saved to results/summary_statistics.csv")

# b. Simple analytical task: Random Forest classification for 'quality'
# Prepare data for classification
X = df.drop('quality', axis=1)
y = df['quality']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Save results of the classification task
with open(os.path.join(output_dir, 'classification_results.txt'), 'w') as f:
    f.write(f"Accuracy: {accuracy:.2%}\n\nClassification Report:\n{classification_rep}")
print("Classification results saved to results/classification_results.txt")

# c. Simple visualization: Histogram of 'alcohol' content
plt.figure(figsize=(8, 6))
plt.hist(df['alcohol'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'alcohol_distribution.png'))
print("Alcohol distribution plot saved to results/alcohol_distribution.png")

# Show plots if running in an interactive environment
plt.show()
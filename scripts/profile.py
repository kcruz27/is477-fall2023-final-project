import pandas as pd
from ydata_profiling import ProfileReport
import os

# Path to the dataset
dataset_path = './data/winequality-red.csv'

# Read the dataset into a DataFrame
df = pd.read_csv(dataset_path)

# Create a profiling report
profile = ProfileReport(df, title='Dataset Profiling Report')

# Output directory for the report
output_dir = 'profiling'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the report to an HTML file
report_path = os.path.join(output_dir, 'report.html')
profile.to_file(report_path)

print(f"Profiling report saved to: {report_path}")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def corr_matrix(d):
    numerical_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
    # Compute the correlation matrix
    correlation_matrix = d[numerical_cols].corr()
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.show()

def load_data(day_file, hour_file):
    day_data = pd.read_csv(day_file)
    hour_data = pd.read_csv(hour_file)
    return day_data, hour_data
    

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.show()

def analyze_correlation(df):
    # Select only numeric columns for correlation computation
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    return correlation_matrix

def identify_irrelevant_columns(df, threshold=0.1):
    # Identify columns with low variance
    low_variance_cols = df.select_dtypes(include=[np.number]).columns[df.select_dtypes(include=[np.number]).var() < threshold]
    # Combine irrelevant columns
    irrelevant_cols = low_variance_cols.tolist()
    return irrelevant_cols

def summarize_data(df):
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'missing_values': df.isnull().sum().to_dict(),
        'describe': df.describe(include='all').to_dict()
    }
    return summary

def main():
    day_data, hour_data = load_data('data/day.csv', 'data/hour.csv')
    day_data = day_data.head()
    hour_data = hour_data.head()
    # Analyze day data
    day_correlation = analyze_correlation(day_data)
    day_irrelevant_cols = identify_irrelevant_columns(day_data)
    day_summary = summarize_data(day_data)
    
    # Analyze hour data
    hour_correlation = analyze_correlation(hour_data)
    hour_irrelevant_cols = identify_irrelevant_columns(hour_data)
    hour_summary = summarize_data(hour_data)
    
    return {
        'day': {
            'correlation': day_correlation,
            'irrelevant_columns': day_irrelevant_cols,
            'summary': day_summary
        },
        'hour': {
            'correlation': hour_correlation,
            'irrelevant_columns': hour_irrelevant_cols,
            'summary': hour_summary
        }
    }

if __name__ == "__main__":
    results = main()
    for i in results:
        print(f"Analysis for {i}:")
        print("Correlation:")
        print(results[i]['correlation'])
        print("\nIrrelevant Columns:")
        print(results[i]['irrelevant_columns'])
        print("\nSummary:")
        print(results[i]['summary'])
        print("\n")
        print("========================================\n")
        print("========================================\n")
        print("========================================\n") 
    print(results)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def dayTypeBox(d):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='day_type', y='cnt', data=d, order=['Working Day', 'Weekend', 'Holiday'], color='red')
    plt.title('Bike Rentals by Day Type')
    plt.xlabel('Day Type')
    plt.ylabel('Bike Rentals')
    plt.grid()
    plt.show()

def dayTypeBoxNoOutlier(d):
    Q1 = d['cnt'].quantile(0.25)
    Q3 = d['cnt'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    datat_no_outliers = d[(d['cnt'] >= lower_bound) & (d['cnt'] <= upper_bound)]

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='day_type', y='cnt', data=datat_no_outliers, order=['Working Day', 'Weekend', 'Holiday'])
    plt.title('Bike Rentals by Day Type (Outliers Removed)')
    plt.xlabel('Day Type')
    plt.ylabel('Bike Rentals')
    plt.grid()
    plt.show()













def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 6)) 
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar=True, square=True, annot_kws={"size": 8})
    plt.title('Correlation Heatmap')
    plt.show()

def plot_time_series(df, time_column, value_column):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=time_column, y=value_column)
    plt.title(f'Time Series of {value_column} Over {time_column}')
    plt.xlabel(time_column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(df, category_column, value_column):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x=category_column, y=value_column)
    plt.title(f'Bar Chart of {value_column} by {category_column}')
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
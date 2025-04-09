# Bike-Rental-Trends-and-Forecasting
This project explores the bike-sharing demand using the UCI Machine Learning Repository "Bike Sharing" dataset. It includes a complete Exploratory Data Analysis (EDA) to uncover usage patterns and factors affecting bike rentals, followed by a regression-based prediction model to forecast future demand.
Analysis on two datasets: `day.csv` and `hour.csv` (main focus) is done to analyze trends and relationships between variables, visualize the data, and identify any irrelevant columns.

## Project Structure

- **data/**: Contains the datasets used for analysis.
  - `day.csv`: Daily data for trend analysis.
  - `hour.csv`: Hourly data for trend analysis.

- **src/**: Contains source code for data processing and analysis.
  - `data_preprocessing.py`: Functions for data cleaning and preprocessing.
  - `visualization.py`: Functions for creating visualizations.
  - `analysis.py`: Functions for performing statistical analysis.
  - `project.ipynb`: Notebook for loading datasets, performing statistical analysis, and visualizing trends

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

- Load the datasets in `project.ipynb` and perform EDA using the provided functions in the `src` directory.
- Use the functions in `data_preprocessing.py` to clean and preprocess the data as needed.
- Create visualizations using the functions in `visualization.py`.
- Perform statistical analysis and identify irrelevant columns using the methods in `analysis.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

# Custom Data Analysis Class: Advanced Statistical Techniques and Visualization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-green.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-yellow.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-orange.svg)

## 📈 Overview

The **custom-made Data and Analysis class** is a robust framework for performing statistical analysis and visualizing relationships in any numerical dataset. It calculates key metrics such as mean, range, and standard deviation, offering valuable insights into data distribution. The script also generates scatter plots and pair plots to reveal correlations and patterns, making it applicable to a wide range of industries and datasets. Whether for finance, healthcare, or engineering, this tool is designed to help users understand data trends, identify key relationships, and support data-driven decision-making.

## 🚀 Key Features
### `analysis.py`
**`Analysis` Class**: Performs statistical analysis and data visualizations on datasets.
- **Key Features**:
  - Computes key statistics: minimum, maximum, range, mean, variance, and standard deviation for selected data columns.
  - Generates visualizations using `matplotlib` (e.g., scatter plots, pair plots) to help in data interpretation.
  - Supports the creation of scatter plots to analyze relationships between independent and dependent variables.

### `data.py`
**`Data` Class**: Handles data loading and preprocessing from CSV files.
- **Key Features**:
  - Reads and parses CSV files into structured `numpy` arrays, ensuring proper handling of different data types (numeric, categorical, strings, dates).
  - Cleans and processes data to ensure it's ready for analysis, improving the quality and consistency of input data.

## 🎨 Visual Examples

This section highlights the visualizations generated from the concrete data analysis.

### **1. Pair Plot of Concrete Components**
A pair plot showing the relationships between `ash`, `slag`, `strength`, and `water` in the dataset.

<img src="https://github.com/rubythedev/data-analysis-and-visualization/blob/main/images/fig1_pair_plot_concrete.png" width="600">

### **2. Scatter Plot: Strength vs. Water**
This scatter plot visualizes the relationship between the `strength` and `water` content in the concrete mixture.

<img src="https://github.com/rubythedev/data-analysis-and-visualization/blob/main/images/fig2_scatter_strength_water.png" width="400">

### **3. Scatter Plot: Ash vs. Slag**
A scatter plot comparing the `ash` and `slag` content in the concrete mixture.

<img src="https://github.com/rubythedev/data-analysis-and-visualization/blob/main/images/fig3_scatter_ash_slag.png" width="400">

## 🛠️ Technologies & Skills

- **Programming Languages:** 
  - [Python 3.x](https://www.python.org/) for general-purpose programming and data manipulation

- **Libraries & Frameworks:** 
  - [NumPy](https://numpy.org/) for efficient numerical computations and matrix operations
  - [Pandas](https://pandas.pydata.org/) for data manipulation, cleaning, and preprocessing
  - [Matplotlib](https://matplotlib.org/) for data visualization, including 2D plotting and charting

- **Data Science Techniques:** 
  - **Exploratory Data Analysis (EDA):** Visualizing and understanding datasets through summary statistics and plots
  - **Statistical Analysis:** Calculation of key metrics (mean, standard deviation, etc.), hypothesis testing, and distribution analysis
  - **Data Visualization:** Creating intuitive and clear visualizations (scatter plots, pair plots, histograms, etc.) to uncover relationships and trends
  - **Descriptive Statistics:** Providing measures like range, variance, and standard deviation to summarize data characteristics

- **Data Handling & File Formats:** 
  - **CSV & Excel** for importing/exporting data and performing I/O operations with large datasets
  - **Data Preprocessing:** Cleaning, normalizing, and handling missing values in raw data

- **Version Control:**
  - [Git](https://git-scm.com/) for version control and collaborative development
  - [GitHub](https://github.com/) for code hosting, collaboration, and project management

- **Visualization Techniques:** 
  - Creating multi-variable plots to identify relationships and outliers
  - Visualizing distributions with histograms and box plots
  - Customizing plot styles and layouts to enhance readability

## 💡 Why Custom Data and Analysis Class?

This custom-built class is designed to be **universal** and adaptable for any dataset containing numerical values, making it a valuable tool for data analysis across a wide range of domains. Whether you're working with scientific, business, or even financial data, this class can be applied to perform key statistical analysis and generate insightful visualizations. It helps you understand the underlying patterns and trends in your data, enabling you to make informed decisions based on solid statistical evidence.

## 📚 Getting Started

### 🔧 Retrieve Data

1. **Download the Data**
   - Download the zipped folder containing the clean or preprocessed datasets.
   - Place the datasets (e.g., `concrete_data.csv`, `iris_data.csv`) inside the `data` folder.
   - Example folder structure:
     ```
     project_directory/
     ├── data/
     │   ├── concrete_data.csv
     │   └── iris_data.csv
     └── visualizations.py
     ```

2. **Ensure Data is Accessible**
   - Ensure that the `data` folder is in the same directory as your script or project files.
   - This will allow you to easily access the datasets for analysis and manipulation.

### 📝 Usage

1. **Import Necessary Modules**
    ```python
    import os
    from data import Data
    from analysis import Analysis
    ```

2. **Get the Current Directory and Load Dataset**
    ```python
    current_directory = os.getcwd()
    dataset_filename = os.path.join(current_directory, 'data', 'your_dataset.csv')
    dataset_filename = 'data/your_dataset.csv'
    ```

3. **Create Data and Analysis Objects**
    ```python
    dataset_data = Data(dataset_filename)
    dataset_an = Analysis(dataset_data)
    ```

4. **Define Headers for Analysis**
    ```python
    header_list = ['header1', 'header2', 'header3', 'header4']
    ```

5. **Summary of Data (Mean, Range, Standard Deviation)**
    ```python
    data_mean = dataset_an.mean(header_list)
    data_range = dataset_an.range(header_list)
    data_std = dataset_an.std(header_list)
    print('MEANS\n', data_mean, '\nRANGES\n', data_range, '\nSTANDARD DEVIATIONS\n', data_std)
    ```

6. **Generate Pair Plot for Selected Headers**
    ```python
    fig, axes = dataset_an.pair_plot(header_list, title="Figure 1. Relationships Between Variables")
    ```

7. **Generate Scatter Plots**
    ```python
    x_samps, y_samps = dataset_an.scatter('header1', 'header2', 'Figure 2. Header1 vs. Header2')
    x_samps, y_samps = dataset_an.scatter('header3', 'header4', 'Figure 3. Header3 vs. Header4')
    ```

8. **Show Figures**
    ```python
    dataset_an.show()
    ```

### 📈 Example Project: Concrete Data Analysis and Visualization with Custom Data and Analysis Classes

This project demonstrates how to perform statistical analysis and visualizations on concrete data using custom `Data` and `Analysis` classes.

#### **`visualization.py`**
_Performs statistical analysis and visualizations on concrete data._

```python
# Importing necessary modules
import os
from data import Data
from analysis import Analysis

# Get the current directory
current_directory = os.getcwd()

# Get the file path for the concrete data CSV
concrete_filename = os.path.join(current_directory, 'data', 'concrete_data.csv')
concrete_filename = 'data/concrete_data.csv'  # Adjust path if necessary

# Create Data and Analysis objects to use functions from the Data and Analysis classes
concrete_data = Data(concrete_filename)
concrete_an = Analysis(concrete_data)

# Define headers to use for analysis
header_list = ['ash', 'slag', 'strength', 'water']

# Perform statistical summary of the data
data_mean = concrete_an.mean(header_list)
data_range = concrete_an.range(header_list)
data_std = concrete_an.std(header_list)

# Print statistical summaries
print('MEANS\n', data_mean, '\nRANGES\n', data_range, '\nSTANDARD DEVIATIONS\n', data_std)

# Generate pair plot for the defined headers
fig, axes = concrete_an.pair_plot(header_list, title="Figure 1. Components and Strength of Concrete")

# Create scatter plots
x_samps, y_samps = concrete_an.scatter('strength', 'water', 'Figure 2. Water Amount vs. Strength of Concrete')
x_samps, y_samps = concrete_an.scatter('ash', 'slag', 'Figure 3. Ash and Slag Amount in Concrete')

# Show all generated figures
concrete_an.show()


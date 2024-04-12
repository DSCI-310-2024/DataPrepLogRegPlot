# DataPrepLogRegPlot

`DataPrepLogRegPlot` is a Python package tailored for data scientists and analysts focusing on predictive analytics in laptop pricing. This package brings together data cleaning, file copying, logistic regression modeling, and plot saving functionalities to facilitate a smoother workflow from raw data to insights.

## Installation

To install `DataPrepLogRegPlot`, run the following command:

```bash
pip install DataPrepLogRegPlot
```

## Usage

Below are some examples of how you can use the functionalities provided by DataPrepLogRegPlot:

```python
from DataPrepLogRegPlot import copy_file, function_data_cleaning, model, save_plot

# Example file paths
# replace "path/to/..." with the actual file paths you will be using in your project
raw_data_path = "path/to/raw/laptop_prices.csv"
clean_data_path = "path/to/cleaned/laptop_prices.csv"
model_output_path = "path/to/output/model.pkl"
plot_output_path = "path/to/output/performance_plot.png"

# Copy files
copy_file.copy(raw_data_path, clean_data_path)

# Clean your data
cleaned_data = function_data_cleaning.clean_data(clean_data_path)

# Fit a logistic regression model
laptop_price_model = model.fit_logistic_regression(cleaned_data, target_variable="price")

# Save the model performance plot
save_plot.save_performance_plot(laptop_price_model, plot_output_path)
```

## Features

- `copy_file`: Simplifies the process of copying data files from one location to another.
- `function_data_cleaning`: Contains functions for cleaning and preparing data for analysis.
- `model`: Provides an interface to fit logistic regression models, optimized for price prediction tasks.
- `save_plot`: Offers utilities to save various diagnostic and performance plots for models.

## Contributing

We welcome contributions to `DataPrepLogRegPlot`. For more information on how to contribute, please check `CONTRIBUTING.md`. This project adheres to a Code of Conduct outlined in `CONDUCT`.md. By contributing to this project, you agree to abide by its terms.

## License

`DataPrepLogRegPlot` is released under the MIT license, as found in the `LICENSE` file.

## Credits

`DataPrepLogRegPlot` was developed by our Data Scientist team from the University of British Columbia, consisting of [An Zhou](https://github.com/brico12),[Anna Czarnocka]https://github.com/AnnaCzarnocka), [Daniel Lima](https://github.com/daniel1lima) and [Lucas Liu](https://github.com/SugarLucas). We extend our gratitude to all future contributors for their invaluable input.

`DataPrepLogRegPlot` was created using the package template from [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
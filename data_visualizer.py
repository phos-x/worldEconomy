 
# Handles visualization of data.

import matplotlib.pyplot as plt

class DataVisualizer:
    def visualize_country_analysis(self, data):
        # Replace with actual visualization logic for single country analysis
        country = input("Enter the country name or number for analysis: ")
        country_data = data[data['Country'] == country]
        if country_data.empty:
            print(f"No data found for country: {country}")
            return
        country_data.plot(kind='bar', x='Year', y='Value')
        plt.title(f"Analysis for {country}")
        plt.show()

    def visualize_country_comparison(self, data):
        # Replace with actual visualization logic for country comparison
        countries = input("Enter the countries for comparison (comma-separated): ").split(',')
        comparison_data = data[data['Country'].isin(countries)]
        if comparison_data.empty:
            print(f"No data found for countries: {countries}")
            return
        comparison_data.groupby('Country')['Value'].sum().plot(kind='bar')
        plt.title("Country Comparison")
        plt.show()

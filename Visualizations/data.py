import pandas as pd

# Read the csv file and save to a dataframe
cities_df = pd.read_csv('Resources/cities.csv')

# Send dataframe to HTML
cities_df.to_html('Visualizations/data_tables.html', index = False)

# # Save HTML to a string
# cities_string = cities_df.to_html()
# print(cities_string)
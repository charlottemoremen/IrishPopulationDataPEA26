import pandas as pd

# Load the population data
df = pd.read_csv("populationData.csv")

# Filter for the specific criteria: 2024, All ages, Both sexes
filtered_pop = df[
    (df['Year'] == 2024) &
    (df['Age Group'] == 'All ages') &
    (df['Sex'] == 'Both sexes')
]

# Select only the region and population value columns
region_pop_2024 = filtered_pop[['NUTS 3 Region', 'VALUE']].rename(columns={'VALUE': 'Population_2024'})

# Remove the national total row ('Ireland' or 'All regions') to focus on NUTS 3 regions
region_pop_2024 = region_pop_2024[
    (region_pop_2024['NUTS 3 Region'] != 'Ireland') &
    (region_pop_2024['NUTS 3 Region'] != 'All regions')
]

# Convert the population column to a numeric type
region_pop_2024['Population_2024'] = pd.to_numeric(region_pop_2024['Population_2024'])

# Save the filtered data to a new CSV file
region_pop_2024.to_csv("regional_population_2024.csv", index=False)
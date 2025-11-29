import pandas as pd

# Load the data
df = pd.read_csv('populationData.csv')

# 1. Filter for total population rows in 2023 and 2024
df_filtered = df[
    (df['Year'].isin([2023, 2024])) &
    (df['Age Group'] == 'All ages') &
    (df['Sex'] == 'Both sexes') &
    (df['NUTS 3 Region'] != 'Ireland')
].copy()

# 2. Pivot the table to get 2023 and 2024 population values side-by-side per region
df_pivot = df_filtered.pivot_table(
    index='NUTS 3 Region',
    columns='Year',
    values='VALUE'
).reset_index()

# Rename columns for clarity after pivoting
df_pivot.columns = ['NUTS 3 Region', 'Population_2023', 'Population_2024']

# 3. Calculate the total population change
df_pivot['Total Population Change (2024 - 2023)'] = df_pivot['Population_2024'] - df_pivot['Population_2023']

# 4. Select the final columns and sort by change
df_result = df_pivot[['NUTS 3 Region', 'Total Population Change (2024 - 2023)']].sort_values(
    by='Total Population Change (2024 - 2023)',
    ascending=False
)

# 5. Save the result to a new CSV file
output_filename = 'population_change_summary.csv'
df_result.to_csv(output_filename, index=False)
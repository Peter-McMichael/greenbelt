import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv("superheroes.csv", delimiter=";")

# Display the first 10 rows of the DataFrame
print("First 10 rows of the DataFrame:")
head10 = df.head(10)
print(head10)

# Display information about the DataFrame
print("\nInformation about the DataFrame:")
info = df.info()
print(info)

# Drop rows with missing values in the 'Identity' column
print("\nDrop rows with missing values in the \"Identity\" column.")

newdf = df.dropna(subset=["Identity"])

print(newdf.head(10))

# # Fill missing values in the 'Publisher' column with "Unknown"

newdf["Publisher"] = newdf["Publisher"].fillna("N/A")



# # Fill missing values in the 'First appearance' column with 0
newdf["First appearance"] = newdf["First appearance"].fillna("N/A")

# # Fill missing values in the 'Strength' column with 0

newdf["Strength"] = newdf["Strength"].fillna("N/A")

# # Fill missing values in the 'Intelligence' column with "Unknown"

newdf["Intelligence"] = newdf["Intelligence"].fillna("N/A")

# # Display the first 10 rows of the cleaned DataFrame
print("\nFirst 10 rows of the cleaned DataFrame:")

print(newdf.head(10))
# # Save the cleaned DataFrame to a new CSV file


print("\nCleaned data saved to 'cleaned_superheroes.csv'")

newdf.to_csv("superheroes.csv", sep=';', index=False)
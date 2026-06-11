import pandas as pd

# Load dataset
df = pd.read_csv("data/diabetic_data.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Replace missing markers
df = df.replace("?", "Unknown")

# Create target variable
df["readmitted_30"] = df["readmitted"].apply(
    lambda x: 1 if x == "<30" else 0
)

# Select useful columns
columns = [
    "time_in_hospital",
    "num_lab_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "readmitted_30"
]

df = df[columns]

# Save cleaned dataset
df.to_csv("data/cleaned_healthcare_data.csv", index=False)

print(df.head())
print("Final Shape:", df.shape)
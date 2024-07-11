import pandas as pd
import os

# Ensure the working directory is the directory containing the script
script_dir = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(script_dir, 'tbbt.csv')

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Define the output directory and ensure it exists
output_dir = os.path.join(script_dir, 'gen_train')
os.makedirs(output_dir, exist_ok=True)

# Create and write to the text file with UTF-8 encoding in the gen_train directory
output_file_path = os.path.join(output_dir, 'gen_0.txt')
with open(output_file_path, 'w', encoding='utf-8') as f:
    for index, row in df.iterrows():
        f.write(f"{row['person_scene']}:\n")
        f.write(f"{row['dialogue']}\n")
        f.write("\n")

print(f'Saved training data to {output_file_path}')

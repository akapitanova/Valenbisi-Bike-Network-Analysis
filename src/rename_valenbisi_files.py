import os
import re

directory = './data/valenbisi_data'

# Regular expression pattern to match the file names
pattern = re.compile(r'valenbici_(\d{2})-(\d{2})-(\d{4})_(\d{2})-(\d{2})-(\d{2}).csv')

# Function to rename the files
def rename_files(directory):
    for filename in os.listdir(directory):
        # Check if the file name matches the pattern
        match = pattern.match(filename)
        if match:
            day, month, year, hour, minute, _ = match.groups()
            # Create the new file name
            new_filename = f"{day}-{month}-{year}_{hour}-{minute}.csv"
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Call the function to rename files in the directory
rename_files(directory)

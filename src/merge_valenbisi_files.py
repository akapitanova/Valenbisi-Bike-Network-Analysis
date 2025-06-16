import os
import csv
import re

# Define the directory containing the files
directory = './data/valenbisi_data'
out_dir = './data/merged_data'

# Regular expression pattern to match the file names
pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})_(\d{2})-(\d{2}).csv')

# Function to merge files
def merge_files(directory):
    merged_data = []
    identifier = 0
    
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            day, month, year, hour, minute = match.groups()
            file_date = f"{year}-{month}-{day}"
            if file_date < "2023-05-22":
                with open(os.path.join(directory, filename), 'r') as file:
                    lines = file.readlines()
                    lines = lines[1:]
                    for line in lines:
                        row = line.strip().split(';')
                        row.insert(0, f"{day}-{month}-{year} {hour}:{minute}")
                        row.insert(0, identifier)
                        merged_data.append(row)
                        identifier += 1    

    # Write merged data to a new CSV file
    with open(os.path.join(out_dir, 'valenbisi_data.csv'), 'w', newline='') as outfile:
        outfile.write('id;datetime;gid;name;number;address;open;available;free;total;ticket;updated_at;globalid;created_user;created_date;last_edited_user;last_edited_date;geo_shape;geo_point_2d\n')

        for row in merged_data:
            outfile.write(';'.join(map(str, row)) + '\n')

merge_files(directory)


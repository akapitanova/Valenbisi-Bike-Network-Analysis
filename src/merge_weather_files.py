import os
import pandas as pd

# Function to merge all CSV files in a directory
def merge_csv_files(directory):
    merged_data = pd.DataFrame()

    for filename in os.listdir(directory):
        if filename.startswith("weather_") and filename.endswith(".csv"):
            date = filename.split("_")[1].split(".")[0].split('-')
            date = f'{date[2]}-{date[1]}-{date[0]}'


            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)

            # need just first 24 hours if there were more print the date
            if len(df) > 24:
                df = df.head(24)
                print(date)


            # Concatenate date and time columns
            df['datetime'] = date  + ' ' + df['hour'].str[-5:]

            # Drop the original hour column
            df.drop(columns=['hour'], inplace=True)
            merged_data = pd.concat([merged_data, df], ignore_index=True)

    return merged_data

directory = "./data/weather_data"
merged_df = merge_csv_files(directory)
merged_df.to_csv("./data/merged_data/weather_data.csv", index=False)

print("Merged data saved to weather_data.csv")


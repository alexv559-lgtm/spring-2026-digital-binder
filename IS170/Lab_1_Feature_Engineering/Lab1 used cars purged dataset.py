#importing pandas in order to organize data from CSV file 
import pandas as pd 
#reading csv file "used cars.csv" and setting it as df
df = pd.read_csv("used cars.csv")
#making a copy of "vechicles.csv" called df1
df1=df.copy()
#dropping columns that i feel aren't useful for the dataset axis=1 = columns read across
df1.drop("url", axis=1, inplace=True)
df1.drop("image_url", axis=1, inplace=True)
df1.drop("size", axis=1, inplace=True)
df1.drop("region_url", axis=1, inplace=True)
df1.drop("lat", axis=1, inplace=True)
df1.drop("long", axis=1, inplace=True)
df1.drop("county", axis=1, inplace=True)
#renaming the column drive to drivetrain 
df1.rename({'drive': 'drivetrain'}, axis=1, inplace=True)
#dropping rows with NaN values in the specifc columns listed
df1 = df1.dropna(subset=["posting_date", "condition", "state", "price", "odometer",])
#displaying the copied dataset
print(df1)
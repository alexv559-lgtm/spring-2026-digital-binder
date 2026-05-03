#import pandas to begin working the dataset
import pandas as pd
#read cirrhosis file and save it as df
df = pd.read_csv("cirrhosis.csv")
#remove all rows containing NA and save data as df1
df1 = df.dropna()
#print the clean dataset and see the results
print(df1)

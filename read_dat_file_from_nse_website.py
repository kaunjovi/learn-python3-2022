import pandas as pd
import os.path
import requests 

date_of_data = "19082022"
dat_file_name = "MTO_"+date_of_data+".DAT"
dat_file_url_location = "https://archives.nseindia.com/archives/equities/mto/" + dat_file_name 
dat_file_local_location = "./01_raw_data/" + dat_file_name
equity_dat_file= "./02_data/" + dat_file_name


if (not os.path.exists(dat_file_local_location)): 
    print(f"{dat_file_name} not found. Will attempt download of { dat_file_url_location }")

    req = requests.get(dat_file_url_location) 

    with open(dat_file_local_location, "wb+") as output_file : 
        output_file.write(req.content)
    
    print(f"{dat_file_local_location} was downloaded")


col_Names=["one", "two", "SECURITY", "EQ", "TRADED", "DELIVERED", "DELIVERY_PER"]
df = pd.read_csv(dat_file_local_location,  skiprows=4, names = col_Names)

df.drop(["one", "two"], axis=1, inplace=True)
# df.drop(df.columns[0], axis=1, inplace=True)
df = df.loc[df['EQ'] == 'EQ']
df.insert(0, "DATE", date_of_data)
print ( df.head() ) 
df.to_csv(equity_dat_file, mode='w+', index = False)

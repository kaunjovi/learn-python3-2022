import pandas as pd
import os.path
import requests 


def download_bhav_copy( bhav_copy_local, bhav_copy_url) : 
    if (not os.path.exists(bhav_copy_local)): 
        print(f"{ bhav_copy_local } not found. Will attempt download of { bhav_copy_url }")

        req = requests.get( bhav_copy_url , timeout=2)  
        with open(bhav_copy_local, "wb+") as output_file : 
            output_file.write(req.content)
    
    if (os.path.exists(bhav_copy_local)) : 
        print(f"{bhav_copy_local} successfully downloaded.")
        return True
    else : 
        print(f"{bhav_copy_local} could not be downloaded.")
        return False
        

def prepare_bhav_data(bhav_copy_local, bhav_copy_file_2, date_of_data) :
    df = pd.read_csv(bhav_copy_local) 
    df.columns = df.columns.str.strip()
    df['SERIES'] = df['SERIES'].str.strip()
    df['DELIV_PER'] = df['DELIV_PER'].str.strip()
    df = df.loc[df['SERIES'] == 'EQ']
    df.insert(0, "DATE", date_of_data)
    df['DELIV_QTY'] = df['DELIV_QTY'].astype(float)
    df['DELIV_LACS'] = (df['DELIV_QTY'] * df['AVG_PRICE'])/100_000
    df['DELIV_LACS'] = df['DELIV_LACS'].astype('int64')
    df['DELIV_PER'] = df['DELIV_PER'].astype(float)
    df.to_csv(bhav_copy_file_2, mode='w+', index = False)

    print(f"{bhav_copy_file_2} successfully created.")
    

def execute (date_of_data): 

    bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
    bhav_copy_url = "https://archives.nseindia.com/products/content/" + bhav_copy_file 
    bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + bhav_copy_file
    bhav_copy_file_2= "./data_files/12_data_bhavcopy/" + bhav_copy_file
    bhav_copy_file_3 = "./data_files/13_top50/" + bhav_copy_file

    download_bhav_copy ( bhav_copy_local , bhav_copy_url)

    df = prepare_bhav_data (bhav_copy_local, bhav_copy_file_2, date_of_data)

    # print ( df.head() ) 
    df = pd.read_csv(bhav_copy_file_2)
    print("##############################################################################")
    print("50 largest by delivery in lacs, sorted by delivery percentage")
    print("##############################################################################")
    largest_delivery = df.nlargest(30, 'DELIV_LACS')
    largest_delivery['DELIV_QTY'] = largest_delivery['DELIV_QTY'].astype(int)
    largest_delivery.drop(["DATE", "SERIES", "PREV_CLOSE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","LAST_PRICE","CLOSE_PRICE","TURNOVER_LACS"], axis=1, inplace=True)
    print (largest_delivery.sort_values(by=["DELIV_PER"] , ascending = False))
    largest_delivery.to_csv(bhav_copy_file_3, mode='w+', index = False)

    # print("##########################")
    # print("20 largest by delivery percentage")
    # print("##########################")
    # print (df.nlargest(20, 'DELIV_PER'))
    return 0

if __name__ == "__main__": 
    execute("15082022")
    ## what is happening here. 




    

    
import pandas as pd
import os.path
import requests 
from kuber_configurations import KuberConf


def download_bhav_copy( date_of_data ) : 
    
    conf = KuberConf(date_of_data)
    bhav_copy_local = conf.bhav_copy_local
    bhav_copy_url = conf.bhav_copy_url
    
    if (not os.path.exists(bhav_copy_local)): 
        print(f"{ bhav_copy_local } not found. Will attempt download of { bhav_copy_url }")

    try: 
        req = requests.get( bhav_copy_url , timeout=2)  
        with open(bhav_copy_local, "wb+") as output_file : 
            output_file.write(req.content)
    except : 
        print(f"There was some exception while downloading from {bhav_copy_url}.")
    
    if (os.path.exists(bhav_copy_local)) : 
        print(f"{bhav_copy_local} successfully downloaded.")
        return True
    else : 
        print(f"{bhav_copy_local} could not be downloaded.")
        return False
        

def prepare_bhav_data( date_of_data) :

    conf = KuberConf(date_of_data)
    bhav_copy_local = conf.bhav_copy_local
    bhav_copy_file_2 = conf.bhav_copy_file_2

    if (os.path.exists(bhav_copy_local)) :
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

        if (os.path.exists(bhav_copy_file_2)) : 
            print(f"{bhav_copy_file_2} successfully created.")
            return True
        else : 
            print(f"{bhav_copy_file_2} could not be downloaded.")
            return False
    else : 
        print(f"{bhav_copy_local} is not available.")
        return False



def execute (date_of_data): 

    download_bhav_copy ( date_of_data)
    df = prepare_bhav_data ( date_of_data)

    conf = KuberConf(date_of_data)
    bhav_copy_file_3 = conf.bhav_copy_file_3
    bhav_copy_file_2 = conf.bhav_copy_file_2


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
    aprl_1 = ["01082022", "02082022", "03082022", "04082022", "05082022" ]
    mkt_dates = aprl_1

    for mkt_date in mkt_dates : 
        execute( mkt_date )

    li = [] 

    for mkt_date in mkt_dates : 
        conf = KuberConf(mkt_date)
        bhav_copy_file_3 = conf.bhav_copy_file_3

        df = pd.read_csv(bhav_copy_file_3, index_col=None, header=0, usecols=["SYMBOL"])
        li.append(df)

    # count = pd.Series(li).value_counts()
    frame = pd.concat(li, axis=0, ignore_index=True)
    
    print(frame["SYMBOL"].value_counts())


    

    
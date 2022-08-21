import bhav_copy  
import os 

def test_download_bhav_copy_success() : 

    date_of_data = "19082021"
    bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
    bhav_copy_url = "https://archives.nseindia.com/products/content/" + bhav_copy_file 
    bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + bhav_copy_file

    # if the file exists, delete it, so that the entire code 
    # path is executed. 
    if ( os.path.exists(bhav_copy_local)): 
        os.remove(bhav_copy_local)

    assert bhav_copy.download_bhav_copy( bhav_copy_local , bhav_copy_url ), "{date_of_data} should have data."
    
def test_download_bhav_copy_fail() : 
    date_of_data = "asd"    # a date was expected here. 
    bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
    bhav_copy_url = "https://archives.nseindia.com/products/content/" + bhav_copy_file 
    bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + bhav_copy_file

    assert not bhav_copy.download_bhav_copy( bhav_copy_local , bhav_copy_url ), "{asd} should not have data."

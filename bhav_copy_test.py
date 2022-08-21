import bhav_copy  

def test_download_bhav_copy_success() : 
    date_of_data = "19082022"
    bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
    bhav_copy_url = "https://archives.nseindia.com/products/content/" + bhav_copy_file 
    bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + bhav_copy_file

    assert bhav_copy.download_bhav_copy( bhav_copy_local , bhav_copy_url ), "check me out"
    
def test_download_bhav_copy_fail() : 
    date_of_data = "asd"    # a date was expected here. 
    bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
    bhav_copy_url = "https://archives.nseindia.com/products/content/" + bhav_copy_file 
    bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + bhav_copy_file

    try : 
        stats = bhav_copy.download_bhav_copy( bhav_copy_local , bhav_copy_url )
    except Exception as e :
        assert True 
        return 0

    assert False, f"No exception was raised."

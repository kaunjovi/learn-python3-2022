import bhav_copy  
import os 
from configurations import KuberConf

def test_happy_path() : 

    date_of_data = "19082021"
    conf = KuberConf(date_of_data)

    # if the file exists, delete it, so that the entire code 
    # path is executed. 
    if ( os.path.exists(conf.bhav_copy_local)): 
        os.remove(conf.bhav_copy_local)

    assert bhav_copy.download_bhav_copy( date_of_data ), f"{date_of_data} should have data."
    assert bhav_copy.prepare_bhav_data(date_of_data), f"{date_of_data} data could not be prepared for the date. "
    
def test_download_bhav_copy_fail() : 
    date_of_data = "asd"    # a date was expected here. 
    conf = KuberConf(date_of_data)

    assert not bhav_copy.download_bhav_copy( date_of_data ), f"{date_of_data} should not have data."


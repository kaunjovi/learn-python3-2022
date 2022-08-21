class KuberConf : 

    def __init__(self , date_of_data) : 
        self.date_of_data = date_of_data
        self.bhav_copy_file = "sec_bhavdata_full_"+date_of_data+".csv"
        self.bhav_copy_url = "https://archives.nseindia.com/products/content/" + self.bhav_copy_file 
        self.bhav_copy_local = "./data_files/11_raw_data_bhavcopy/" + self.bhav_copy_file
        self.bhav_copy_file_2= "./data_files/12_data_bhavcopy/" + self.bhav_copy_file
        self.bhav_copy_file_3 = "./data_files/13_top50/" + self.bhav_copy_file

# if __name__ == "__main__" : 
#     conf = KuberConf("01012022")
#     print(f"{conf.bhav_copy_file}")
#     print(f"{conf.bhav_copy_url}")
#     print(f"{conf.bhav_copy_local}")
#     print(f"{conf.bhav_copy_file_2}")
#     print(f"{conf.bhav_copy_file_3}")

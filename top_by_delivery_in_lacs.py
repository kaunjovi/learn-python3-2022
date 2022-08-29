from kuber_configurations import KuberConf

if __name__ == "__main__": 
    print(f"Print the names of stocks that are in top N, by delivery in lacs.")

    topLacs_folder = KuberConf.get_topLacs_folder()
    print(f"Consider all files in folder {topLacs_folder} for topLacs delivery report.")

    
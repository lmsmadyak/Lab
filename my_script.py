import requests
import pandas, numpy
import matplotlib
from datetime import datetime
import os,shutil, fnmatch
import time

def city_list():
    string = str()
    with open(r"C:\Users\madya\Desktop\2\download_collection\cities.txt", "r") as file:
        string = file.readline()
    city_list = string.split(" ")
    city_list = ("".join(city_list)).split(",")
    city_list.pop(-1)
    return city_list


def csv_file_name(province):
    csv_list = fnmatch.filter(os.listdir(r"C:\Users\madya\Desktop\2\download_collection\VHI"),"*.csv")
    file_name = str()
    for k in csv_list:
        if k.find(province) >= 0:
            file_name = k
            break
    return file_name


def data_frame_filter(province,year=2017, index="VHI", min=0, max=53):
    file_name = csv_file_name(province)
    df = pandas.read_csv(r"""C:\Users\madya\Desktop\2\download_collection\VHI\{}""".format(file_name))
    df = df[(df['week'] >= min) & (df['week'] <= max)]
    df_1 = df[(df['year'] == year)]
    filter_df = df_1[['year','week',index]]
    return filter_df

# import geopandas as gpd
import pandas as pd

user_file = pd.read_csv('users.csv')
marker_files = pd.read_csv('marker_sample_file.csv')

# create a wkt column
user_file['wkt'] = str(user_file['Longcorner1']) +" "+ str(user_file['Latcorner1']) +" ," + str(user_file['Longcorner2']) +" "+ str(user_file['Latcorner2'])+", "+ str(user_file['Longcorner3']) +" "+ str(user_file['Latcorner3'])+", "+ str(user_file['Longcorner4']) +" "+ str(user_file['Latcorner4'])

print(user_file['wkt'].head())


def in_rectangle(df):
    for marker_files.iterrows()
user_file['in_rectangle'] = user_file.apply(in_rectangle)

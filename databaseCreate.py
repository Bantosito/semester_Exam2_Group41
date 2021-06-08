#The purpose of this program is to load the geoJson and csv file, prepare a version of DATAframe that can be handled by the MySql database 
# (Geographical object are replaced with cordinates from the csv file as two seprarate columns "xAxis","yAxis")
# The dataframe is than uploaded to the database where it injects the "chargingStations" table with the given data
#Important this file should be executed only once to avoid issues and data redundancy

#Created by group 41
#last change 08.06.2021

import geopandas as gpd #library used to load the GeoJson file and creating geoDataframe from it
import pandas as pd # Library used to load and handle csv file as well as send the prepared dataframe to the mySql database
from sqlalchemy import create_engine #Library used to establish connection with the database, Does the same purpose as Mysql.connector

user = 'root'       #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
passw = 'Bantos 180' #!!!PLEASE CHANGE THE PASSWORD TO THE PASSWORD OF YOUR DATABASE!!!!
host = 'localhost' #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
port = 3306        #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
database = 'reCharge' 

#Creating connection with the database based on the data above
mydb = create_engine('mysql+mysqlconnector://' + user+ ' :'+ passw + '@' + host + ':' + str(port) + '/' + database, echo=False)


chargers = gpd.read_file("export.geojson") #Parse the geoJsonFile
chargers = pd.DataFrame(chargers.drop(columns='geometry')) #drop the geographcal part of it in order to handle it properly by mySql database 
chargers = pd.DataFrame(chargers.drop(columns='@id')) #drop the redundant column (id column == @id column)
chargers = chargers.iloc[1: , :]    #Cut out the first row which consists of the data of the whole area of Denmark which will be not necceseary in
chargers = chargers.reset_index(drop=True) #It resetes the index to start counting from 0 again
geometrics = pd.read_csv("charging_station.csv") #creats a dataframe from csv file that it reads
geometrics = geometrics[['xAxis', 'yAxis']] # exracts xAxis yAxis columns from it
chargers = chargers.join(geometrics) # add xAxis yAxis columns to final chargers join
chargers = chargers.rename(columns={"socket:chademo" : "chademo","socket:type2" : "type2", "socket:type2_combo" : "type2combo"}) #renames columns for the analitics purposes
    
chargers.to_sql (name="chargingStations",con = mydb, if_exists = 'append', index=False ) #Send to sql database
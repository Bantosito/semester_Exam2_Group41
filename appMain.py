import mysql.connector
import geopandas as gpd 
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
from sqlalchemy import create_engine

chargers = gpd.read_file("export.geojson")
chargers = pd.DataFrame(chargers.drop(columns='geometry'))
chargers = chargers.iloc[1: , :]
chargers = chargers.reset_index(drop=True)

geometrics = pd.read_csv("charging_station.csv")

geometrics = geometrics[['xAxis', 'yAxis']]
chargers=chargers.join(geometrics)
 
user = 'root'
passw = 'Bantos 180'
host = 'localhost'
port = 3306
database = 'reCharge' 

mydb = create_engine('mysql+mysqlconnector://' + user+ ' :'+ passw + '@' + host + ':' + str(port) + '/' + database, echo=False)

BBox= (55.7143,55.6228,12.5831,12.6561)

photo = plt.imread("mapCPH.png")
fig, ax = plt.subplots(figsize = (8,7))
#ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title("DUpaaaa")
ax.set_xlim(55.7143,55.6228)
ax.set_ylim(12.5831,12.6561)
ax.imshow(photo, zorder=0, extent = BBox, aspect= 'equal')
plt.show()
#chargers.to_sql (name="chargingStations",con = mydb, if_exists = 'replace', index=False )

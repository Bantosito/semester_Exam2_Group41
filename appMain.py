import mysql.connector
import geopandas as gpd 
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
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

BBox= (12.4829,12.6685,55.6245,55.7260)


#chargers.to_sql (name="chargingStations",con = mydb, if_exists = 'replace', index=False )

df = pd.read_sql_table("chargingStations",con= mydb)
df['xAxis'] = df['xAxis'].str.replace(',', '.').astype(float)
df['yAxis'] = df['yAxis'].str.replace(',', '.').astype(float)

print(df)
dupa = df[df["operator"] == "Clever"]
print(dupa )

photo = plt.imread("mapFinal.png")
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(dupa.xAxis, dupa.yAxis, zorder=1, alpha= 1, c='r', s=10)
ax.set_title("Chargers")
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(photo, zorder=0, extent = BBox, aspect= 'equal')
plt.show()

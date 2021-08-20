#This file creates the logic of the whole program in a separate functions, but in order to work they need to be executed externally.
#this is handled by UserInterface.py
#This is only to present the functionality of possible solution as the shown should be treated as a demonstration


import pandas as pd # Library used to handle, filter the data as well connecting and downloading the data from the database
import matplotlib.pyplot as plt #library used to plot the chargers location on the photo of the map
from sqlalchemy import create_engine #Library used to establish connection with the database, Does the same purpose as Mysql.connector

# Data used to establish connection with the database

user = 'root'       #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
passw = 'Bantos 180' #!!!PLEASE CHANGE THE PASSWORD TO THE PASSWORD OF YOUR DATABASE Server!!!!
host = 'localhost' #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
port = 3306        #PLEASE LEAVE IF USING DIFFERENT THAN LOCAL MYSQL SERVER
database = 'reCharge' #Name of the database that is created while executing


#Creating connection with the database based on the data above
mydb = create_engine('mysql+mysqlconnector://' + user+ ' :'+ passw + '@' + host + ':' + str(port) + '/' + database, echo=False)

#List used to determine and store the real life coordinates of the map used inside the graph
BBox= (12.4829,12.6685,55.6245,55.7260)

#Function that imports the charging station table from the database and changes xAxis yAxis columns from strings to values(floats)
def fromSqlFileImport():
    global df #make possible to acces the "df" dataframe outside the function
    df = pd.read_sql_table("chargingStations",con= mydb)
    df['xAxis'] = df['xAxis'].str.replace(',', '.').astype(float)
    df['yAxis'] = df['yAxis'].str.replace(',', '.').astype(float)


#Function used to sort the chargers based on the operator
def chargerCompanySort(allOperators,clever,tesla,ionity,sperto,eon):
    global filteredOperators
    global df
    #Logic: 1. checks if "allOperator" equals 1 then outputs all the chargers there are
    if allOperators == 1:
       filteredOperators = df

    #2. If not it checks if any of the other variables equals 1. 
    # If so it adds filtered rows of the intial dataFrame to an empty one in order to fulfill the filtering requiremens
    #First a new dataframe is established (line 40) than another "throwaway" database is created to take the filtered data from the database table.
    #After that the content of the throwaway database is added to the filteredOperators that than is being passed to "chargerFunctionSort" function
    #It happens with each variable
    elif clever == 1 or tesla == 1 or ionity ==1 or sperto == 1 or eon == 1:
        filteredOperators = pd.DataFrame()
        if clever == 1:
            chargerReference = df[(df["operator"] == "Clever")] 
            filteredOperators = filteredOperators.append(chargerReference)
            chargerReference = df[(df["operator"] == "clever")]
            filteredOperators = filteredOperators.append(chargerReference)
        if tesla == 1:
            chargerReference = df[df["operator"] == 'Tesla Motors Inc.']
            filteredOperators = filteredOperators.append(chargerReference)
        if ionity == 1:
            chargerReference = df[df["operator"] == 'Københavns Kommune']
            filteredOperators = filteredOperators.append(chargerReference)
        if sperto == 1:
            chargerReference = df[df["operator"] == 'Sperto'] 
            filteredOperators = filteredOperators.append(chargerReference)
        if eon == 1:
            eonList = ["E-on","e-on","E.ON","Eon","e.On","eon"]
            for i in range(len(eonList)):
                chargerReference = df[(df["operator"] == eonList[i])]
                filteredOperators = filteredOperators.append(chargerReference)
    #3. If no row is checked it tells the program to plot every charger point
    else:
        filteredOperators = df # it equals allOperators == 1

# Function works similar to the one above but this time it starts with end dataframe of the function above
# Its purpose is to create a final dataframe that will be used to ploth the graph.
def chargerFunctionSort(chademo, ccs2, type2Combo, twoSpots, allNight):
    global filteredOperators
    global chargerFunctions
    if chademo == 1 or ccs2 == 1 or type2Combo == 1 or twoSpots == 1 or allNight == 1:
        chargerFunctions = pd.DataFrame()
        if chademo == 1:
            helper = filteredOperators[filteredOperators.chademo.notnull()]
            chargerFunctions = chargerFunctions.append(helper)
        if ccs2 == 1:
            helper = filteredOperators[filteredOperators.type2.notnull()]
            chargerFunctions = chargerFunctions.append(helper)
        if type2Combo == 1:
            helper = filteredOperators[filteredOperators.type2combo.notnull()]
            chargerFunctions = chargerFunctions.append(helper)
        if twoSpots == 1:
            helper = filteredOperators[(filteredOperators["capacity"] != 2)]
            chargerFunctions = chargerFunctions.append(helper)
            helper = filteredOperators[(filteredOperators["capacity"] != 1)]
            chargerFunctions = chargerFunctions.append(helper)
        if allNight == 1:
            helper = filteredOperators[(filteredOperators["opening_hours"] == "24/7")]
            chargerFunctions = chargerFunctions.append(helper)
    else:
        chargerFunctions = filteredOperators


#Function below prepares and than plots the graph based on the "chargerFunctions" dataFrame it receives

def plotChargersMap():
    global chargerFunctions
    global filteredOperators
    photo = plt.imread("mapFinal.png") #load the image

    fig, ax = plt.subplots(figsize = (8,7)) #create a graph presenting more than one data source (photo and charging points in this case)
    ax.scatter(chargerFunctions.xAxis, chargerFunctions.yAxis, zorder=1, alpha= 1, c='r', s=10)
    ax.set_title("Map of chargers") #set the title of graph
    ax.set_xlim(BBox[0],BBox[1]) #set the limits of xAxis
    ax.set_ylim(BBox[2],BBox[3])#set the limits of yAxis
    ax.imshow(photo, zorder=0, extent = BBox, aspect= 'equal') # show the image
    plt.show()#show the graph
    filteredOperators = pd.DataFrame() #reset the dataframe to allow the whole procedure to go again and again

#load the database in order to work on it
fromSqlFileImport()
reCharge v 1.0
------------------------------------------------------------------------------------

This is a guide on how to preapre the database and computer to properly use the program and database.

DATABASE SETUP
---------------------------------------------------------------------------------
1. Execute quieries that can be found inside "SQLquieries.sql" in order to create the database and its inner connections. 
2. Execute "mySQLData.sql" queries to inject demonstrative data inside the tables.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

PARSING CSV/GEOJSON AND INJECTING DATA TO THE DATABASES CHARGINGSTATIONS TABLE
---------------------------------------------------------------------------------
1. Make sure you have pandas and geopandas libraries as well as sqlalchemy library installed for python 3 
 (following commands are intended for use with "pip" package management system)

	pip install pandas
	pip install geopandas
	pip install sqlalchemy

2. Change password (row13) to the personal mySql server (and other data from rows 12-16 if using external server) to be able to establish connection with your database engine

3. To inject the data you must compile "databaseCreate.py" with Python 3.8.4+
   (May work with older versions of Python 3 too.)
  
Contents of the chargingStations is created by mixing and exporting export.geojson and charging_station.csv files
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

RUNNING THE PROGRAM
-----------------------------------------------------------------------------------
1. Make sure you have all the prevoius libraries installed as well as matplotlib installed for python 3 
	both tkinter and PIL are standard libraries and they should be recognized without any additional downloads
 (following commands are intended for use with "pip" package management system)

	pip install pandas
	pip install matplotlib

	("pip install tkinter:" and "pip install PIL" in case they don't work "out of the box" )
	

2.To run our code you must compile "appMain" with Python 3.8.4+
   (May work with older versions of Python 3 too.)

3. reCharge has GUI (graphical user interface) and is operated using mouse. 
	After opening map its window has to be closed to be able to make any changes.

In case there is no data shown on the map it means that no charger fits the given criteria in the area.
(dots representing the locations can still be found on the graph although without the map underneath due to the limitation of .png photo file)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
ReCharge is an addition to the mockup app "reCharge" that can be found and tested here:

https://xd.adobe.com/view/c5ea2002-3557-4928-976d-1f96d6275278-90b9/

It is a functional mockup presenting both basic functions and overal design of it.
Python program shows map functionalities,data filtering, working with databases as well as working with already existing data
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Created by group 41
08.06.2021
Copenhagen

-----------------------------------------------------------------------------------

All files, and changes can be accesed on the project GitHub:

https://github.com/Bantosito/semester_Exam2_Group41.git
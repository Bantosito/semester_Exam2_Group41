use reCharge;
-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: reCharge
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'AB 55483','TESLA ','MODEL 3','EV','55kWh'),(2,'DE 45832','TOYOTA','PRIUS PRIME','PHEV','8.8kWh'),(3,'CS 32318','WV','ID.3','EV','45kWh'),(4,'AA 22198','DACIA','SPRING','EV','26.8kWh');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `chargings`
--

LOCK TABLES `chargings` WRITE;
/*!40000 ALTER TABLE `chargings` DISABLE KEYS */;
INSERT INTO `chargings` VALUES (1,4,300,2,'2021-03-21 20:20:10','2021-03-21 22:40:10',135,'23kWh',1),(2,2,237,3,'2021-04-13 16:22:30','2021-05-13 17:53:30',110,'20kWH',0),(3,3,123,4,'2021-04-13 13:57:30','2021-04-13 14:30:04',83,'17kwH',0),(4,1,25,1,'2021-05-13 16:22:30','2021-05-14 07:45:26',260,'39kWh',5),(5,1,64,1,'2021-05-18 23:22:30','2021-05-19 08:02:30',180,'28kWh',3);
/*!40000 ALTER TABLE `chargings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `chargingStations`
--

LOCK TABLES `chargingStations` WRITE;
/*!40000 ALTER TABLE `chargingStations` DISABLE KEYS */;
/*!40000 ALTER TABLE `chargingStations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creditCard`
--

LOCK TABLES `creditCard` WRITE;
/*!40000 ALTER TABLE `creditCard` DISABLE KEYS */;
INSERT INTO `creditCard` VALUES (1,'4556 6988 2155 7171',1,'10/2025',888),(2,'5212 9205 0903 1011',2,'1/2023',708),(3,'4929 9509 7345 0311',2,'2/2022',740),(4,'5454 1816 8478 5734',4,'4/2023',600);
/*!40000 ALTER TABLE `creditCard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
INSERT INTO `gender` VALUES (1,'female'),(2,'male');
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'laco','Oosieng9t','Michael','Oosieng9t',2,'MichaelAOlsen@jourrapide.com','81-23-40-51',4,4,'2020-08-21 23:10:00',1),(2,'Andre.bamber','eezahH7aim','Anna','Bruun',1,'AnnaOBruun@dayrep.com','26-22-37-81',1,2,'2021-01-03 14:50:33',1),(3,'Capand','GeeN3iecoo','Sarah ','Nørgaard',1,'SarahJNorgaard@rhyta.com','81-23-40-51',3,1,'2020-10-21 08:10:30',1),(4,'Brok1974','buaMa3anieloh','Christoffer','Mikkelsen',2,'ChristofferSMikkelsen@teleworm.us','60-50-06-35',2,3,'2021-04-11 18:50:30',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-08 19:44:29

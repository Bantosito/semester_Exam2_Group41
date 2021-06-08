--It's a 1 to 1 export from our database which consists of many different files we created 



CREATE DATABASE  IF NOT EXISTS `reCharge` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `reCharge`;
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
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `ID` int NOT NULL,
  `plateNumbers` varchar(10) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `evType` varchar(50) DEFAULT NULL,
  `batteryCapacity` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chargings`
--

DROP TABLE IF EXISTS `chargings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chargings` (
  `ID` int NOT NULL,
  `IDuser` int DEFAULT NULL,
  `IDcharger` int DEFAULT NULL,
  `IDcar` int DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  `price` int DEFAULT NULL,
  `energyConsumed` varchar(20) DEFAULT NULL,
  `hoursParked` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `IDuser` (`IDuser`),
  KEY `IDcar` (`IDcar`),
  CONSTRAINT `chargings_ibfk_1` FOREIGN KEY (`IDuser`) REFERENCES `user` (`ID`),
  CONSTRAINT `chargings_ibfk_2` FOREIGN KEY (`IDcar`) REFERENCES `car` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chargings`
--

LOCK TABLES `chargings` WRITE;
/*!40000 ALTER TABLE `chargings` DISABLE KEYS */;
/*!40000 ALTER TABLE `chargings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chargingStations`
--

DROP TABLE IF EXISTS `chargingStations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chargingStations` (
  `id` text,
  `amenity` text,
  `capacity` text,
  `operator` text,
  `authentication:membership_card` text,
  `fee` text,
  `motorcar` text,
  `opening_hours` text,
  `chademo` text,
  `truck` text,
  `authentication:none` text,
  `socket:cee_blue` text,
  `access` text,
  `type2` text,
  `bicycle` text,
  `car` text,
  `name` text,
  `socket:tesla_supercharger` text,
  `website` text,
  `ref` text,
  `source` text,
  `socket:type2:output` text,
  `socket:chademo:output` text,
  `socket:type2_combo:output` text,
  `note` text,
  `bike` text,
  `scooter` text,
  `socket:type2:current` text,
  `motor_vehicle` text,
  `phone` text,
  `socket:schuko` text,
  `charge` text,
  `payment:Tesla_Account` text,
  `type2combo` text,
  `amperage` text,
  `parking:fee` text,
  `voltage` text,
  `fixme` text,
  `description` text,
  `note:de` text,
  `authentication:phone_call` text,
  `charging_station:output` text,
  `brand` text,
  `level` text,
  `layer` text,
  `url` text,
  `covered` text,
  `socket:ccs` text,
  `authentication:nfc` text,
  `vehicle` text,
  `mapillary` text,
  `operator:wikidata` text,
  `check_date` text,
  `socket:type1_combo` text,
  `socket:tesla_supercharger:output` text,
  `start_date` text,
  `authentication:app` text,
  `maxstay` text,
  `self_service` text,
  `manufacturer` text,
  `model` text,
  `payment:credit_cards` text,
  `xAxis` text,
  `yAxis` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `creditCard`
--

DROP TABLE IF EXISTS `creditCard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditCard` (
  `ID` int NOT NULL,
  `number` int DEFAULT NULL,
  `owner` int DEFAULT NULL,
  `expDate` text DEFAULT NULL,
  `ccv` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditCard`
--

LOCK TABLES `creditCard` WRITE;
/*!40000 ALTER TABLE `creditCard` DISABLE KEYS */;
/*!40000 ALTER TABLE `creditCard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender`
--

DROP TABLE IF EXISTS `gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gender` (
  `ID` int NOT NULL,
  `gender` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `ID` int NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `IDgender` int DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phoneNumber` varchar(20) DEFAULT NULL,
  `IDcreditCard` int DEFAULT NULL,
  `IDcar` int DEFAULT NULL,
  `creationDate` datetime DEFAULT NULL,
  `isActive` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `IDgender` (`IDgender`),
  KEY `IDcreditCard` (`IDcreditCard`),
  KEY `IDcar` (`IDcar`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`IDgender`) REFERENCES `gender` (`ID`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`IDcreditCard`) REFERENCES `creditCard` (`ID`),
  CONSTRAINT `user_ibfk_3` FOREIGN KEY (`IDcar`) REFERENCES `car` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
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

-- Dump completed on 2021-06-08 16:05:46

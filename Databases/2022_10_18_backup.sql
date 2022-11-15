-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: epam_hometask
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(18) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Ivan','Petrov',18,'petrov@test.ua','+380501234567'),(2,'Иван','Петров',81,'ivpetrov@test.ua','+480501234567'),(3,'Petrov','Ivan',81,'petroviv@test.ua','+580501234567'),(4,'Petr','Ivanov',19,'petrov1@test.ua','+680501234567'),(5,'Петр','Иванов',20,'petrov2@test.ua','+780501234567'),(6,'Иван','Иванов',21,'petrov3@test.ua','+880501234567'),(7,'Максим','Петров',22,'petrov4@test.ua','+980501234567'),(8,'Maksim','Petrov',23,'petrov5@test.ua','+180501234567'),(9,'Sergey','Sergeev',24,'petrov6@test.ua','+280501234567'),(10,'Maksim','Sergeev',25,'petrov7@test.ua','+381501234567');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer2`
--

DROP TABLE IF EXISTS `customer2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer2` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(18) NOT NULL,
  `date_of_registration` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer2`
--

LOCK TABLES `customer2` WRITE;
/*!40000 ALTER TABLE `customer2` DISABLE KEYS */;
INSERT INTO `customer2` VALUES (2,'Иван','Иванов',21,'petrov3@test.ua','+880501234567',NULL),(3,'Максим','Петров',22,'petrov@test.ua','+380501234567','2022-10-17 16:19:19');
/*!40000 ALTER TABLE `customer2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1014809,'лопата саперная Solid',752.46),(2,1003455,'лопата штыковая Solid',751.25),(3,1001567,'лопата штыковая SmartFit',660.14),(4,1027039,'грабли Xact M',579.03),(5,1000621,'лопата саперная',488.92),(6,1000685,'разрыхлитель QuikFit',397.81),(7,1027112,'корнеудалитель Xact',206.7),(8,1003459,'вилы для компоста Solid',115.69),(9,1000655,'грабли-аэратор QuikFit',224.58),(10,1027037,'грабли для листьев Xact L',333.47),(11,133433,'грабли для листьев Xact',442.36);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sale_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES (1,3,1003455,2),(2,4,1001567,3),(3,5,1027039,4),(4,6,1000621,5),(5,7,1000685,6),(6,8,1027112,7),(7,9,1003459,8),(8,10,1000655,9),(9,9,1027037,10),(10,8,133433,11),(11,7,1014809,12),(12,6,1003455,13),(13,5,1001567,14),(14,4,1027039,15),(15,3,1000621,16),(16,2,1000621,17);
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-18  9:24:54

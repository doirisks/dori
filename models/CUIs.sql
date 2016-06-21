-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: doiarchive
-- ------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `models`
--

DROP TABLE IF EXISTS `CUIs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUIs` (

  `CUI` varchar(255) NOT NULL,      /*identification*/
  `name1` varchar(255),
  `name2` varchar(255),
  `name3` varchar(255),
  
  `must` TEXT,                      /*relations to models*/ 
  `mustnot` TEXT,
  `input` TEXT,
  `outcome` TEXT,
  `output` TEXT,
  
  `equivalent` TEXT,                /*relations to other CUIs*/
  `derivable` TEXT,
  `derivedfrom` TEXT,

  `units` varchar(255),                     /*program features*/
  `defaultupper` varchar(20),
  `defaultlower` varchar(20),
  `datatype` varchar(12),
  
/*  `uploaded` DATE DEFAULT CURRENT_DATE,*/
  
  PRIMARY KEY (`CUI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



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

DROP TABLE IF EXISTS `models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `models` (

  `id` int(16) NOT NULL AUTO_INCREMENT, /*id category*/
  `DOI` varchar(255)  COLLATE utf8_unicode_ci NOT NULL,
  `papertitle` varchar(255) NOT NULL,
  `modeltitle` varchar(255) NOT NULL,
  `yearofpub` varchar(5),
  `authors` TEXT,

  `must` TEXT, /*population category*/
  `mustnot` TEXT,
  `mustCUI` TEXT,
  `mustnotCUI` TEXT,

  `inpname` TEXT, /*input category*/
  `inpdesc` TEXT,
  `inpCUI` TEXT,
  `inpunits` TEXT,
  `inpdatatype` TEXT,
  `upper` TEXT,
  `lower` TEXT,
  
  `output` varchar(255), /*output category*/
  `outcome` varchar(255),
  `outcometime` varchar(3),
  `outputCUI` varchar(255),
  `outcomeCUI` varchar(255),
  
  `filename` TEXT, /*data category*/
  `filepointer` TEXT,
  `datumname` TEXT,
  `datum` TEXT,
  
  `language` varchar(12), /*model category*/
  `uncompiled` TEXT,
  `compiled` TEXT,
  `dependList` varchar(255),
  `example` TEXT,
  
  `model_category` varchar(255), /*other categories: model_category and predictive ability*/
  `type` varchar(255), 
  `metric` varchar(255), 
  `value` varchar(255), 
  `lcl` varchar(255), 
  `ucl` varchar(255), 
  
  `modified` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
/*  `uploaded` DATE DEFAULT CURRENT_DATE,*/
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `models` 



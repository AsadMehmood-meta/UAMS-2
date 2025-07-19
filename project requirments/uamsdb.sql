-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: uamsdb
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `budgetrule`
--

DROP TABLE IF EXISTS `budgetrule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `budgetrule` (
  `budgetrule_id` int NOT NULL AUTO_INCREMENT,
  `user_email` varchar(100) DEFAULT NULL,
  `project_category` varchar(100) DEFAULT NULL,
  `hourly_rate_threshold` decimal(10,2) DEFAULT NULL,
  `profit_margin_threshold` decimal(5,2) DEFAULT NULL,
  `client_tier` enum('New','Returning','Premium') DEFAULT NULL,
  `budget_type` enum('Hourly','Fixed') DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`budgetrule_id`),
  KEY `user_email` (`user_email`),
  CONSTRAINT `budgetrule_ibfk_1` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budgetrule`
--

LOCK TABLES `budgetrule` WRITE;
/*!40000 ALTER TABLE `budgetrule` DISABLE KEYS */;
INSERT INTO `budgetrule` VALUES (1,'asad.mehmood@example.com','Web Development',20.00,35.00,'New','Hourly',1,'2025-07-01 10:00:00'),(2,'asad.mehmood@example.com','UI/UX Design',18.00,30.00,'Returning','Fixed',1,'2025-07-02 11:30:00'),(3,'usman.farooq@example.com','Data Analysis',22.00,28.00,'Premium','Hourly',1,'2025-07-03 12:45:00'),(4,'asad.mehmood@example.com','DevOps',25.00,40.00,'New','Hourly',1,'2025-07-04 14:15:00'),(5,'usman.farooq@example.com','Mobile App Development',24.00,33.00,'Returning','Fixed',1,'2025-07-05 09:50:00');
/*!40000 ALTER TABLE `budgetrule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dailyreport`
--

DROP TABLE IF EXISTS `dailyreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dailyreport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `user_email` varchar(100) DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `report_date` date DEFAULT NULL,
  `pending_tasks` int DEFAULT NULL,
  `completed_tasks` int DEFAULT NULL,
  `task_progress` decimal(5,2) DEFAULT NULL,
  `project_progress` decimal(5,2) DEFAULT NULL,
  `task_deadline` date DEFAULT NULL,
  `project_deadline` date DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`report_id`),
  KEY `user_email` (`user_email`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `dailyreport_ibfk_1` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`) ON DELETE CASCADE,
  CONSTRAINT `dailyreport_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dailyreport`
--

LOCK TABLES `dailyreport` WRITE;
/*!40000 ALTER TABLE `dailyreport` DISABLE KEYS */;
INSERT INTO `dailyreport` VALUES (1,'asad.mehmood@example.com',1,'2025-07-09',3,2,65.00,55.00,'2025-07-11','2025-07-20','2025-07-09 08:30:00'),(2,'asad.mehmood@example.com',2,'2025-07-09',2,1,72.00,40.00,'2025-07-13','2025-07-22','2025-07-09 08:30:00'),(3,'usman.farooq@example.com',3,'2025-07-09',4,3,50.00,38.00,'2025-07-12','2025-07-25','2025-07-09 08:30:00'),(4,'asad.mehmood@example.com',4,'2025-07-09',1,2,85.00,78.00,'2025-07-10','2025-07-18','2025-07-09 08:30:00'),(5,'usman.farooq@example.com',5,'2025-07-09',2,0,48.00,25.00,'2025-07-15','2025-07-27','2025-07-09 08:30:00');
/*!40000 ALTER TABLE `dailyreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(150) NOT NULL,
  `description` text,
  `category` varchar(100) DEFAULT NULL,
  `skill_required` varchar(255) DEFAULT NULL,
  `connects_required` int DEFAULT NULL,
  `date_posted` date DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `client_rating` decimal(2,1) DEFAULT NULL,
  `budget_type` enum('Fixed','Hourly') DEFAULT NULL,
  `client_budget` decimal(10,2) DEFAULT NULL,
  `expected_cost` decimal(10,2) DEFAULT NULL,
  `expected_earning` decimal(10,2) DEFAULT NULL,
  `feasibility_score` tinyint DEFAULT NULL,
  `url_link` text,
  `client_country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  CONSTRAINT `job_chk_1` CHECK ((`feasibility_score` between 0 and 10))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (1,'React Developer Needed','Build responsive UI using React for SaaS app.','Web Development','React, HTML, CSS, JavaScript',6,'2025-07-01','2025-07-10',4.9,'Hourly',20.00,15.00,200.00,9,'https://www.upwork.com/job/react-dev-1','Pakistan'),(2,'SEO Optimization for E-commerce','Improve SEO for Shopify store.','Marketing','SEO, Google Analytics',4,'2025-07-05','2025-07-15',4.6,'Fixed',300.00,200.00,100.00,7,'https://www.upwork.com/job/seo-shopify-usa','United States'),(3,'Automation Script in Python','Need script for data cleaning and PDF extraction.','Programming','Python, Pandas',8,'2025-07-04','2025-07-12',5.0,'Fixed',150.00,120.00,30.00,6,'https://www.upwork.com/job/python-cleaning-uk','United Kingdom'),(4,'Figma UI/UX Design','Create a design prototype for mobile app.','Design','Figma, UI/UX Design',5,'2025-07-06','2025-07-16',4.2,'Hourly',25.00,18.00,150.00,8,'https://www.upwork.com/job/figma-design-canada','Canada'),(5,'Setup CI/CD Pipeline','DevOps expert needed for GitHub Actions setup.','Infrastructure','DevOps, Docker, GitHub Actions',10,'2025-07-02','2025-07-20',4.8,'Fixed',500.00,300.00,200.00,10,'https://www.upwork.com/job/devops-germany','Germany'),(6,'Fix WordPress Plugin Bug','Issue with form plugin in WordPress site.','CMS Development','WordPress, PHP',2,'2025-07-07','2025-07-09',4.3,'Fixed',80.00,60.00,20.00,5,'https://www.upwork.com/job/wp-bug-india','India'),(7,'Need Logo Design for Startup','Creative logo required with 3 concepts.','Graphic Design','Adobe Photoshop, Illustrator',3,'2025-07-03','2025-07-11',4.5,'Fixed',100.00,70.00,30.00,6,'https://www.upwork.com/job/logo-aus','Australia'),(8,'SQL Expert for Report Automation','Automate Excel reports using SQL queries.','Database','SQL, Excel, PowerBI',6,'2025-07-01','2025-07-10',4.7,'Hourly',18.00,12.00,120.00,7,'https://www.upwork.com/job/sql-uae','United Arab Emirates'),(9,'Sample Job Title',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Pakistan');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `project_id` int NOT NULL AUTO_INCREMENT,
  `project_title` varchar(150) NOT NULL,
  `description` text,
  `status` enum('Not Started','In Progress','On Hold','Completed','Cancelled') DEFAULT 'Not Started',
  `start_date` date DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `completion_date` date DEFAULT NULL,
  `progress` tinyint DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `manager_email` varchar(150) DEFAULT NULL,
  `proposal_id` int DEFAULT NULL,
  `job_id` int DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `manager_email` (`manager_email`),
  KEY `proposal_id` (`proposal_id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `project_ibfk_1` FOREIGN KEY (`manager_email`) REFERENCES `user` (`email`) ON DELETE SET NULL,
  CONSTRAINT `project_ibfk_2` FOREIGN KEY (`proposal_id`) REFERENCES `proposal` (`proposal_id`) ON DELETE SET NULL,
  CONSTRAINT `project_ibfk_3` FOREIGN KEY (`job_id`) REFERENCES `job` (`job_id`) ON DELETE SET NULL,
  CONSTRAINT `project_chk_1` CHECK ((`progress` between 0 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'React SaaS Dashboard','Frontend UI for a SaaS dashboard using React.','In Progress','2025-07-01','2025-07-15',NULL,60,'2025-07-13 02:29:00','ayesha.khan@example.com',1,1),(2,'Shopify SEO Boost','Full SEO optimization for a Shopify store.','Not Started',NULL,'2025-07-20',NULL,0,'2025-07-13 02:29:00','bilal.ahmed@example.com',2,2),(3,'Python Automation Script','Data cleaning and PDF parsing script in Python.','Completed','2025-07-01','2025-07-10','2025-07-09',100,'2025-07-13 02:29:00','usman.farooq@example.com',3,3),(4,'Mobile App UI/UX Design','Figma design for mobile productivity app.','In Progress','2025-07-04','2025-07-18',NULL,40,'2025-07-13 02:29:00','rabia.kaleem@example.com',4,4),(5,'CI/CD DevOps Setup','Pipeline setup using Docker and GitHub Actions.','Completed','2025-07-01','2025-07-15','2025-07-14',100,'2025-07-13 02:29:00','asad.mehmood@example.com',5,5);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proposal`
--

DROP TABLE IF EXISTS `proposal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proposal` (
  `proposal_id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `user_email` varchar(150) DEFAULT NULL,
  `content` text,
  `connects_required` int DEFAULT NULL,
  `submitted_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` enum('Draft','Submitted','Accepted','Rejected') DEFAULT 'Draft',
  PRIMARY KEY (`proposal_id`),
  KEY `job_id` (`job_id`),
  KEY `user_email` (`user_email`),
  CONSTRAINT `proposal_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job` (`job_id`) ON DELETE CASCADE,
  CONSTRAINT `proposal_ibfk_2` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proposal`
--

LOCK TABLES `proposal` WRITE;
/*!40000 ALTER TABLE `proposal` DISABLE KEYS */;
INSERT INTO `proposal` VALUES (1,1,'asad.mehmood@example.com','I have 5+ years of experience with React and can start immediately.',6,'2025-07-13 02:21:23','Submitted'),(2,2,'ayesha.khan@example.com','SEO strategy will be based on data-driven keywords and on-page optimization.',4,'2025-07-13 02:21:23','Draft'),(3,3,'zain.ali@example.com','Python script will be efficient, documented, and delivered in 2 days.',8,'2025-07-13 02:21:23','Submitted'),(4,4,'hira.iqbal@example.com','Experienced UI/UX designer with strong Figma skills and mobile-first approach.',5,'2025-07-13 02:21:23','Draft'),(5,5,'bilal.ahmed@example.com','Set up a CI/CD pipeline using Docker and GitHub Actions within a week.',10,'2025-07-13 02:21:23','Submitted'),(6,6,'fatima.rashid@example.com','I can fix the plugin bug and optimize performance in under 4 hours.',2,'2025-07-13 02:21:23','Submitted'),(7,7,'saad.nawaz@example.com','Logo design will include 3 modern concepts + unlimited revisions.',3,'2025-07-13 02:21:23','Draft'),(8,8,'usman.farooq@example.com','Can automate your SQL reports and provide PowerBI integration.',6,'2025-07-13 02:21:23','Submitted');
/*!40000 ALTER TABLE `proposal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `skill_id` int NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`skill_id`),
  UNIQUE KEY `skill_name` (`skill_name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,'Python','Programming','General-purpose programming language, used in data science and web development.'),(2,'JavaScript','Programming','Frontend and backend scripting language, core to web development.'),(3,'React','Frontend Framework','JavaScript library for building user interfaces.'),(4,'Node.js','Backend','JavaScript runtime for server-side development.'),(5,'HTML & CSS','Frontend','Markup and styling languages for building web pages.'),(6,'SQL','Database','Structured Query Language used for relational databases.'),(7,'MongoDB','Database','NoSQL database used for modern applications.'),(8,'UI/UX Design','Design','Design of user interfaces and experiences.'),(9,'WordPress','CMS','Content management system for websites and blogs.'),(10,'SEO','Marketing','Search Engine Optimization to improve site ranking.'),(11,'Adobe Photoshop','Design','Image editing and graphics design tool.'),(12,'Figma','Design','Collaborative interface design tool.'),(13,'DevOps','Infrastructure','CI/CD, server deployment, and automation practices.'),(14,'Project Management','Management','Managing timelines, tasks, and teams.'),(15,'Google Ads','Marketing','Google ad campaign and PPC advertising.');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `task_id` int NOT NULL AUTO_INCREMENT,
  `task_title` varchar(150) NOT NULL,
  `description` text,
  `comment` text,
  `created_by_email` varchar(150) DEFAULT NULL,
  `priority` enum('Low','Medium','High','Critical') DEFAULT 'Medium',
  `status` enum('To Do','In Progress','Review','Completed','Blocked') DEFAULT 'To Do',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `start_date` date DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `progress` tinyint DEFAULT '0',
  `completed_date` date DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`task_id`),
  KEY `created_by_email` (`created_by_email`),
  KEY `project_id` (`project_id`),
  KEY `fk_user_task` (`user_id`),
  CONSTRAINT `fk_user_task` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE SET NULL,
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`created_by_email`) REFERENCES `user` (`email`) ON DELETE SET NULL,
  CONSTRAINT `task_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE,
  CONSTRAINT `task_chk_1` CHECK ((`progress` between 0 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,'Setup Project Repo','Initialize GitHub repository and README.',NULL,'ayesha.khan@example.com','Low','Completed','2025-07-01 00:00:00','2025-07-01','2025-07-02',100,'2025-07-02',1,NULL),(2,'Build React Components','Develop reusable UI elements.',NULL,'ayesha.khan@example.com','High','In Progress','2025-07-02 00:00:00','2025-07-03','2025-07-10',70,NULL,1,NULL),(3,'Run SEO Audit','Check website for SEO issues.',NULL,'bilal.ahmed@example.com','Medium','Completed','2025-07-03 00:00:00','2025-07-04','2025-07-06',100,'2025-07-06',2,NULL),(4,'Keyword Research','Find high-performing keywords.',NULL,'bilal.ahmed@example.com','High','In Progress','2025-07-05 00:00:00','2025-07-06','2025-07-10',60,NULL,2,NULL),(6,'Clean Raw Excel','Write function to normalize data.',NULL,'usman.farooq@example.com','High','Completed','2025-07-01 00:00:00','2025-07-01','2025-07-02',100,'2025-07-02',3,NULL),(7,'Extract PDF Tables','Parse tables from scanned PDFs.',NULL,'usman.farooq@example.com','Critical','Completed','2025-07-02 00:00:00','2025-07-02','2025-07-03',100,'2025-07-03',3,NULL),(10,'User Research','Survey competitors and user pain points.',NULL,'rabia.kaleem@example.com','High','Completed','2025-07-01 00:00:00','2025-07-02','2025-07-03',100,'2025-07-03',4,NULL),(11,'Sketch Wireframes','Draw low-fidelity screens.',NULL,'rabia.kaleem@example.com','Medium','In Progress','2025-07-04 00:00:00','2025-07-05','2025-07-08',40,NULL,4,NULL),(12,'Design UI Screens','Create high-fidelity Figma screens.',NULL,'rabia.kaleem@example.com','Critical','To Do','2025-07-05 00:00:00',NULL,'2025-07-10',0,NULL,4,NULL),(14,'Client Review Meeting','Present prototype to client.',NULL,'rabia.kaleem@example.com','High','To Do','2025-07-07 00:00:00',NULL,'2025-07-12',0,NULL,4,NULL),(15,'Server Setup','Provision Ubuntu server for deployment.',NULL,'asad.mehmood@example.com','High','Completed','2025-07-01 00:00:00','2025-07-02','2025-07-03',100,'2025-07-03',5,NULL),(16,'Install Docker','Set up Docker and containers.',NULL,'asad.mehmood@example.com','High','Completed','2025-07-02 00:00:00','2025-07-03','2025-07-04',100,'2025-07-04',5,NULL),(17,'Write Dockerfile','Create Dockerfile for CI build.',NULL,'asad.mehmood@example.com','Medium','Completed','2025-07-03 00:00:00','2025-07-04','2025-07-05',100,'2025-07-05',5,NULL),(18,'GitHub Actions Setup','Configure CI/CD workflow.',NULL,'asad.mehmood@example.com','Critical','Completed','2025-07-04 00:00:00','2025-07-05','2025-07-06',100,'2025-07-06',5,NULL),(19,'Test Deployment','Deploy to staging and test.',NULL,'asad.mehmood@example.com','High','Completed','2025-07-05 00:00:00','2025-07-06','2025-07-07',100,'2025-07-07',5,NULL),(20,'Monitoring Setup','Add monitoring with Prometheus.',NULL,'asad.mehmood@example.com','Medium','In Progress','2025-07-06 00:00:00','2025-07-07','2025-07-10',40,NULL,5,NULL),(21,'Client Handover','Document system and handover.',NULL,'asad.mehmood@example.com','High','To Do','2025-07-07 00:00:00',NULL,'2025-07-11',0,NULL,5,NULL),(39,'hgfd','jhgfd','jjgfd',NULL,'Low','To Do','2025-07-16 18:16:01',NULL,'2025-07-17',0,NULL,3,7);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `contact` varchar(20) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `role` enum('Admin','Manager','Member') NOT NULL,
  `password` varchar(255) NOT NULL,
  `connect_balance` int DEFAULT '0',
  `hourly_rate` decimal(6,2) DEFAULT '0.00',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Asad','Mehmood','03011234567','asad.mehmood@example.com','Admin','admin123',120,30.00,'2025-07-13 02:03:54'),(2,'Ayesha','Khan','03121234567','ayesha.khan@example.com','Manager','ayesha456',90,22.00,'2025-07-13 02:03:54'),(3,'Zain','Ali','03211234567','zain.ali@example.com','Member','zainpass',60,18.50,'2025-07-13 02:03:54'),(4,'Hira','Iqbal','03451234567','hira.iqbal@example.com','Member','hira@321',75,20.00,'2025-07-13 02:03:54'),(5,'Bilal','Ahmed','03081234567','bilal.ahmed@example.com','Manager','bilal789',110,25.00,'2025-07-13 02:03:54'),(6,'Fatima','Rashid','03151234567','fatima.rashid@example.com','Member','fatimaPass',95,19.00,'2025-07-13 02:03:54'),(7,'Saad','Nawaz','03241234567','saad.nawaz@example.com','Member','saad007',45,15.00,'2025-07-13 02:03:54'),(8,'Iqra','Zafar','03031234567','iqra.zafar@example.com','Member','iqra#pass',105,21.00,'2025-07-13 02:03:54'),(9,'Usman','Farooq','03421234567','usman.farooq@example.com','Admin','usman123',130,35.00,'2025-07-13 02:03:54'),(10,'Rabia','Kaleem','03191234567','rabia.kaleem@example.com','Manager','rabia321',88,23.50,'2025-07-13 02:03:54');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userskill`
--

DROP TABLE IF EXISTS `userskill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userskill` (
  `user_id` int NOT NULL,
  `skill_id` int NOT NULL,
  `proficiency_level` enum('Beginner','Intermediate','Expert') DEFAULT 'Intermediate',
  `years_of_experience` int DEFAULT '0',
  `certified` tinyint(1) DEFAULT '0',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`skill_id`),
  KEY `skill_id` (`skill_id`),
  CONSTRAINT `userskill_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `userskill_ibfk_2` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`skill_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userskill`
--

LOCK TABLES `userskill` WRITE;
/*!40000 ALTER TABLE `userskill` DISABLE KEYS */;
INSERT INTO `userskill` VALUES (1,1,'Expert',5,1,'2025-07-13 02:08:33'),(1,2,'Intermediate',3,0,'2025-07-13 02:08:33'),(2,1,'Intermediate',2,0,'2025-07-13 02:08:33'),(2,3,'Expert',4,1,'2025-07-13 02:08:33'),(3,2,'Intermediate',3,0,'2025-07-13 02:08:33'),(3,4,'Expert',5,1,'2025-07-13 02:08:33'),(4,1,'Intermediate',2,1,'2025-07-13 02:08:33'),(4,5,'Beginner',1,0,'2025-07-13 02:08:33'),(5,2,'Intermediate',2,0,'2025-07-13 02:08:33'),(5,6,'Expert',6,1,'2025-07-13 02:08:33'),(6,3,'Beginner',1,0,'2025-07-13 02:08:33'),(6,7,'Intermediate',2,0,'2025-07-13 02:08:33'),(7,1,'Intermediate',3,1,'2025-07-13 02:08:33'),(7,8,'Expert',5,1,'2025-07-13 02:08:33'),(8,2,'Beginner',1,0,'2025-07-13 02:08:33'),(8,4,'Intermediate',2,0,'2025-07-13 02:08:33'),(9,5,'Expert',4,1,'2025-07-13 02:08:33'),(9,6,'Intermediate',3,0,'2025-07-13 02:08:33'),(10,3,'Intermediate',2,0,'2025-07-13 02:08:33'),(10,7,'Expert',5,1,'2025-07-13 02:08:33');
/*!40000 ALTER TABLE `userskill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'uamsdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-17 18:53:24

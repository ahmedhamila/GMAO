-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 01, 2022 at 10:25 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gmao_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `agent_maintenance`
--

CREATE TABLE `agent_maintenance` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL,
  `Specialite` varchar(50) NOT NULL,
  `Age` int(11) NOT NULL,
  `Sexe` enum('Homme','Femme','','') NOT NULL,
  `NiveauEducation` varchar(50) NOT NULL,
  `ExperienceProfessionnelle` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agent_maintenance`
--

INSERT INTO `agent_maintenance` (`Matricule`, `Nom`, `Prenom`, `Specialite`, `Age`, `Sexe`, `NiveauEducation`, `ExperienceProfessionnelle`) VALUES
('AAA00009', 'Touhemi', 'Jibli', 'Chaudiere', 32, 'Homme', '2', 7);

-- --------------------------------------------------------

--
-- Table structure for table `bon_approvisionnement`
--

CREATE TABLE `bon_approvisionnement` (
  `Id` varchar(25) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `Matricule_M` varchar(50) NOT NULL,
  `DateLiberation` date NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bon_travail`
--

CREATE TABLE `bon_travail` (
  `Id` int(25) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `Matricule_AM` varchar(50) NOT NULL,
  `Description` text NOT NULL,
  `Section` varchar(25) NOT NULL,
  `DateLiberation` datetime NOT NULL,
  `type` enum('Curatif','Preventif') NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL,
  `RefDIM` varchar(50) NOT NULL,
  `Frequence` varchar(50) DEFAULT NULL,
  `Active` tinyint(1) NOT NULL DEFAULT 0,
  `Status` enum('Traitee','NonTraitee') NOT NULL DEFAULT 'NonTraitee'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bon_travail`
--

INSERT INTO `bon_travail` (`Id`, `Matricule_RM`, `Matricule_AM`, `Description`, `Section`, `DateLiberation`, `type`, `CodeEquipement`, `RefDIM`, `Frequence`, `Active`, `Status`) VALUES
(5, 'AAA00001', 'AAA00009', 'TSTSTSTSTTSTSTS', 'CCC1', '2022-07-26 00:00:00', 'Curatif', 'EEE00001', '1', '', 0, 'NonTraitee'),
(6, 'AAA00001', 'AAA00009', 'a:kjfnakfkanf\nakfjbkafbkabfka', 'CCC1', '2022-07-26 00:00:00', 'Curatif', 'EEE00002', '2', NULL, 0, 'NonTraitee'),
(15, 'AAA00001', 'AAA00009', 'ezsrdtfyughinjlk,af65', 'CCC1', '2022-07-27 00:00:00', 'Curatif', 'EEE00001', '8', 'NULL', 0, 'NonTraitee'),
(16, 'AAA00001', 'AAA00009', 'oooh!', 'CCC1', '2022-07-27 00:00:00', 'Preventif', 'EEE00002', '', '112', 0, 'NonTraitee'),
(17, 'AAA00001', 'AAA00009', 'aeaeazeazeazea', 'CCC1', '2022-08-16 19:53:17', 'Curatif', 'EEE00002', '121212', 'NULL', 0, 'NonTraitee'),
(18, 'AAA00001', 'AAA00009', '111111111111111111111', 'CCC1', '2022-08-16 21:02:01', 'Curatif', 'EEE00001', '22222', 'NULL', 0, 'NonTraitee'),
(19, 'AAA00001', 'AAA00009', 'adadadad', 'CCC1', '2022-08-24 13:39:53', 'Curatif', 'EEE00001', '1', 'NULL', 0, 'NonTraitee'),
(28, 'AAA00001', 'AAA00009', '555555555555555', 'CCC1', '2022-08-24 13:56:46', 'Preventif', 'EEE00001', '', '5', 1, 'NonTraitee'),
(30, 'AAA00001', 'AAA00009', 'TestTestTestTestTestTestTestTestTestTestTest2', 'CCC1', '2022-09-14 14:55:49', 'Preventif', 'EEE00002', 'None', '100', 1, 'NonTraitee'),
(31, 'AAA00001', 'AAA00009', 'TESTETSTSTTSTSTS', 'CCC1', '2022-09-14 15:04:37', 'Curatif', 'EEE00001', '11', 'NULL', 0, 'NonTraitee');

-- --------------------------------------------------------

--
-- Table structure for table `chaine_equipement`
--

CREATE TABLE `chaine_equipement` (
  `RefChaine` varchar(50) NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chaine_production`
--

CREATE TABLE `chaine_production` (
  `RefChaine` varchar(50) NOT NULL,
  `NbEquipement` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chaine_production`
--

INSERT INTO `chaine_production` (`RefChaine`, `NbEquipement`) VALUES
('CCC1', 50);

-- --------------------------------------------------------

--
-- Table structure for table `demande_intervention`
--

CREATE TABLE `demande_intervention` (
  `Id` int(11) NOT NULL,
  `Matricule_RCP` varchar(25) NOT NULL,
  `Matricule_RM` varchar(25) NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL,
  `Section` varchar(25) NOT NULL,
  `DateLiberation` datetime NOT NULL,
  `Motif` enum('ArretComplet','AnomaliePouvantEntrainerunePanne') NOT NULL,
  `Description` text NOT NULL,
  `Status` enum('Traitee','NonTraitee') NOT NULL DEFAULT 'NonTraitee'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `demande_intervention`
--

INSERT INTO `demande_intervention` (`Id`, `Matricule_RCP`, `Matricule_RM`, `CodeEquipement`, `Section`, `DateLiberation`, `Motif`, `Description`, `Status`) VALUES
(1, 'AAA00003', 'AAA00001', 'EEE00001', 'T', '2022-08-16 20:38:34', 'ArretComplet', '1111111111111111111', 'Traitee'),
(2, 'AAA00003', 'AAA00001', 'EEE00001', 'T', '2022-08-16 20:38:34', 'ArretComplet', '1111111111111111111', 'Traitee'),
(3, 'AAA00003', 'AAA00001', 'EEE00003', 'T', '2022-08-16 21:17:03', 'AnomaliePouvantEntrainerunePanne', '11111111111111111111111111111', 'Traitee'),
(5, 'AAA00003', 'AAA00001', 'EEE00002', 'T', '2022-08-16 21:23:20', 'ArretComplet', '11111111111111111', 'Traitee'),
(6, 'AAA00003', 'AAA00001', 'EEE00001', '1111', '2022-08-24 12:14:24', 'ArretComplet', '11111111111111111111111', 'Traitee'),
(7, 'AAA00003', 'AAA00001', 'EEE00003', '8', '2022-08-24 12:16:08', 'ArretComplet', '88888888888888888888', 'Traitee'),
(8, 'AAA00003', 'AAA00001', 'EEE00003', 'l', '2022-08-24 12:18:47', 'ArretComplet', 'llllllllllllllllllllllllllll', 'Traitee'),
(9, 'AAA00003', 'AAA00001', 'EEE00003', 'p', '2022-08-24 12:20:01', 'ArretComplet', 'ppppppppppppppppppppppp', 'Traitee'),
(10, 'AAA00003', 'AAA00001', 'EEE00001', 'ddd', '2022-08-24 12:30:54', 'ArretComplet', 'dddddddddddddddddddddddddddddd', 'Traitee'),
(11, 'AAA00003', 'AAA00001', 'EEE00003', '', '2022-09-02 14:44:37', 'AnomaliePouvantEntrainerunePanne', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Traitee'),
(12, 'AAA00003', 'AAA00001', 'EEE00001', 'h', '2022-09-10 11:26:09', 'ArretComplet', 'ngfcngch,gv,jjhv,hv', 'NonTraitee');

--
-- Triggers `demande_intervention`
--
DELIMITER $$
CREATE TRIGGER `Demande_Intervention_TRG` AFTER INSERT ON `demande_intervention` FOR EACH ROW BEGIN
insert into notification(Emetteur,Recepteur,DateTime,Type) VALUES(NEW.Matricule_RCP,NEW.Matricule_RM,NEW.DateLiberation,"DemandeIntervention");
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `equipement`
--

CREATE TABLE `equipement` (
  `Code` varchar(25) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `DateFabriquation` date NOT NULL,
  `DateMiseEnMarche` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `equipement`
--

INSERT INTO `equipement` (`Code`, `Nom`, `Type`, `DateFabriquation`, `DateMiseEnMarche`) VALUES
('EEE00001', 'Chaudiere', 'ahbd', '2013-07-03', '2020-07-29'),
('EEE00002', 'piece2', 'ajkhfb', '2013-07-10', '2020-07-15'),
('EEE00003', 'piece3', 'afafkjaf', '2012-07-11', '2020-07-15');

-- --------------------------------------------------------

--
-- Table structure for table `magasinier`
--

CREATE TABLE `magasinier` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id` int(11) NOT NULL,
  `Emetteur` varchar(25) NOT NULL,
  `Recepteur` varchar(25) NOT NULL,
  `DateTime` datetime NOT NULL,
  `Type` enum('DemandeIntervention','BonTravail','BonApprovisionnement') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`id`, `Emetteur`, `Recepteur`, `DateTime`, `Type`) VALUES
(1, 'AAA00003', 'AAA00001', '2022-08-16 21:23:20', 'DemandeIntervention'),
(2, 'AAA00003', 'AAA00001', '2022-08-24 12:14:24', 'DemandeIntervention'),
(3, 'AAA00003', 'AAA00001', '2022-08-24 12:16:08', 'DemandeIntervention'),
(4, 'AAA00003', 'AAA00001', '2022-08-24 12:18:47', 'DemandeIntervention'),
(5, 'AAA00003', 'AAA00001', '2022-08-24 12:20:01', 'DemandeIntervention'),
(6, 'AAA00003', 'AAA00001', '2022-08-24 12:30:54', 'DemandeIntervention'),
(7, 'AAA00003', 'AAA00001', '2022-09-02 14:44:37', 'DemandeIntervention'),
(8, 'AAA00003', 'AAA00001', '2022-09-10 11:26:09', 'DemandeIntervention');

-- --------------------------------------------------------

--
-- Table structure for table `piece_rechange`
--

CREATE TABLE `piece_rechange` (
  `Code` varchar(25) NOT NULL,
  `Nom` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `piece_rechange_bon_approvisionnement`
--

CREATE TABLE `piece_rechange_bon_approvisionnement` (
  `Id` int(11) NOT NULL,
  `Code_Piece` varchar(25) NOT NULL,
  `Id_bon` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `responsable_chaine_production`
--

CREATE TABLE `responsable_chaine_production` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL,
  `RefChaine` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `responsable_chaine_production`
--

INSERT INTO `responsable_chaine_production` (`Matricule`, `Nom`, `Prenom`, `RefChaine`) VALUES
('AAA00003', 'Touhemi', 'boubaker', 'CCC1');

-- --------------------------------------------------------

--
-- Table structure for table `responsable_maintenance`
--

CREATE TABLE `responsable_maintenance` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL,
  `RefChaine` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `responsable_maintenance`
--

INSERT INTO `responsable_maintenance` (`Matricule`, `Nom`, `Prenom`, `RefChaine`) VALUES
('AAA00001', 'Hamila', 'Ahmed', '1'),
('AAA00005', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `responsable_production`
--

CREATE TABLE `responsable_production` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Matricule` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Role` enum('ResponsableProduction','ResponsableChaineProduction','ResponsableMaintenance','AgentMaintenance','Administrateur','Magasinier') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Matricule`, `Password`, `Role`) VALUES
('AAA00001', 'Hamila', 'ResponsableMaintenance'),
('AAA00002', 'Hajri', 'Administrateur'),
('AAA00003', 'Gaston', 'ResponsableChaineProduction'),
('AAA00005', 'azerty', 'ResponsableProduction');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agent_maintenance`
--
ALTER TABLE `agent_maintenance`
  ADD PRIMARY KEY (`Matricule`);

--
-- Indexes for table `bon_approvisionnement`
--
ALTER TABLE `bon_approvisionnement`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_BA_1` (`Matricule_RM`),
  ADD KEY `FK_BA_2` (`Matricule_M`);

--
-- Indexes for table `bon_travail`
--
ALTER TABLE `bon_travail`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_BT_1` (`Matricule_RM`),
  ADD KEY `FK_BT_2` (`Matricule_AM`),
  ADD KEY `FK_BT_3` (`CodeEquipement`);

--
-- Indexes for table `chaine_equipement`
--
ALTER TABLE `chaine_equipement`
  ADD KEY `FK_CE_1` (`CodeEquipement`),
  ADD KEY `FK_CE_2` (`RefChaine`);

--
-- Indexes for table `chaine_production`
--
ALTER TABLE `chaine_production`
  ADD PRIMARY KEY (`RefChaine`);

--
-- Indexes for table `demande_intervention`
--
ALTER TABLE `demande_intervention`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_DI_1` (`CodeEquipement`),
  ADD KEY `FK_DI_2` (`Matricule_RCP`),
  ADD KEY `FK_DI_3` (`Matricule_RM`);

--
-- Indexes for table `equipement`
--
ALTER TABLE `equipement`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `magasinier`
--
ALTER TABLE `magasinier`
  ADD PRIMARY KEY (`Matricule`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `piece_rechange`
--
ALTER TABLE `piece_rechange`
  ADD PRIMARY KEY (`Code`);

--
-- Indexes for table `piece_rechange_bon_approvisionnement`
--
ALTER TABLE `piece_rechange_bon_approvisionnement`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_PRBA_1` (`Code_Piece`),
  ADD KEY `FK_PRBA_2` (`Id_bon`);

--
-- Indexes for table `responsable_chaine_production`
--
ALTER TABLE `responsable_chaine_production`
  ADD PRIMARY KEY (`Matricule`),
  ADD KEY `FK_1` (`RefChaine`);

--
-- Indexes for table `responsable_maintenance`
--
ALTER TABLE `responsable_maintenance`
  ADD PRIMARY KEY (`Matricule`);

--
-- Indexes for table `responsable_production`
--
ALTER TABLE `responsable_production`
  ADD PRIMARY KEY (`Matricule`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Matricule`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bon_travail`
--
ALTER TABLE `bon_travail`
  MODIFY `Id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `demande_intervention`
--
ALTER TABLE `demande_intervention`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `piece_rechange_bon_approvisionnement`
--
ALTER TABLE `piece_rechange_bon_approvisionnement`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bon_approvisionnement`
--
ALTER TABLE `bon_approvisionnement`
  ADD CONSTRAINT `FK_BA_1` FOREIGN KEY (`Matricule_RM`) REFERENCES `responsable_maintenance` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BA_2` FOREIGN KEY (`Matricule_M`) REFERENCES `magasinier` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `bon_travail`
--
ALTER TABLE `bon_travail`
  ADD CONSTRAINT `FK_BT_1` FOREIGN KEY (`Matricule_RM`) REFERENCES `responsable_maintenance` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BT_2` FOREIGN KEY (`Matricule_AM`) REFERENCES `agent_maintenance` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BT_3` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `chaine_equipement`
--
ALTER TABLE `chaine_equipement`
  ADD CONSTRAINT `FK_CE_1` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CE_2` FOREIGN KEY (`RefChaine`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `demande_intervention`
--
ALTER TABLE `demande_intervention`
  ADD CONSTRAINT `FK_DI_1` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Code`),
  ADD CONSTRAINT `FK_DI_2` FOREIGN KEY (`Matricule_RCP`) REFERENCES `responsable_chaine_production` (`Matricule`),
  ADD CONSTRAINT `FK_DI_3` FOREIGN KEY (`Matricule_RM`) REFERENCES `responsable_maintenance` (`Matricule`);

--
-- Constraints for table `piece_rechange_bon_approvisionnement`
--
ALTER TABLE `piece_rechange_bon_approvisionnement`
  ADD CONSTRAINT `FK_PRBA_1` FOREIGN KEY (`Code_Piece`) REFERENCES `piece_rechange` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PRBA_2` FOREIGN KEY (`Id_bon`) REFERENCES `bon_approvisionnement` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `responsable_chaine_production`
--
ALTER TABLE `responsable_chaine_production`
  ADD CONSTRAINT `FK_1` FOREIGN KEY (`RefChaine`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

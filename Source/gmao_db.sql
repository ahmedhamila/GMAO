-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 26, 2022 at 01:44 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

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
  `Id` varchar(25) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `Matricule_AM` varchar(50) NOT NULL,
  `Description` text NOT NULL,
  `Section` varchar(25) NOT NULL,
  `DateLiberation` date NOT NULL,
  `type` enum('Correctif','Preventif') NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bon_travail`
--

INSERT INTO `bon_travail` (`Id`, `Matricule_RM`, `Matricule_AM`, `Description`, `Section`, `DateLiberation`, `type`, `CodeEquipement`) VALUES
('1', 'AAA00001', 'AAA00009', 'bon de test', '1', '2022-07-20', 'Correctif', 'EEE00001'),
('2', 'AAA00001', 'AAA00009', 'jhhjv test', '1', '2022-07-20', 'Correctif', 'EEE00001'),
('3', 'AAA00001', 'AAA00009', 'kjbf test', '1', '2022-07-20', 'Correctif', 'EEE00001');

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

-- --------------------------------------------------------

--
-- Table structure for table `demande_intervention`
--

CREATE TABLE `demande_intervention` (
  `Id` varchar(25) NOT NULL,
  `Matricule_RCP` varchar(50) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL,
  `Section` varchar(25) NOT NULL,
  `DateLiberation` date NOT NULL,
  `Motif` enum('ArretComplet','AnomaliePouvantEntrainerUnePanne','','') NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
('AAA00001', 'Hamila', 'Ahmed', '1');

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
  `Role` enum('ResponsableProduction','ResponsableChaineProduction','ResponsableMaintenance','AgentMaintenance','Administrateur') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Matricule`, `Password`, `Role`) VALUES
('AAA00001', 'Hamila', 'ResponsableMaintenance'),
('AAA00002', 'Hajri', 'Administrateur');

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
  ADD KEY `FK_DI_1` (`Matricule_RCP`),
  ADD KEY `FK_DI_2` (`Matricule_RM`),
  ADD KEY `FK_DI_3` (`CodeEquipement`);

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
  ADD CONSTRAINT `FK_DI_1` FOREIGN KEY (`Matricule_RCP`) REFERENCES `responsable_chaine_production` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DI_2` FOREIGN KEY (`Matricule_RM`) REFERENCES `responsable_maintenance` (`Matricule`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DI_3` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE;

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

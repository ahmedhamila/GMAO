-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2022 at 10:20 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

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
('AAA00001', 'Agent1', 'Maintenance1', 'Specialite1', 25, 'Homme', 'Bac', 5),
('AAA00002', 'Agent2', 'Maintenance2', 'Specialite2', 25, 'Femme', 'Bac', 5),
('AAA00003', 'Agent3', 'Maintenance3', 'Specialite3', 25, 'Femme', 'Bac', 7);

-- --------------------------------------------------------

--
-- Table structure for table `bon_approvisionnement`
--

CREATE TABLE `bon_approvisionnement` (
  `Id` int(11) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `Matricule_M` varchar(50) NOT NULL,
  `DateLiberation` date NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bon_approvisionnement`
--

INSERT INTO `bon_approvisionnement` (`Id`, `Matricule_RM`, `Matricule_M`, `DateLiberation`, `Description`) VALUES
(1, 'MMM00001', 'MG1', '2022-10-02', 'DescriptionBonApp1'),
(2, 'MMM00002', 'MG2', '2022-10-01', 'DescriptionBonApp2'),
(3, 'MMM00003', 'MG3', '2022-10-03', 'DescriptionBonApp3'),
(4, 'MMM00001', 'MG1', '2022-10-02', 'DescriptionBonApp1'),
(5, 'MMM00002', 'MG2', '2022-10-01', 'DescriptionBonApp2'),
(6, 'MMM00003', 'MG3', '2022-10-03', 'DescriptionBonApp3');

-- --------------------------------------------------------

--
-- Table structure for table `bon_travail`
--

CREATE TABLE `bon_travail` (
  `Id` int(25) NOT NULL,
  `Matricule_RM` varchar(50) NOT NULL,
  `Matricule_AM` varchar(50) NOT NULL,
  `Description` text NOT NULL,
  `Operation` int(11) NOT NULL,
  `Section` varchar(25) NOT NULL,
  `DateLiberation` datetime NOT NULL,
  `type` enum('Curatif','Preventif') NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL,
  `RefDIM` int(11) DEFAULT NULL,
  `Frequence` varchar(50) DEFAULT NULL,
  `Active` tinyint(1) NOT NULL DEFAULT 0,
  `Status` enum('Traitee','NonTraitee') NOT NULL DEFAULT 'NonTraitee'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bon_travail`
--

INSERT INTO `bon_travail` (`Id`, `Matricule_RM`, `Matricule_AM`, `Description`, `Operation`, `Section`, `DateLiberation`, `type`, `CodeEquipement`, `RefDIM`, `Frequence`, `Active`, `Status`) VALUES
(36, 'MMM00001', 'AAA00001', 'DescriptionBonTra1', 7, 'CCC00001', '2022-10-02 17:56:49', 'Preventif', 'EEE00001', NULL, '12', 1, 'NonTraitee'),
(37, 'MMM00002', 'AAA00002', 'DescriptionBonTra2', 7, 'CCC00002', '2022-10-02 17:57:17', 'Preventif', 'EEE00002', NULL, '12', 0, 'NonTraitee'),
(38, 'MMM00003', 'AAA00003', 'DescriptionBonTra3', 8, 'CCC00003', '2022-10-02 17:59:21', 'Curatif', 'EEE00003', 15, NULL, 0, 'NonTraitee'),
(41, 'MMM00001', 'AAA00003', 'DescTest', 9, 'CCC00001', '2022-10-02 18:31:27', 'Curatif', 'EEE00001', 13, 'NULL', 0, 'NonTraitee'),
(44, 'MMM00001', 'AAA00001', '5', 6, 'CCC00001', '2022-10-04 19:11:15', 'Curatif', 'EEE00001', 18, 'NULL', 0, 'NonTraitee'),
(45, 'MMM00001', 'AAA00001', '2', 10, 'CCC00001', '2022-10-04 19:15:07', 'Curatif', 'EEE00001', 19, 'NULL', 0, 'NonTraitee'),
(46, 'MMM00001', 'AAA00001', 'd', 6, 'CCC00001', '2022-10-04 19:20:36', 'Curatif', 'EEE00001', 20, 'NULL', 0, 'NonTraitee'),
(47, 'MMM00001', 'AAA00001', '111111111111111111111111', 6, 'CCC00001', '2022-10-04 19:22:52', 'Curatif', 'EEE00001', 21, 'NULL', 0, 'Traitee');

-- --------------------------------------------------------

--
-- Table structure for table `chaine_equipement`
--

CREATE TABLE `chaine_equipement` (
  `id` int(11) NOT NULL,
  `RefChaine` varchar(50) NOT NULL,
  `CodeEquipement` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chaine_equipement`
--

INSERT INTO `chaine_equipement` (`id`, `RefChaine`, `CodeEquipement`) VALUES
(1, 'CCC00001', 'EEE00001'),
(2, 'CCC00002', 'EEE00002'),
(3, 'CCC00003', 'EEE00003');

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
('CCC00001', 25),
('CCC00002', 20),
('CCC00003', 25);

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
  `Status` enum('Traitee','NonTraitee','EnCours') NOT NULL DEFAULT 'NonTraitee'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `demande_intervention`
--

INSERT INTO `demande_intervention` (`Id`, `Matricule_RCP`, `Matricule_RM`, `CodeEquipement`, `Section`, `DateLiberation`, `Motif`, `Description`, `Status`) VALUES
(13, 'HHH00001', 'MMM00001', 'EEE00001', 'CCC00001', '2022-10-02 17:58:28', 'ArretComplet', 'DescriptionDemandeInter1', 'Traitee'),
(14, 'HHH00002', 'MMM00002', 'EEE00002', 'CCC00002', '2022-10-02 17:58:28', 'ArretComplet', 'DescriptionDemandeInter3', 'NonTraitee'),
(15, 'HHH00003', 'MMM00003', 'EEE00003', 'CCC00003', '2022-10-02 17:58:28', 'AnomaliePouvantEntrainerunePanne', 'DescriptionDemandeInter3', 'NonTraitee'),
(17, 'HHH00001', 'MMM00001', 'EEE00001', 'CCC00001', '2022-10-04 19:02:05', 'ArretComplet', 'Test3', 'EnCours'),
(18, 'HHH00001', 'MMM00001', 'EEE00001', 'CCC00001', '2022-10-04 19:10:36', 'ArretComplet', '1', 'Traitee'),
(19, 'HHH00001', 'MMM00001', 'EEE00002', 'CCC00002', '2022-10-04 19:14:44', 'AnomaliePouvantEntrainerunePanne', 'lhbhjblb', 'Traitee'),
(20, 'HHH00001', 'MMM00001', 'EEE00001', 'CCC00001', '2022-10-04 19:20:23', 'ArretComplet', 'd', 'Traitee'),
(21, 'HHH00001', 'MMM00001', 'EEE00001', 'CCC00001', '2022-10-04 19:22:36', 'ArretComplet', '11111111111111', 'Traitee');

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
  `Reference` varchar(25) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `Role` varchar(50) NOT NULL,
  `Fabriquant` varchar(25) NOT NULL,
  `DateFabriquation` date NOT NULL,
  `DateMiseEnMarche` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `equipement`
--

INSERT INTO `equipement` (`Reference`, `designation`, `Role`, `Fabriquant`, `DateFabriquation`, `DateMiseEnMarche`) VALUES
('EEE00001', 'Equipement1', 'Role1', 'Fabriquant1', '2022-10-01', '2022-10-02'),
('EEE00002', 'Equipement2', 'Role2', 'Fabriquant2', '2022-10-01', '2022-10-02'),
('EEE00003', 'Equipement3', 'Role3', 'Fabriquant3', '2022-10-01', '2022-10-02');

-- --------------------------------------------------------

--
-- Table structure for table `equipe_piece`
--

CREATE TABLE `equipe_piece` (
  `id` int(11) NOT NULL,
  `Equipement` varchar(25) NOT NULL,
  `piece` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `equipe_piece`
--

INSERT INTO `equipe_piece` (`id`, `Equipement`, `piece`) VALUES
(1, 'EEE00001', 'PR1'),
(2, 'EEE00002', 'PR2'),
(3, 'EEE00003', 'PR3');

-- --------------------------------------------------------

--
-- Table structure for table `lubrification`
--

CREATE TABLE `lubrification` (
  `Reference` varchar(25) NOT NULL,
  `designation` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lubrification`
--

INSERT INTO `lubrification` (`Reference`, `designation`) VALUES
('Lub1', 'Lubrification1'),
('Lub2', 'Lubrification2'),
('Lub3', 'Lubrification3');

-- --------------------------------------------------------

--
-- Table structure for table `magasinier`
--

CREATE TABLE `magasinier` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `magasinier`
--

INSERT INTO `magasinier` (`Matricule`, `Nom`, `Prenom`) VALUES
('MG1', 'Magasinier1', 'moth1'),
('MG2', 'Magasinier2', 'moth2'),
('MG3', 'Magasinier3', 'moth3');

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
(8, 'AAA00003', 'AAA00001', '2022-09-10 11:26:09', 'DemandeIntervention'),
(9, 'HHH00001', 'MMM00001', '2022-10-02 17:58:28', 'DemandeIntervention'),
(10, 'HHH00002', 'MMM00002', '2022-10-02 17:58:28', 'DemandeIntervention'),
(11, 'HHH00003', 'MMM00003', '2022-10-02 17:58:28', 'DemandeIntervention'),
(12, 'HHH00001', 'MMM00003', '2022-10-04 19:02:05', 'DemandeIntervention'),
(13, 'HHH00001', 'MMM00001', '2022-10-04 19:10:36', 'DemandeIntervention'),
(14, 'HHH00001', 'MMM00001', '2022-10-04 19:14:44', 'DemandeIntervention'),
(15, 'HHH00001', 'MMM00001', '2022-10-04 19:20:23', 'DemandeIntervention'),
(16, 'HHH00001', 'MMM00001', '2022-10-04 19:22:36', 'DemandeIntervention');

-- --------------------------------------------------------

--
-- Table structure for table `operation`
--

CREATE TABLE `operation` (
  `id` int(11) NOT NULL,
  `titre` varchar(25) NOT NULL,
  `Mode` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `operation`
--

INSERT INTO `operation` (`id`, `titre`, `Mode`) VALUES
(6, 'Operation1', 'OperationDescription1'),
(7, 'Operation2', 'OperationDescription2'),
(8, 'Operation3', 'OperationDescription3'),
(9, 'OperationTest', 'OperationTestDesc'),
(10, 'OpTest2', 'OpTest2');

-- --------------------------------------------------------

--
-- Table structure for table `oper_lubri`
--

CREATE TABLE `oper_lubri` (
  `id` int(11) NOT NULL,
  `oper` int(11) NOT NULL,
  `lubri` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `oper_lubri`
--

INSERT INTO `oper_lubri` (`id`, `oper`, `lubri`) VALUES
(2, 6, 'Lub1'),
(3, 7, 'Lub2'),
(4, 8, 'Lub3'),
(5, 9, 'Lub1'),
(6, 10, 'Lub1');

-- --------------------------------------------------------

--
-- Table structure for table `oper_piece`
--

CREATE TABLE `oper_piece` (
  `id` int(11) NOT NULL,
  `oper` int(11) NOT NULL,
  `piece` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `oper_piece`
--

INSERT INTO `oper_piece` (`id`, `oper`, `piece`) VALUES
(2, 6, 'PR1'),
(3, 7, 'PR2'),
(4, 8, 'PR3'),
(5, 9, 'PR1'),
(6, 10, 'PR3');

-- --------------------------------------------------------

--
-- Table structure for table `piece_rechange`
--

CREATE TABLE `piece_rechange` (
  `Reference` varchar(25) NOT NULL,
  `Designation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `piece_rechange`
--

INSERT INTO `piece_rechange` (`Reference`, `Designation`) VALUES
('PR1', 'PieceRechange1'),
('PR2', 'PieceRechange2'),
('PR3', 'PieceRechange3');

-- --------------------------------------------------------

--
-- Table structure for table `piece_rechange_bon_approvisionnement`
--

CREATE TABLE `piece_rechange_bon_approvisionnement` (
  `Id` int(11) NOT NULL,
  `Code_Piece` varchar(25) NOT NULL,
  `Id_bon` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `piece_rechange_bon_approvisionnement`
--

INSERT INTO `piece_rechange_bon_approvisionnement` (`Id`, `Code_Piece`, `Id_bon`) VALUES
(1, 'PR1', 1),
(2, 'PR2', 2),
(3, 'PR3', 6);

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
('HHH00001', 'ResponsableC1', 'Chaine1', 'CCC00001'),
('HHH00002', 'ResponsableC2', 'Chaine2', 'CCC00002'),
('HHH00003', 'ResponsableC3', 'Chaine3', 'CCC00003');

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
('MMM00001', 'ResponsableM1', 'Maintenance1', 'CCC00001'),
('MMM00002', 'ResponsableM2', 'Maintenance2', 'CCC00002'),
('MMM00003', 'ResponsableM3', 'Maintenance3', 'CCC00003');

-- --------------------------------------------------------

--
-- Table structure for table `responsable_production`
--

CREATE TABLE `responsable_production` (
  `Matricule` varchar(50) NOT NULL,
  `Nom` varchar(25) NOT NULL,
  `Prenom` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `responsable_production`
--

INSERT INTO `responsable_production` (`Matricule`, `Nom`, `Prenom`) VALUES
('PPP00001', 'ResponsableP1', 'Production1'),
('PPP00002', 'ResponsableP2', 'Production2'),
('PPP00003', 'ResponsableP3', 'Production3');

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
('AAA00001', 'Maintenance1', 'AgentMaintenance'),
('Admin', 'Admin', 'Administrateur'),
('HHH00001', 'ResponsableC1', 'ResponsableChaineProduction'),
('MG1', 'Magasinier1', 'Magasinier'),
('MMM00001', 'ResponsableM1', 'ResponsableMaintenance'),
('PPP00001', 'ResponsableP1', 'ResponsableProduction');

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
  ADD KEY `FK_BT_3` (`CodeEquipement`),
  ADD KEY `FK_BT_4` (`RefDIM`),
  ADD KEY `FK_BT_5` (`Operation`),
  ADD KEY `FK_BT_6` (`Section`);

--
-- Indexes for table `chaine_equipement`
--
ALTER TABLE `chaine_equipement`
  ADD PRIMARY KEY (`id`),
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
  ADD KEY `FK_DI_3` (`Matricule_RM`),
  ADD KEY `FK_DI_4` (`Section`);

--
-- Indexes for table `equipement`
--
ALTER TABLE `equipement`
  ADD PRIMARY KEY (`Reference`);

--
-- Indexes for table `equipe_piece`
--
ALTER TABLE `equipe_piece`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Equipement` (`Equipement`),
  ADD KEY `piéce` (`piece`);

--
-- Indexes for table `lubrification`
--
ALTER TABLE `lubrification`
  ADD PRIMARY KEY (`Reference`);

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
-- Indexes for table `operation`
--
ALTER TABLE `operation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `oper_lubri`
--
ALTER TABLE `oper_lubri`
  ADD PRIMARY KEY (`id`),
  ADD KEY `oper` (`oper`),
  ADD KEY `lubri` (`lubri`);

--
-- Indexes for table `oper_piece`
--
ALTER TABLE `oper_piece`
  ADD PRIMARY KEY (`id`),
  ADD KEY `oper` (`oper`),
  ADD KEY `piece` (`piece`);

--
-- Indexes for table `piece_rechange`
--
ALTER TABLE `piece_rechange`
  ADD PRIMARY KEY (`Reference`);

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
  ADD PRIMARY KEY (`Matricule`),
  ADD KEY `FK_RM_1` (`RefChaine`);

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
-- AUTO_INCREMENT for table `bon_approvisionnement`
--
ALTER TABLE `bon_approvisionnement`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `bon_travail`
--
ALTER TABLE `bon_travail`
  MODIFY `Id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `chaine_equipement`
--
ALTER TABLE `chaine_equipement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `demande_intervention`
--
ALTER TABLE `demande_intervention`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `equipe_piece`
--
ALTER TABLE `equipe_piece`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `operation`
--
ALTER TABLE `operation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `oper_lubri`
--
ALTER TABLE `oper_lubri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `oper_piece`
--
ALTER TABLE `oper_piece`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `piece_rechange_bon_approvisionnement`
--
ALTER TABLE `piece_rechange_bon_approvisionnement`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  ADD CONSTRAINT `FK_BT_3` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Reference`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BT_4` FOREIGN KEY (`RefDIM`) REFERENCES `demande_intervention` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BT_5` FOREIGN KEY (`Operation`) REFERENCES `operation` (`id`),
  ADD CONSTRAINT `FK_BT_6` FOREIGN KEY (`Section`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `chaine_equipement`
--
ALTER TABLE `chaine_equipement`
  ADD CONSTRAINT `FK_CE_1` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Reference`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CE_2` FOREIGN KEY (`RefChaine`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `demande_intervention`
--
ALTER TABLE `demande_intervention`
  ADD CONSTRAINT `FK_DI_1` FOREIGN KEY (`CodeEquipement`) REFERENCES `equipement` (`Reference`),
  ADD CONSTRAINT `FK_DI_2` FOREIGN KEY (`Matricule_RCP`) REFERENCES `responsable_chaine_production` (`Matricule`),
  ADD CONSTRAINT `FK_DI_3` FOREIGN KEY (`Matricule_RM`) REFERENCES `responsable_maintenance` (`Matricule`),
  ADD CONSTRAINT `FK_DI_4` FOREIGN KEY (`Section`) REFERENCES `chaine_production` (`RefChaine`);

--
-- Constraints for table `equipe_piece`
--
ALTER TABLE `equipe_piece`
  ADD CONSTRAINT `equipe_piece_ibfk_1` FOREIGN KEY (`Equipement`) REFERENCES `equipement` (`Reference`),
  ADD CONSTRAINT `equipe_piece_ibfk_2` FOREIGN KEY (`piece`) REFERENCES `piece_rechange` (`Reference`);

--
-- Constraints for table `oper_lubri`
--
ALTER TABLE `oper_lubri`
  ADD CONSTRAINT `oper_lubri_ibfk_1` FOREIGN KEY (`oper`) REFERENCES `operation` (`id`),
  ADD CONSTRAINT `oper_lubri_ibfk_2` FOREIGN KEY (`lubri`) REFERENCES `lubrification` (`Reference`);

--
-- Constraints for table `oper_piece`
--
ALTER TABLE `oper_piece`
  ADD CONSTRAINT `oper_piece_ibfk_1` FOREIGN KEY (`oper`) REFERENCES `operation` (`id`),
  ADD CONSTRAINT `oper_piece_ibfk_2` FOREIGN KEY (`piece`) REFERENCES `piece_rechange` (`Reference`);

--
-- Constraints for table `piece_rechange_bon_approvisionnement`
--
ALTER TABLE `piece_rechange_bon_approvisionnement`
  ADD CONSTRAINT `FK_PRBA_1` FOREIGN KEY (`Code_Piece`) REFERENCES `piece_rechange` (`Reference`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PRBA_2` FOREIGN KEY (`Id_bon`) REFERENCES `bon_approvisionnement` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `responsable_chaine_production`
--
ALTER TABLE `responsable_chaine_production`
  ADD CONSTRAINT `FK_1` FOREIGN KEY (`RefChaine`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `responsable_maintenance`
--
ALTER TABLE `responsable_maintenance`
  ADD CONSTRAINT `FK_RM_1` FOREIGN KEY (`RefChaine`) REFERENCES `chaine_production` (`RefChaine`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

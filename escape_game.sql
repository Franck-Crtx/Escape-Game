-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 13 juil. 2021 à 19:06
-- Version du serveur : 10.4.19-MariaDB
-- Version de PHP : 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `escape_game`
--
CREATE DATABASE IF NOT EXISTS `escape_game` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `escape_game`;

-- --------------------------------------------------------

--
-- Structure de la table `acheteur`
--

DROP TABLE IF EXISTS `acheteur`;
CREATE TABLE `acheteur` (
  `id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `civilite` tinyint(1) NOT NULL,
  `prenom` varchar(24) NOT NULL,
  `nom` varchar(24) NOT NULL,
  `age` tinyint(3) UNSIGNED NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `game`
--

DROP TABLE IF EXISTS `game`;
CREATE TABLE `game` (
  `id` int(11) NOT NULL,
  `nom` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `game`
--

INSERT INTO `game` (`id`, `nom`) VALUES
(1, 'Impôt sur le revenu'),
(2, 'Grève des fonctionnaires'),
(3, 'Interminable attente chez le médecin'),
(4, 'Soutenance finale'),
(5, 'Mon compte en banque en fin du mois'),
(6, 'Mariage sans alcool'),
(7, 'Dîner de famille insoutenable'),
(8, 'Plus de PQ dans les toilettes'),
(9, 'En plein dans la Friendzone');

-- --------------------------------------------------------

--
-- Structure de la table `game_has_themes`
--

DROP TABLE IF EXISTS `game_has_themes`;
CREATE TABLE `game_has_themes` (
  `theme_id` int(11) NOT NULL,
  `type_theme` int(11) NOT NULL,
  `game_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `game_has_themes`
--

INSERT INTO `game_has_themes` (`theme_id`, `type_theme`, `game_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 1, 2),
(4, 2, 2),
(5, 1, 3),
(6, 2, 3),
(2, 1, 4),
(3, 2, 4),
(4, 1, 5),
(1, 2, 5),
(7, 1, 6),
(8, 2, 6),
(6, 1, 7),
(5, 2, 7),
(9, 1, 8),
(7, 2, 8),
(8, 1, 9),
(9, 2, 9);

-- --------------------------------------------------------

--
-- Structure de la table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `state` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `login`
--

INSERT INTO `login` (`id`, `state`) VALUES
(43, 1),
(44, 1);

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE `reservation` (
  `id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `jour` date NOT NULL,
  `horaire` time NOT NULL,
  `vr` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `reservation_has_spectateurs`
--

DROP TABLE IF EXISTS `reservation_has_spectateurs`;
CREATE TABLE `reservation_has_spectateurs` (
  `id` int(11) NOT NULL,
  `spectateur_id` int(11) NOT NULL,
  `reservation_id` int(11) NOT NULL,
  `tarif_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `spectateur`
--

DROP TABLE IF EXISTS `spectateur`;
CREATE TABLE `spectateur` (
  `id` int(11) NOT NULL,
  `civilite` tinyint(1) NOT NULL,
  `nom` varchar(60) NOT NULL,
  `prenom` varchar(60) NOT NULL,
  `age` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `tarif`
--

DROP TABLE IF EXISTS `tarif`;
CREATE TABLE `tarif` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prix` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `tarif`
--

INSERT INTO `tarif` (`id`, `nom`, `prix`) VALUES
(1, 'Tarif plein', 10),
(2, 'Tarif réduit', 8),
(3, 'Tarif sénior', 7),
(4, 'Tarif étudiant', 7);

-- --------------------------------------------------------

--
-- Structure de la table `theme`
--

DROP TABLE IF EXISTS `theme`;
CREATE TABLE `theme` (
  `id` int(11) NOT NULL,
  `nom` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `theme`
--

INSERT INTO `theme` (`id`, `nom`) VALUES
(1, 'Braquage'),
(2, 'Stress'),
(3, 'Rapidité'),
(4, 'Mythologique'),
(5, 'Stratégie'),
(6, 'Psychologie'),
(7, 'Santé'),
(8, 'Amour'),
(9, 'Horreur');

-- --------------------------------------------------------

--
-- Structure de la table `type_theme`
--

DROP TABLE IF EXISTS `type_theme`;
CREATE TABLE `type_theme` (
  `id` int(11) NOT NULL,
  `nom` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `type_theme`
--

INSERT INTO `type_theme` (`id`, `nom`) VALUES
(1, 'principale'),
(2, 'secondaire');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(254) NOT NULL,
  `nom` varchar(60) NOT NULL,
  `prenom` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `login_id`, `email`, `password`, `nom`, `prenom`) VALUES
(8, 43, 'habi_a@etna-alternance.net', 'b\'gAAAAABg6yxHEbQAe7dJTSthwTrau4Gmo_vAoc3asC8autnD6R_V3X7gsLH3H_6MMLaJYwhGuR6VTQfhOAs8eICmI_e-ou2RUg==\'', 'Habi', 'Acal'),
(9, 44, 'courta_f@etna-alternance.net', 'b\'gAAAAABg6yxog7hAAy8DBjeaB928YGywN67xjs0V7R6u50N3VB4KJKAhXR3Mo5m8uMjxCtcF8ArI9IhaWJLZKbKcu8Bxl7SOxg==\'', 'Courtaux', 'Franck');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `acheteur`
--
ALTER TABLE `acheteur`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `login_id` (`login_id`);

--
-- Index pour la table `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `game_has_themes`
--
ALTER TABLE `game_has_themes`
  ADD KEY `theme_id` (`theme_id`),
  ADD KEY `type_theme` (`type_theme`),
  ADD KEY `game_has_themes_ibfk_1` (`game_id`);

--
-- Index pour la table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_id` (`login_id`),
  ADD KEY `game_id` (`game_id`);

--
-- Index pour la table `reservation_has_spectateurs`
--
ALTER TABLE `reservation_has_spectateurs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `game_id` (`reservation_id`),
  ADD KEY `spectateur_id` (`spectateur_id`),
  ADD KEY `tarif_id` (`tarif_id`);

--
-- Index pour la table `spectateur`
--
ALTER TABLE `spectateur`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tarif`
--
ALTER TABLE `tarif`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `type_theme`
--
ALTER TABLE `type_theme`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `login_id` (`login_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `acheteur`
--
ALTER TABLE `acheteur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT pour la table `game`
--
ALTER TABLE `game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT pour la table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `reservation_has_spectateurs`
--
ALTER TABLE `reservation_has_spectateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `spectateur`
--
ALTER TABLE `spectateur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `tarif`
--
ALTER TABLE `tarif`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `theme`
--
ALTER TABLE `theme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `type_theme`
--
ALTER TABLE `type_theme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `acheteur`
--
ALTER TABLE `acheteur`
  ADD CONSTRAINT `acheteur_ibfk_1` FOREIGN KEY (`login_id`) REFERENCES `login` (`id`);

--
-- Contraintes pour la table `game_has_themes`
--
ALTER TABLE `game_has_themes`
  ADD CONSTRAINT `game_has_themes_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  ADD CONSTRAINT `game_has_themes_ibfk_2` FOREIGN KEY (`theme_id`) REFERENCES `theme` (`id`),
  ADD CONSTRAINT `game_has_themes_ibfk_3` FOREIGN KEY (`type_theme`) REFERENCES `type_theme` (`id`);

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`login_id`) REFERENCES `login` (`id`),
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`);

--
-- Contraintes pour la table `reservation_has_spectateurs`
--
ALTER TABLE `reservation_has_spectateurs`
  ADD CONSTRAINT `reservation_has_spectateurs_ibfk_1` FOREIGN KEY (`reservation_id`) REFERENCES `reservation` (`id`),
  ADD CONSTRAINT `reservation_has_spectateurs_ibfk_2` FOREIGN KEY (`spectateur_id`) REFERENCES `spectateur` (`id`),
  ADD CONSTRAINT `reservation_has_spectateurs_ibfk_3` FOREIGN KEY (`tarif_id`) REFERENCES `tarif` (`id`);

--
-- Contraintes pour la table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`login_id`) REFERENCES `login` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

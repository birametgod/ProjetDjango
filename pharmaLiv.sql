-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  Dim 01 avr. 2018 à 20:04
-- Version du serveur :  10.1.31-MariaDB
-- Version de PHP :  7.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `pharmaLiv`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add ordonnances', 6, 'add_ordonnances'),
(17, 'Can change ordonnances', 6, 'change_ordonnances'),
(18, 'Can delete ordonnances', 6, 'delete_ordonnances'),
(19, 'Can add patient', 7, 'add_patient'),
(20, 'Can change patient', 7, 'change_patient'),
(21, 'Can delete patient', 7, 'delete_patient'),
(22, 'Can add userbi', 8, 'add_userbi'),
(23, 'Can change userbi', 8, 'change_userbi'),
(24, 'Can delete userbi', 8, 'delete_userbi'),
(25, 'Can add medecin', 9, 'add_medecin'),
(26, 'Can change medecin', 9, 'change_medecin'),
(27, 'Can delete medecin', 9, 'delete_medecin'),
(28, 'Can add commandes_ effectuees', 10, 'add_commandes_effectuees'),
(29, 'Can change commandes_ effectuees', 10, 'change_commandes_effectuees'),
(30, 'Can delete commandes_ effectuees', 10, 'delete_commandes_effectuees'),
(31, 'Can add fiche_ produit', 11, 'add_fiche_produit'),
(32, 'Can change fiche_ produit', 11, 'change_fiche_produit'),
(33, 'Can delete fiche_ produit', 11, 'delete_fiche_produit'),
(34, 'Can add pharmacie', 12, 'add_pharmacie'),
(35, 'Can change pharmacie', 12, 'change_pharmacie'),
(36, 'Can delete pharmacie', 12, 'delete_pharmacie'),
(37, 'Can add user', 13, 'add_user'),
(38, 'Can change user', 13, 'change_user'),
(39, 'Can delete user', 13, 'delete_user');

-- --------------------------------------------------------

--
-- Structure de la table `connexion_user`
--

CREATE TABLE `connexion_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  `is_medecin` tinyint(1) NOT NULL,
  `is_livreur` tinyint(1) NOT NULL,
  `is_pharmacie` tinyint(1) NOT NULL,
  `is_userbi` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `connexion_user`
--

INSERT INTO `connexion_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_patient`, `is_medecin`, `is_livreur`, `is_pharmacie`, `is_userbi`) VALUES
(3, 'pbkdf2_sha256$100000$H8HxjxelqI49$VNFWJjsCga33VrOQqCT+K8xBcw7Ayd2JsEviLgivC64=', '2018-04-01 15:57:41.873979', 0, 'birametgod', '', '', 'birame@gmail.com', 0, 1, '2018-04-01 15:57:41.720965', 0, 0, 0, 0, 1),
(4, 'pbkdf2_sha256$100000$nuOaLMzG9qIT$ttyOSzLUoS75p9pZnG1Wxh5TUFi9EB88AmO1Gc7PX+U=', '2018-04-01 16:28:20.825083', 0, 'cheickh', '', '', 'cheickh@gmail.com', 0, 1, '2018-04-01 16:28:20.608124', 0, 0, 0, 0, 1),
(5, 'pbkdf2_sha256$100000$hhL4jD5MvNhn$Y+J7MduGo+nkNJr0OiNO18krrfSkbV3y0h0+2h1fHXQ=', '2018-04-01 16:54:07.438741', 0, 'mouhamed', '', '', 'mouh@gmail.com', 0, 1, '2018-04-01 16:33:59.864195', 0, 0, 0, 0, 1),
(7, 'pbkdf2_sha256$100000$opCDLs9tIKMY$rXtFAPQehT4y6GWYxIMW2vfxd6hG9OQz//E8MeDUoMo=', '2018-04-01 17:17:11.177777', 0, 'birame', 'Birame', 'SENE', 'bira@gmail.com', 0, 1, '2018-04-01 17:17:11.025894', 1, 0, 0, 0, 0),
(8, 'pbkdf2_sha256$100000$eRVVYafjCi5C$8lOqjdz5Httzj62QFAAsDCbNaWJ8GAT7XE0KiswKAWY=', '2018-04-01 18:01:12.707765', 0, 'mouha', 'Mouhamed', 'Wade', 'wade@gmail.com', 0, 1, '2018-04-01 17:36:49.612156', 1, 0, 0, 0, 0),
(9, 'pbkdf2_sha256$100000$zXOmjWD3Uj9W$lczhKReZ5qrc0a8K75UcVLkQYXEHKQm/BO24l9BY7Kk=', '2018-04-01 18:02:38.509521', 0, 'ismaila', 'Ismaila', 'Badiane', 'iso@gmail.com', 0, 1, '2018-04-01 18:02:38.357005', 1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `connexion_user_groups`
--

CREATE TABLE `connexion_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `connexion_user_user_permissions`
--

CREATE TABLE `connexion_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(13, 'connexion', 'user'),
(4, 'contenttypes', 'contenttype'),
(9, 'medecin', 'medecin'),
(6, 'patient', 'ordonnances'),
(7, 'patient', 'patient'),
(8, 'patient', 'userbi'),
(10, 'pharmacie', 'commandes_effectuees'),
(11, 'pharmacie', 'fiche_produit'),
(12, 'pharmacie', 'pharmacie'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-01 02:36:15.784216'),
(2, 'contenttypes', '0002_remove_content_type_name', '2018-04-01 02:36:15.823320'),
(3, 'auth', '0001_initial', '2018-04-01 02:36:15.979907'),
(4, 'auth', '0002_alter_permission_name_max_length', '2018-04-01 02:36:16.012382'),
(5, 'auth', '0003_alter_user_email_max_length', '2018-04-01 02:36:16.022817'),
(6, 'auth', '0004_alter_user_username_opts', '2018-04-01 02:36:16.035077'),
(7, 'auth', '0005_alter_user_last_login_null', '2018-04-01 02:36:16.045207'),
(8, 'auth', '0006_require_contenttypes_0002', '2018-04-01 02:36:16.047423'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2018-04-01 02:36:16.059092'),
(10, 'auth', '0008_alter_user_username_max_length', '2018-04-01 02:36:16.072916'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2018-04-01 02:36:16.086519'),
(12, 'connexion', '0001_initial', '2018-04-01 02:36:16.282823'),
(13, 'admin', '0001_initial', '2018-04-01 02:36:16.390692'),
(14, 'admin', '0002_logentry_remove_auto_add', '2018-04-01 02:36:16.414809'),
(15, 'medecin', '0001_initial', '2018-04-01 02:36:16.441606'),
(16, 'medecin', '0002_auto_20180331_1640', '2018-04-01 02:36:16.511186'),
(17, 'patient', '0001_initial', '2018-04-01 02:36:16.659103'),
(18, 'pharmacie', '0001_initial', '2018-04-01 02:36:16.785219'),
(19, 'sessions', '0001_initial', '2018-04-01 02:36:16.807415'),
(20, 'connexion', '0002_auto_20180401_0245', '2018-04-01 02:45:47.693159'),
(21, 'connexion', '0003_user_is_userbi', '2018-04-01 12:25:11.334920'),
(22, 'patient', '0002_auto_20180401_1710', '2018-04-01 17:10:28.535513'),
(23, 'patient', '0003_auto_20180401_1738', '2018-04-01 17:38:19.561762'),
(24, 'patient', '0004_auto_20180401_1739', '2018-04-01 17:39:09.124293'),
(25, 'patient', '0005_auto_20180401_1800', '2018-04-01 18:00:49.197517');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `medecin_medecin`
--

CREATE TABLE `medecin_medecin` (
  `id` int(11) NOT NULL,
  `login` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `prenom` varchar(30) NOT NULL,
  `dateNaissance` datetime(6) NOT NULL,
  `specialite` varchar(30) NOT NULL,
  `hopital` varchar(30) NOT NULL,
  `profil` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `patient_ordonnances`
--

CREATE TABLE `patient_ordonnances` (
  `id` int(11) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `medicaments` varchar(255) NOT NULL,
  `medecin_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `patient_patient`
--

CREATE TABLE `patient_patient` (
  `id` int(11) NOT NULL,
  `sexe` varchar(30) NOT NULL,
  `allergie` varchar(100) NOT NULL,
  `traitement` varchar(100) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `dateNaissance` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `patient_patient`
--

INSERT INTO `patient_patient` (`id`, `sexe`, `allergie`, `traitement`, `adresse`, `user_id`, `dateNaissance`) VALUES
(2, 'homme', 'rhume', 'beaucoup de mouchoirs', 'Dakar', 7, NULL),
(3, 'homme', 'Birame1995', 'envoie', 'Thies', 8, NULL),
(4, 'homme', 'les poils de chat', 'éviter les chats', 'Bordeaux', 9, '1996-10-01');

-- --------------------------------------------------------

--
-- Structure de la table `pharmacie_commandes_effectuees`
--

CREATE TABLE `pharmacie_commandes_effectuees` (
  `id` int(11) NOT NULL,
  `nomPatient` varchar(30) NOT NULL,
  `prenomPatient` varchar(30) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `telephonePatient` int(11) NOT NULL,
  `commande` varchar(200) NOT NULL,
  `dateCommande` datetime(6) NOT NULL,
  `dateLivraison` datetime(6) NOT NULL,
  `livree` tinyint(1) NOT NULL,
  `slug` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `pharmacie_fiche_produit`
--

CREATE TABLE `pharmacie_fiche_produit` (
  `id` int(11) NOT NULL,
  `titre` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `prix` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `types` varchar(10) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `nom_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `pharmacie_pharmacie`
--

CREATE TABLE `pharmacie_pharmacie` (
  `id` int(11) NOT NULL,
  `login` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `profil` varchar(100) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `telephone` int(11) NOT NULL,
  `horaire` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `connexion_user`
--
ALTER TABLE `connexion_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `connexion_user_groups`
--
ALTER TABLE `connexion_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `connexion_user_groups_user_id_group_id_538241cd_uniq` (`user_id`,`group_id`),
  ADD KEY `connexion_user_groups_group_id_78b4d561_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `connexion_user_user_permissions`
--
ALTER TABLE `connexion_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `connexion_user_user_perm_user_id_permission_id_5d202636_uniq` (`user_id`,`permission_id`),
  ADD KEY `connexion_user_user__permission_id_94c9f573_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_connexion_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `medecin_medecin`
--
ALTER TABLE `medecin_medecin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `medecin_medecin_slug_65b102cb` (`slug`);

--
-- Index pour la table `patient_ordonnances`
--
ALTER TABLE `patient_ordonnances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_ordonnances_medecin_id_2a4dace7_fk_medecin_medecin_id` (`medecin_id`),
  ADD KEY `patient_ordonnances_patient_id_6ea8455c_fk_patient_patient_id` (`patient_id`);

--
-- Index pour la table `patient_patient`
--
ALTER TABLE `patient_patient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_patient_user_id_40c1c82a_fk_connexion_user_id` (`user_id`);

--
-- Index pour la table `pharmacie_commandes_effectuees`
--
ALTER TABLE `pharmacie_commandes_effectuees`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pharmacie_commandes_effectuees_slug_4ba1b906` (`slug`);

--
-- Index pour la table `pharmacie_fiche_produit`
--
ALTER TABLE `pharmacie_fiche_produit`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pharmacie_fiche_produit_slug_807ae983` (`slug`),
  ADD KEY `pharmacie_fiche_prod_nom_id_3e0e5dd1_fk_pharmacie` (`nom_id`);

--
-- Index pour la table `pharmacie_pharmacie`
--
ALTER TABLE `pharmacie_pharmacie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pharmacie_pharmacie_slug_5350709a` (`slug`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT pour la table `connexion_user`
--
ALTER TABLE `connexion_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `connexion_user_groups`
--
ALTER TABLE `connexion_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `connexion_user_user_permissions`
--
ALTER TABLE `connexion_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT pour la table `medecin_medecin`
--
ALTER TABLE `medecin_medecin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `patient_ordonnances`
--
ALTER TABLE `patient_ordonnances`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `patient_patient`
--
ALTER TABLE `patient_patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `pharmacie_commandes_effectuees`
--
ALTER TABLE `pharmacie_commandes_effectuees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `pharmacie_fiche_produit`
--
ALTER TABLE `pharmacie_fiche_produit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `pharmacie_pharmacie`
--
ALTER TABLE `pharmacie_pharmacie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `connexion_user_groups`
--
ALTER TABLE `connexion_user_groups`
  ADD CONSTRAINT `connexion_user_groups_group_id_78b4d561_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `connexion_user_groups_user_id_e9a573aa_fk_connexion_user_id` FOREIGN KEY (`user_id`) REFERENCES `connexion_user` (`id`);

--
-- Contraintes pour la table `connexion_user_user_permissions`
--
ALTER TABLE `connexion_user_user_permissions`
  ADD CONSTRAINT `connexion_user_user__permission_id_94c9f573_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `connexion_user_user__user_id_604b856c_fk_connexion` FOREIGN KEY (`user_id`) REFERENCES `connexion_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_connexion_user_id` FOREIGN KEY (`user_id`) REFERENCES `connexion_user` (`id`);

--
-- Contraintes pour la table `patient_ordonnances`
--
ALTER TABLE `patient_ordonnances`
  ADD CONSTRAINT `patient_ordonnances_medecin_id_2a4dace7_fk_medecin_medecin_id` FOREIGN KEY (`medecin_id`) REFERENCES `medecin_medecin` (`id`),
  ADD CONSTRAINT `patient_ordonnances_patient_id_6ea8455c_fk_patient_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`id`);

--
-- Contraintes pour la table `patient_patient`
--
ALTER TABLE `patient_patient`
  ADD CONSTRAINT `patient_patient_user_id_40c1c82a_fk_connexion_user_id` FOREIGN KEY (`user_id`) REFERENCES `connexion_user` (`id`);

--
-- Contraintes pour la table `pharmacie_fiche_produit`
--
ALTER TABLE `pharmacie_fiche_produit`
  ADD CONSTRAINT `pharmacie_fiche_prod_nom_id_3e0e5dd1_fk_pharmacie` FOREIGN KEY (`nom_id`) REFERENCES `pharmacie_pharmacie` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

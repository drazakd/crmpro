-- Cr�ation de la table AccountsUtilisateurs
CREATE TABLE accounts_utilisateurs (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME NULL,
    is_superuser TINYINT NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff TINYINT NOT NULL,
    is_active TINYINT NOT NULL,
    date_joined DATETIME NOT NULL,
    role VARCHAR(30) NOT NULL,
    gender VARCHAR(30) NOT NULL
);

-- Cr�ation de la table AccountsUtilisateursGroups
CREATE TABLE accounts_utilisateurs_groups (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    accountsutilisateurs_id BIGINT NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (accountsutilisateurs_id) REFERENCES accounts_utilisateurs(id),
    UNIQUE(accountsutilisateurs_id, group_id)
);

-- Cr�ation de la table AccountsUtilisateursUserPermissions
CREATE TABLE accounts_utilisateurs_user_permissions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    utilisateurs_id BIGINT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (utilisateurs_id) REFERENCES accounts_utilisateurs(id),
    UNIQUE(utilisateurs_id, permission_id)
);

-- Cr�ation de la table AuthGroup
CREATE TABLE auth_group (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) UNIQUE NOT NULL
);

-- Cr�ation de la table AuthGroupPermissions
CREATE TABLE auth_group_permissions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    group_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES auth_group(id),
    UNIQUE(group_id, permission_id)
);

-- Cr�ation de la table AuthPermission
CREATE TABLE auth_permission (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    content_type_id INT NOT NULL,
    codename VARCHAR(100) NOT NULL,
    UNIQUE(content_type_id, codename)
);

-- Cr�ation de la table AuthUser
CREATE TABLE auth_user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME NULL,
    is_superuser TINYINT NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff TINYINT NOT NULL,
    is_active TINYINT NOT NULL,
    date_joined DATETIME NOT NULL
);

-- Cr�ation de la table AuthUserGroups
CREATE TABLE auth_user_groups (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    UNIQUE(user_id, group_id)
);

-- Cr�ation de la table AuthUserUserPermissions
CREATE TABLE auth_user_user_permissions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    UNIQUE(user_id, permission_id)
);

-- Cr�ation de la table Categorie
CREATE TABLE categorie (
    id_categorie INT PRIMARY KEY AUTO_INCREMENT,
    nom_categorie VARCHAR(255) NOT NULL
);

-- Cr�ation de la table Client
CREATE TABLE client (
    id_client INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    adresse TEXT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telephone VARCHAR(255) NOT NULL
);

-- Cr�ation de la table CommandeFournisseur
CREATE TABLE commande_fournisseur (
    id_commande_fournisseur INT PRIMARY KEY AUTO_INCREMENT,
    date_commande DATETIME NOT NULL,
    id_gestionnaire BIGINT NULL,
    id_fournisseur INT NULL,
    etat VARCHAR(8) NOT NULL,
    FOREIGN KEY (id_gestionnaire) REFERENCES accounts_utilisateurs(id),
    FOREIGN KEY (id_fournisseur) REFERENCES fournisseur(id_fournisseur)
);

-- Cr�ation de la table DjangoAdminLog
CREATE TABLE django_admin_log (
    action_time DATETIME NOT NULL,
    object_id TEXT NULL,
    object_repr VARCHAR(200) NOT NULL,
    action_flag SMALLINT UNSIGNED NOT NULL,
    change_message TEXT NOT NULL,
    content_type_id INT NULL,
    user_id INT NOT NULL
);

-- Cr�ation de la table DjangoContentType
CREATE TABLE django_content_type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    app_label VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    UNIQUE(app_label, model)
);

-- Cr�ation de la table DjangoMigrations
CREATE TABLE django_migrations (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    app VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    applied DATETIME NOT NULL
);



-- Cr�ation de la table DjangoSession
CREATE TABLE django_session (
    session_key VARCHAR(40) PRIMARY KEY,
    session_data TEXT NOT NULL,
    expire_date DATETIME NOT NULL
);

-- Cr�ation de la table Fournisseur
CREATE TABLE fournisseur (
    id_fournisseur INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    adresse TEXT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telephone VARCHAR(255) NOT NULL
);

-- Cr�ation de la table LigneCommandeFournisseur
CREATE TABLE ligne_commande_fournisseur (
    id_ligne_commande_fournisseur INT PRIMARY KEY AUTO_INCREMENT,
    quantite_commandee INT NOT NULL,
    prix_unitaire DECIMAL(10,2) NOT NULL,
    etat VARCHAR(8) NOT NULL,
    id_commande_fournisseur INT NULL,
    id_produit INT NULL,
    FOREIGN KEY (id_commande_fournisseur) REFERENCES commande_fournisseur(id_commande_fournisseur),
    FOREIGN KEY (id_produit) REFERENCES produit(id_produit)
);

-- Cr�ation de la table Produit
CREATE TABLE produit (
    id_produit INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    description TEXT NULL,
    prix DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    id_fournisseur INT NULL,
    id_categorie INT NULL,
    FOREIGN KEY (id_fournisseur) REFERENCES fournisseur(id_fournisseur),
    FOREIGN KEY (id_categorie) REFERENCES categorie(id_categorie)
);


-- Cr�ation de la table Vente
CREATE TABLE vente (
    id_vente INT PRIMARY KEY AUTO_INCREMENT,
    date_vente DATETIME NOT NULL,
    id_produit INT NULL,
    quantite INT NOT NULL,
    prix_unitaire DECIMAL(10,2) NOT NULL,
    id_client INT NULL,
    id INT NULL,
    FOREIGN KEY (id_produit) REFERENCES produit(id_produit),
    FOREIGN KEY (id_client) REFERENCES client(id_client),
    FOREIGN KEY (id) REFERENCES accounts_utilisateurs(id)
);
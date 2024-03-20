-- Dimension Table 1: DimGenre
CREATE TABLE DimGenre (
    GenreID INT PRIMARY KEY,
    GenreName VARCHAR(10) -- 'femme' and 'homme' are the possible values
);

-- Dimension Table 2: DimAge
CREATE TABLE DimAge (
    AgeID INT PRIMARY KEY,
    Age INT
);

-- Dimension Table 3: DimMaritalStatus
CREATE TABLE DimEtatCivil (
    EtatCivilID INT PRIMARY KEY,
    EtatCivil  VARCHAR(10) -- Assuming 'yes' and 'no' are the possible values
);

CREATE TABLE FactChurnEvent ( 
    ChurnEventID INT PRIMARY KEY,
    ClientID VARCHAR(30),
	NumTel VARCHAR(20), -- Assuming maximum length for telephone numbers
    NbJoursAbonne INT, -- Usage metric
    DureeAppelJour FLOAT, -- Usage metric
    NbAppelJour INT, -- Usage metric
    CoutAppelJour FLOAT, -- Usage metric
    DureeAppelSoiree FLOAT, -- Usage metric
    NbAppelNuit INT, -- Usage metric
    CoutAppelNuit FLOAT, -- Usage metric
    DureeAppelInter FLOAT, -- Usage metric
    NbAppelInter INT, -- Usage metric
    CoutAppelInter FLOAT, -- Usage metric
    ActiveMsgVocaux INT, -- Usage metric
    NbMsgVocaux INT, -- Usage metric
    NbReclamation INT, -- Usage metric
	GenreID INT, -- Foreign key referencing genre dimension table
    AgeID INT, -- Foreign key referencing age dimension table
	EtatCivilID INT -- Foreign key referencing marital status dimension table
	);


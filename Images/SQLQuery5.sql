-- Add foreign key constraint for GenreID referencing DimGenre
ALTER TABLE FactChurnEvent
ADD CONSTRAINT FK_FactChurnEvents_GenreID
FOREIGN KEY (GenreID)
REFERENCES DimGenre(GenreID);

-- Add foreign key constraint for AgeID referencing DimAge
ALTER TABLE FactChurnEvent
ADD CONSTRAINT FK_FactChurnEvents_AgeID
FOREIGN KEY (AgeID)
REFERENCES DimAge(AgeID);

-- Add foreign key constraint for MaritalStatusID referencing DimMaritalStatus
ALTER TABLE FactChurnEvent
ADD CONSTRAINT FK_FactChurnEvents_EtatCivilID
FOREIGN KEY (EtatCivilID)
REFERENCES DimEtatCivil(EtatCivilID);
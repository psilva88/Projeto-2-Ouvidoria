CREATE TABLE manifestation (
    codigo INT AUTO_INCREMENT ,
    tipo ENUM('Reclamação', 'Sugestão', 'Elogio') NOT NULL,
    manifestacao VARCHAR(255),
    PRIMARY KEY (codigo)
);

SELECT * FROM manifestation;

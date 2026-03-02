CREATE TABLE Usuario(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(1OO) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(200) NOT NULL,
    tipo VARCHAR(50) DEFAULT 'usuario'
);

CREATE TABLE Enquete(
    id_enquete INT AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	descricao TEXT,
	data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'rascunho',
    id_admin INT,
    FOREIGN KEY (id_admin) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Candidato(
	id_candidato INT AUTO_INCREMENT PRIMARY KEY,
	descricao VARCHAR(200) NOT NULL,
	id_enquete INT,
    FOREIGN KEY (id_enquete) REFERENCES Enquete(id_enquete)
); 

CREATE TABLE Voto(
	id_voto INT AUTO_INCREMENT PRIMARY KEY,
    data_voto TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT,
    id_enquete INT,
    id_candidato INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_enquete) REFERENCES Enquete(id_enquete),
    FOREIGN KEY (id_candidato) REFERENCES Candidato(id_candidato),
    UNIQUE KEY voto_unico (id_usuario, id_enquete)
);
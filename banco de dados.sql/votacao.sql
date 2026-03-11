Create table usuario(
 id INT PRIMARY KEY AUTO_INCREMENT,
nome Varchar(104) NOT NULL,	
email Varchar(24) NOT NULL UNIQUE,
senha varchar(20)NOT NULL,
tipo ENUM("Admin, eleitor") NOT NULL
    );	
 
CREATE TABLE Enquete(
id INT PRIMARY KEY AUTO_INCREMENT,
 id_usuario INT NOT NULL,
 titulo varchar(54) NOT NULL,
descricao TEXT,	
 dataInicio DATETIME NOT NULL,
dataFim DATETIME NOT NULL,
status ENUM('ativa, encerrada, pendente') NOT NULL default 'pendente',
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
        );
        
        CREATE TABLE Opcao(
            id_enquete INT NOT NULL,
            id INT PRIMARY KEY AUTO_INCREMENT,
            descricao varchar(30) NOT NULL,
            quantidadeVotos INT DEFAULT 0,
            FOREIGN KEY (id_enquete) REFERENCES Enquete(id)
            );
            
            CREATE TABLE Resusltado(
                id INT PRIMARY KEY AUTO_INCREMENT,
                id_enquete INT NOT NULL,
                totalVotos INT DEFAULT 0,
                FOREIGN KEY (id_enquete) REFERENCES Enquete(id)
                );
                
                CREATE TABLE Voto(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    id_usuario INT NOT NULL,
                    id_enqute INT NOT NULL,
                    id_opcao INT NOT NULL,
                    dataVoto DATETIME NOT NULL,
                    UNIQUE(id_usuario, id_enquete),
                    FOREIGN KEY (id_usuario) REFERENCES Uuario(id),
                    FOREIGN KEY (id_enqete) REFERENCES Enqute(id),
                    FOREIGN KEY (id_opcao) REFERENCES Opcao(id)
                    );
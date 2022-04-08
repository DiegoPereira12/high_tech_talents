CREATE TABLE proprietario ( 
 id INT PRIMARY KEY NOT NULL,  
 nome CHAR(100) NOT NULL,  
 data_nascimento DATE NOT NULL,  
 id_imovel INT NOT NULL,  
); 

CREATE TABLE imovel ( 
 id INT PRIMARY KEY NOT NULL,  
 logradouro CHAR(100) NOT NULL,  
 cep VARCHAR(100) NOT NULL,  
 bairro CHAR(100) NOT NULL,  
 cidade INT NOT NULL,  
 id_proprietario INT NOT NULL,  
); 

CREATE TABLE aluguel ( 
 id INT PRIMARY KEY NOT NULL,  
 id_imovel INT NOT NULL,  
 id_inquilino INT NOT NULL,  
); 

CREATE TABLE inquilino 
( 
 id INT PRIMARY KEY NOT NULL,  
 nome CHAR(100) NOT NULL,  
 data_nascimento DATE NOT NULL,  
); 



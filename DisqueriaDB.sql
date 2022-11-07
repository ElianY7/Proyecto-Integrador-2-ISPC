CREATE DATABASE proyecto_discografica;

USE proyecto_discografica;

CREATE TABLE IF NOT EXISTS Interprete
(
id_interprete INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
pais VARCHAR(3) NOT NULL,
foto VARCHAR (100),
CONSTRAINT id_interprete PRIMARY KEY(id_interprete)
);

CREATE TABLE IF NOT EXISTS Genero
(
id_genero INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
CONSTRAINT id_genero PRIMARY KEY(id_genero)
);

CREATE TABLE IF NOT EXISTS Discografia
(
id_discografia INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
CONSTRAINT id_discografia PRIMARY KEY(id_discografia)
);

CREATE TABLE IF NOT EXISTS Formato
(
id_formato INT NOT NULL AUTO_INCREMENT,
tipo VARCHAR(20) NOT NULL,
CONSTRAINT id_formato PRIMARY KEY(id_formato)
);

CREATE TABLE IF NOT EXISTS Album
(
id_album INT NOT NULL AUTO_INCREMENT,
cod_album INT NOT NULL,
nombre VARCHAR(50) NOT NULL,
id_interprete INT NOT NULL,	
id_genero INT NOT NULL,
cant_temas INT NOT NULL,
id_discografia INT NOT NULL,
id_formato INT NOT NULL,
fec_lanzamiento YEAR NOT NULL,
precio FLOAT NOT NULL,
cantidad INT NOT NULL,
caratula VARCHAR (60) NOT NULL,
CONSTRAINT id_album PRIMARY KEY(id_album),
CONSTRAINT id_interprete FOREIGN KEY(id_interprete) REFERENCES Interprete(id_interprete),
CONSTRAINT id_genero FOREIGN KEY(id_genero) REFERENCES Genero(id_genero),
CONSTRAINT id_discografia FOREIGN KEY(id_discografia) REFERENCES Discografia(id_discografia),
CONSTRAINT id_formato FOREIGN KEY(id_formato) REFERENCES Formato(id_formato)
);

CREATE TABLE IF NOT EXISTS Tema
(
id_tema INT NOT NULL AUTO_INCREMENT,
titulo VARCHAR(50) NOT NULL,
duracion TIME NOT NULL,
autor VARCHAR(100) NOT NULL,
compositor VARCHAR(50) NOT NULL,
id_album INT NOT NULL,
f_id_interprete INT NOT NULL,
CONSTRAINT id_tema PRIMARY KEY(id_tema),
CONSTRAINT f_id_interprete FOREIGN KEY(f_id_interprete) REFERENCES Interprete(id_interprete),
CONSTRAINT id_album FOREIGN KEY(id_album) REFERENCES Album(id_album)
);

INSERT INTO Genero (id_genero,nombre) VALUES
(null,"Pop"),
(null,"Clasica"),
(null,"Rock"),
(null,"Electronica"),
(null,"Hip hop/Rap"),
(null,"Reggae"),
(null,"Jazz"),
(null,"Country"),
(null,"Salsa"),
(null,"Indie"),
(null,"Reggaeton"),
(null,"Disco");

INSERT INTO Formato (id_formato,tipo) VALUES
(null,"CD"),
(null,"Vinilo"),
(null,"Cassette"),
(null,"Digital");

INSERT INTO Discografia (id_discografia,nombre) VALUES
(null,"Universal Music Group"),
(null,"Warner Music Group"),
(null,"Sony Music Entertainment"),
(null,"RCA Records"),
(null,"Columbia Records"),
(null,"MCA Records"),
(null,"PolyGram"),
(null,"EMI Music"),
(null,"Epic Records"),
(null,"Island Records"),
(null,"Atlantic Records");

INSERT INTO Interprete (id_interprete,nombre,pais,foto) VALUES
(null,"Michael Jackson","USA","https://acortar.link/wObbc5"),
(null,"Daft Punk","FRA","https://acortar.link/aKA5iN"),
(null,"AC/DC","GBR","https://acortar.link/RaWxQH"),
(null,"Pink Floyd","GBR","https://acortar.link/WzIYi8"),
(null,"Whitney Houston","USA","https://acortar.link/DuGp0h"),
(null,"Bee Gees","GBR","https://acortar.link/rYNURK"),
(null,"Guns N' Roses","USA","https://acortar.link/1OXynO"),
(null,"The Beatles","GBR","https://acortar.link/oC6lOj"),
(null,"Bill Evans","USA","https://acortar.link/NKovyr"),
(null,"John Lennon","GBR","https://acortar.link/S1ANov"),
(null,"Queen","GBR","https://acortar.link/BuLud5"),
(null,"Bob Marley","JAM","https://acortar.link/x4pnb7"),
(null,"Elton John","GBR","https://acortar.link/MpZ0xR");

INSERT INTO Album (id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula) VALUES 
(null,1351,"Thriller",1,1,9,9,1,"1982",3200,27,"https://acortar.link/tX92Yo"),
(null,2342,"Back in black",3,3,10,11,1,"1980",4200,4,"https://acortar.link/fcB4WG"),
(null,8261,"The dark side of the moon",4,3,9,1,2,"1973",9200,2,"https://acortar.link/WZqiv6"),
(null,9312,"The bodygard (BSO)",5,1,12,3,1,"1982",2400,21,"https://acortar.link/8peDB6"),
(null,0191,"Saturday Night Fever",6,12,6,7,2,"1977",8500,11,"https://acortar.link/I5EY3o"),
(null,1738,"Bad",1,1,11,9,3,"1987",2500,13,"https://acortar.link/tdjuj9"),
(null,8102,"Appetite for Destruction",7,3,12,1,3,"1987",2700,2,"https://acortar.link/q3aFB8"),
(null,3781,"Random Access Memories",2,4,13,5,1,"2013",4250,28,"https://acortar.link/Ugrg0e"),
(null,1829,"You Must Believe In Spring",9,7,7,2,2,"1977",6700,6,"https://acortar.link/XTU4en"),
(null,3821,"Soul Revolution",12,6,12,10,1,"1971",3500,12,"https://acortar.link/wG9O5E"),
(null,4532,"The One",13,1,11,6,3,"1992",2100,50,"https://acortar.link/kGx9Q5");



INSERT INTO Tema (id_tema,titulo,duracion,autor,compositor,id_album,f_id_interprete) VALUES
(null,"Wanna Be Startin' Somethin'","00:06:04","Rod Temperton","Quincy Jones",1,1),
(null,"Beat It","00:04:19","Rod Temperton","Quincy Jones",1,1),
(null,"Billie Jean","00:04:56","Rod Temperton","Quincy Jones",1,1),
(null,"Smooth Criminal","00:04:17","Michael Jackson","Quincy Jones, Michael Jackson",6,1),
(null,"Get Lucky","00:06:07","Thomas Bangalter, Guy-Manuel de Homem-Christo, Pharrell Williams, Nile Rodgers","Daft Punk",8,2),
(null,"Stayin' Alive","00:04:44","Barry Gibb, Robin Gibb, Maurice Gibb","Bee Gees, Albhy Galuten, Karl Richardson",5,6);




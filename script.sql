#Creamos las tablas de la base de datos "Usuarios"
DROP TABLE          IF EXISTS users;
DROP PROCEDURE      IF EXISTS user_insert_sp;



CREATE TABLE users(
    user_id             INT             NOT NULL    AUTO_INCREMENT,
    user_name           VARCHAR(150)    NOT NULL    UNIQUE,
    user_email          VARCHAR(255)    NOT NULL    UNIQUE,
    user_password       VARCHAR(255)    NOT NULL,
    user_attempts       INT             NOT NULL,

    
    PRIMARY KEY (user_id)
);


#Creamos las funciones de los store tabla;

DELIMITER //
CREATE PROCEDURE user_insert_sp(IN  _name VARCHAR(150) , 
                                IN  _password VARCHAR(255),
                                IN  _email VARCHAR(255))
    BEGIN
        DECLARE pass_encryp VARCHAR(255);
        SET     pass_encryp = SHA2(_password,224);
        
        INSERT  INTO users(user_name,user_email,user_password,user_attempts)
                VALUES(_name,pass_encryp,_email,0);
        
    END;
    
    //
    DELIMITER ;
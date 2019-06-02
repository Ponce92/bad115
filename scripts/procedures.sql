#-- Eliminamos los procedimientos
DROP PROCEDURE      IF EXISTS user_insert_sp;




#--Procedimientos de la tabla USUARIOS
DELIMITER //
CREATE PROCEDURE user_insert_sp(IN  _code VARCHAR(8),
                                IN  _name VARCHAR(150) ,
                                IN  _password VARCHAR(255),
                                IN  _email VARCHAR(255),
                                IN  _rol VARCHAR(4))
    BEGIN
        DECLARE pass_encryp VARCHAR(255);
        SET     pass_encryp = SHA2(_password,224);

        INSERT  INTO users(user_code,user_name,rol_code,user_email,user_password,user_attempts,user_state)
                VALUES(_code,_name,_rol,_email,pass_encryp,0,'ACT');

    END;

    //
    DELIMITER ;

DELIMITER $$
#--------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE rol_get_all_sp()
    BEGIN
    SELECT * FROM roles where rol_code<> 'ADIT';
    END;
    $$
    DELIMITER ;
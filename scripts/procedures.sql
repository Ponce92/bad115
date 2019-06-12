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

#----------------------------------------------------------------------------------------
DELIMITER $$

CREATE  PROCEDURE bsp_delete_menu(
                    IN  p_codigo    VARCHAR(6),
                    OUT w_estado    VARCHAR(10),
                    OUT w_mensaje   VARCHAR(150)
                    )
    BEGIN

        DECLARE cuenta  INT;
        DECLARE count	INT;
        SET count = (SELECT COUNT(*) FROM bt_menus men WHERE men.pk_codigo=p_codigo);

		IF count = 0 THEN
			SET cuenta=(SELECT COUNT(*) FROM bt_menus men WHERE men.fk_menu_codigo = p_codigo);
			IF cuenta > 0 THEN
				DELETE FROM bt_menus  men WHERE pk_codigo=p_codigo;
                SET w_estado := 'SUCCESS';
				SET w_mensaje := 'El menu se ha eliminado correctamente';

            ELSE
				SET w_estado := 'WARN';
				SET w_mensaje := 'El menu no puede ser borrado debido a que posee submenus asociados';
            END IF;
		ELSE
			SET w_estado := 'ERROR';
			SET w_mensaje := 'El recurso no se encuentra disponible';
        END IF;


        SELECT w_estado,w_mensaje ;
    END
    $$
DELIMITER ;
# -----------------------------------------------------------------------------------------------------
# Desc: Procedimiento que obtiene los permisos de ro que esten o no esten asociados segun la bandera


# Desc :: Si la bandera es true entonces obtiene los permisos asociados si es falso obtene los permisos que aun no estan asociados . . .
DROP PROCEDURE  IF EXISTS bsp_get_permisos_roles;
DELIMITER $$
CREATE  PROCEDURE bsp_get_permisos_roles(
                    IN  p_bandera   BOOLEAN,
                    IN  p_codigo    VARCHAR(8)
                    )

    BEGIN
        DECLARE conteo   INT;
        SET conteo = (SELECT COUNT(*) FROM bt_roles_permisos WHERE fk_rol_codigo=p_codigo);
		IF p_bandera THEN
            ##Recuperamos lo registros depermisos que se relacionan con el rol .. .
            IF conteo < 1 THEN
                #retrona una secuencia vacia
                SELECT * FROM bt_permisos where pk_codigo = 'none';
		    ELSE
                SELECT * FROM bt_permisos WHERE pk_codigo
                        IN (
                            SELECT fk_permiso_codigo FROM bt_roles_permisos WHERE fk_rol_codigo = p_codigo
                            );

            END IF;

		ELSE
			SELECT * FROM bt_permisos pe WHERE pk_codigo
					 NOT IN (
						SELECT fk_permiso_codigo FROM bt_roles_permisos WHERE fk_rol_codigo = p_codigo
						);
        END IF;

    END
    $$
DELIMITER ;

# -----------------------------------------------------------------------------------------------------
# Desc: Procedimiento que obtiene los permisos de ro que esten o no esten asociados segun la bandera


# Desc :: Si la bandera es true entonces obtiene los permisos asociados si es falso obtene los permisos que aun no estan asociados . . .
DROP PROCEDURE  IF EXISTS bsp_get_menus_roles;
DELIMITER $$
CREATE  PROCEDURE bsp_get_menus_roles(
                    IN  p_bandera   BOOLEAN,
                    IN  p_codigo    VARCHAR(8)
                    )

    BEGIN
        DECLARE conteo   INT;
        SET conteo = (SELECT COUNT(*) FROM bt_roles_menus WHERE fk_rol_codigo=p_codigo);
		IF p_bandera THEN
            ##Recuperamos lo registros depermisos que se relacionan con el rol .. .
            IF conteo < 1 THEN
                #retrona una secuencia vacia
                SELECT * FROM bt_menus where pk_codigo = 'none';
		    ELSE
                SELECT * FROM bt_menus WHERE pk_codigo
                        IN (
                            SELECT fk_menu_codigo FROM bt_roles_menus WHERE fk_rol_codigo = p_codigo
                            );

            END IF;

		ELSE
			SELECT * FROM bt_menus  WHERE pk_codigo
					 NOT IN (
						SELECT fk_menu_codigo FROM bt_roles_menus WHERE fk_rol_codigo = p_codigo
						);
        END IF;

    END
    $$
DELIMITER ;
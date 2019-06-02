    #Creamos las tablas de la base de datos
    DROP TABLE IF EXISTS menus_roles;
    DROP TABLE IF EXISTS permissions_roles;
    DROP TABLE IF EXISTS permissions;
    DROP TABLE IF EXISTS menus;
#--    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS roles;

 #   --- Creamos la tabla Roles
    CREATE TABLE roles(
        rol_code            VARCHAR(4)      NOT NULL            ,
        rol_name            VARCHAR(255)    NOT NULL    UNIQUE  ,
        rol_desc            VARCHAR(255)    NOT NULL            ,
        rol_state           VARCHAR(3)      NOT NULL            ,

        PRIMARY KEY (rol_code)
    );

    #--- Crear la tabla usuarios
#--    CREATE TABLE users(
#--        user_code           VARCHAR(8)      NOT NULL            ,
#--        rol_code            VARCHAR(4)                          ,
#--        user_name           VARCHAR(150)    NOT NULL    UNIQUE  ,
#--        user_email          VARCHAR(255)    NOT NULL    UNIQUE  ,
#--        user_password       VARCHAR(255)    NOT NULL            ,
#--        user_attempts       INT             NOT NULL            ,
#--        user_state          VARCHAR(3)      NOT NULL            ,
#--
#--        PRIMARY KEY (user_code),
#--        FOREIGN KEY (rol_code) REFERENCES roles(rol_code)
#--                             ON DELETE SET NULL
#--                             ON UPDATE CASCADE
#--    );

    # --- Creamos la tabla permisos
    CREATE TABLE permissions(
        permission_code      VARCHAR(4)     NOT NULL            ,
        permission_name      VARCHAR(100)   NOT NULL            ,
        permission_desc      VARCHAR(200)   NOT NULL            ,

        PRIMARY KEY(permission_code)
    );

    # --- creamos la tabla MENUS
    CREATE  TABLE menus(
        menu_code           VARCHAR(4)      NOT NULL            ,
        menu_padre_code     VARCHAR(4)                          ,
        menu_name           VARCHAR(150)    NOT NULL UNIQUE     ,
        menu_desc           VARCHAR(255)    NOT NULL            ,
        menu_state          VARCHAR(3)      NOT NULL            ,
        menu_url            VARCHAR(255)    NOT NULL UNIQUE     ,
        menu_icono          VARCHAR(50)                         ,

        PRIMARY KEY     (menu_code),
        FOREIGN KEY     (menu_padre_code)     REFERENCES menus(menu_code)
                            ON DELETE RESTRICT
                            ON UPDATE CASCADE
    );
    #--- Creamos la tabla MENUS-ROLES
        CREATE TABLE menus_roles(
            menu_rol_id           INT         NOT NULL  AUTO_INCREMENT,
            menu_code             VARCHAR(4)                          ,
            rol_code              VARCHAR(4)                          ,

            PRIMARY KEY (menu_rol_id)                                 ,
            FOREIGN KEY (rol_code) REFERENCES roles(rol_code)
                                    ON DELETE   CASCADE
                                    ON UPDATE   CASCADE               ,
            FOREIGN KEY (menu_code) REFERENCES menus(menu_code)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE

        );


    # -- Creamos la tabla Permisos de roles
    CREATE TABLE permissions_roles(
        permission_rol_id     INT           NOT NULL AUTO_INCREMENT,
        permission_code       VARCHAR(4)    NOT NULL,
        rol_code              VARCHAR(4)    NOT NULL,

        PRIMARY KEY(permission_rol_id),
        FOREIGN KEY (rol_code)    REFERENCES roles(rol_code)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
        FOREIGN KEY (permission_code) REFERENCES permissions(permission_code)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE
    );






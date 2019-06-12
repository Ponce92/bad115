    #Creamos las tablas de la base de datos
    DROP TABLE IF EXISTS menus_roles;
    DROP TABLE IF EXISTS permissions_roles;
    DROP TABLE IF EXISTS permissions;
    DROP TABLE IF EXISTS menus;

#--    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS roles;

 #   --- Creamos la tabla Roles
    CREATE TABLE bt_roles(
        pk_codigo           VARCHAR(8)      NOT NULL            ,
        ct_nombre           VARCHAR(255)    NOT NULL    UNIQUE  ,
        ct_descrpcion       VARCHAR(255)    NOT NULL            ,
        cl_estado           BOOLEAN         NOT NULL            ,
        cl_editable         BOOLEAN         NOT NULL            ,

        PRIMARY KEY (pk_codigo)
    );


    # ----------------------------- Creamos la tabla permisos
    CREATE TABLE bt_permisos(
        pk_codigo           VARCHAR(8)     NOT NULL            ,
        ct_nombre           VARCHAR(100)   NOT NULL  UNIQUE    ,
        cd_descripcion      VARCHAR(200)   NOT NULL            ,

        PRIMARY KEY(pk_codigo)
    );

    # --- creamos la tabla MENUS
    CREATE  TABLE bt_menus(
        pk_codigo           VARCHAR(4)      NOT NULL            ,
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
            CREATE TABLE bt_roles_menus(
                pk_id           INT         NOT NULL  AUTO_INCREMENT,
                fk_rol_codigo   VARCHAR(8)                          ,
                fk_menu_codigo  VARCHAR(8)                          ,

                PRIMARY KEY (pk_id)                                 ,
                FOREIGN KEY (fk_rol_codigo) REFERENCES bt_roles(pk_codigo)
                                        ON DELETE   CASCADE
                                        ON UPDATE   CASCADE               ,
                FOREIGN KEY (fk_menu_codigo) REFERENCES bt_menus(pk_codigo)
                                        ON DELETE CASCADE
                                        ON UPDATE CASCADE

            );


    # -- Creamos la tabla Permisos de roles
    CREATE TABLE bt_roles_permisos(
        pk_id     INT       NOT NULL AUTO_INCREMENT,
        fk_rol_codigo       VARCHAR(8)    NOT NULL,
        fk_permiso_codigo   VARCHAR(8)    NOT NULL,

        PRIMARY KEY(pk_id),
        FOREIGN KEY (fk_rol_codigo)    REFERENCES bt_roles(pk_codigo)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
        FOREIGN KEY (fk_permiso_codigo) REFERENCES bt_permisos(pk_codigo)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE
    );






#insertamos valores en las tablas
TRUNCATE TABLE permissions_roles;
TRUNCATE TABLE menus_roles;
TRUNCATE TABLE users;
TRUNCATE TABLE menus;
TRUNCATE TABLE permissions;
TRUNCATE TABLE roles;

#--roles
INSERT INTO roles (rol_code,rol_name,rol_desc,rol_state) VALUES('ADIT','Administrador','Administrador de la aplicacion','ACT');
INSERT INTO roles (rol_code,rol_name,rol_desc,rol_state) VALUES('PRDR','Proveedor','Proveedor de instituciones de gobierno','ACT');
INSERT INTO roles (rol_code,rol_name,rol_desc,rol_state) VALUES('ADIN','admin Institucional','Administrador Institucional','ACT');
INSERT INTO roles (rol_code,rol_name,rol_desc,rol_state) VALUES('UACI','Jefe UACI','Jefe UACI de sistema','ACT');

## insertamos usuarios
    CALL user_insert_sp('PEAJ1900','Azael','azael','azael.ponce92@gmail.com','ADIT');
    CALL user_insert_sp('PPAJ1901','Ponce','ponce','azael@gmail.com','PRDR');
    CALL user_insert_sp('RREE1902','Roque','roque','ponce92@gmail.com','ADIN');
    CALL user_insert_sp('DFRE1903','Bad','bad','correo@gmail.com','UACI');


    ##insertamos permisos

        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CCUS','can_create_user','Puede crear usuarios');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CEUS','can_edit_user','Puede editar usuarios');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CRUS','can_read_user','Puede leer usuarios');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CDUS','can_delete_user','Puede eliminar usuarios');

        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CCRL','can_create_roles','Puede crear roles');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CERL','can_edit_roles','Puede editar roles');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CRRL','can_read_roles','Puede ver roles');
        INSERT INTO permissions (permission_code,permission_name,permission_desc) VALUES ('CDRL','can_delete_roles','Puede eliminar roles');


    ##Insertar en tabla MENUS
    INSERT INTO menus (menu_code,menu_padre_code,menu_name,menu_desc,menu_state,menu_url,menu_icono)
           VALUES('MNSS',null,'Sistema','Administracion del sistema ','ACT','/home/','icon-screen-desktop');

    INSERT INTO menus (menu_code,menu_padre_code,menu_name,menu_desc,menu_state,menu_url,menu_icono)
           VALUES('MNGR','MNSS','Roles','Gesion de roles del sistema','ACT','/home/roles/','icon-grid');

    INSERT INTO menus (menu_code,menu_padre_code,menu_name,menu_desc,menu_state,menu_url,menu_icono)
           VALUES('MNGU','MNSS','Usuarios','Gesion de usuarios del sistema','ACT','/home/usuarios/','icon-people');


    ##-----------Tabla ROLES-MENU

    INSERT INTO menus_roles(menu_code,rol_code) VALUES ('MNSS','ADIT');
    INSERT INTO menus_roles(menu_code,rol_code) VALUES ('MNGR','ADIT');
    INSERT INTO menus_roles(menu_code,rol_code) VALUES ('MNGU','ADIT');

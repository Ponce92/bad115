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

#--------------------------- insersiones de la tabla Permisos
        #roles
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PCRL', 'puede_crear_roles', 'Puede crear un rol');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PBRL', 'puede_borar_roles', 'Puede borrar los roles ( si es posible)');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PERL', 'puede_editar_roles', 'Puede editar los roles');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PRRL', 'puede_leer_roles', 'Puede leer roles existentes');
        #usuarios
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PCUS', 'puede_crear_usuarios', 'Puede crear un nuevo usuario');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PEUS', 'puede_eliminar_usuarios', 'Puede borrar usuarios existentes');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PAUS', 'puede_actualizar_usuarios', 'Puede actualizar un usuario existente ');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PLUS', 'Puede  roles', 'Puede leer usuarios');
        #Roles y permisos
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PLPR', 'puede_leer_permisos_rol', 'Puede leer los permisos del rol');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PEPR', 'puede_eliminar_permisos_rol', 'Puede eliminar un permisos de roles');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PAPR', 'puede_agregar_permisos_rol', 'Puede agregar permisos a roles');
        #Roles y menus
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PLRM', 'puede_leer_menus_rol', 'Puede leer los menus asociados a un roles');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PERM', 'puede_eliminar_menus_rol', 'Puede eliminar un menus asociados  a los roles');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PARM', 'puede_agregar_menus_rol', 'Puede agregar menus asociados a un roles');
        #Catalogo productos
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PLEQ', 'puede_leer_equipo', 'Puede leer catalogo de equipo');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PEEQ', 'puede_eliminar_equipo', 'Puede eliminar  euipo electrico');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PCEQ', 'puede_agregar_equipo', 'Puede agregar equipo electrico');
INSERT INTO bt_permisos (pk_codigo, ct_nombre, cd_descripcion) VALUES ('PAEQ', 'puede_actualizar_equipo', 'Puede actualizar un equipo');





    --- Nombre del proyecto: ElectroLab
    --- Empresa dedicada a la reparación de todo tipo de dispositivos electrónicos.

    --- Enlace al video de muestra:     https://youtu.be/FimwlkVvYIw

    --- Este proyecto tiene como funcionalidad tener un listado de los clientes, técnicos y ordenes de trabajo que tiene la empresa.
        A estos modelos se puede acceder siempre y cuando el usuario registrado tenga los permisos correspondientes.
        También tiene un apartado de compra / venta, en donde hay un listado al cual solo los usuarios registrados pueden acceder.

    --- Los modelos en este sitio son 4:    - Cliente
                                            - Tecnico
                                            - Publicacion
                                            - Trabajo

    --- Hay 3 tipos de usuarios :   - Admins
                                    - Tecnicos
                                    - Usuarios "comunes"

        - Usuarios Admins: Tienen acceso a todo el sitio y a todas las funcionalidades de cada uno de los modelos (Crear, Leer, Editar, Borrar)

        - Usuarios Tecnicos: Tienen acceso solo a los modelos Trabajo (Crear, Leer, Editar, Borrar) y Publicacion (compra / venta) (Crear, Leer)

        - Usuarios "comunes" (default): Tienen acceso solo al modelo Publicacion (compra / venta) (Crear, Leer).
                                        También pueden acceder al apartado Seguimiento, en donde pueden buscar con el nro de OT y ver en
                                        que estado esta el dispositivo que dejó para reparar.

    --- Cuando se registra un usuario nuevo, por default, es un usuario "común".
    --- Mediante el panel de administración de django se puede colocar en el grupo Admins o Tecnicos y asi poder tener los permisos necesarios
        para operar en el sitio
    
    --- Cuando inicia sesión la aplicación reconoce que tipo de usuario es y lo redirige al "home" que corresponde, segun el tipo de usuario




-- USUARIOS REGISTRADOS:
    
    - Usuarios "comunes":
        Usuario: Ricardo
        Contraseña: rdj12345

        Usuario: Roberto
        Contraseña: rober12345

    - Admins:
        Usuario: admin_1
        Contraseña: ElectroLab

        Usuario: admin_2
        Contraseña: ElectroLab

    - Tecnicos:
        Usuario: Tecnico1
        Contraseña: 12345tec1

        Usuario: Tecnico2
        Contraseña: 12345tec2



-- USUARIO PANEL DE ADMINISTRACION django:
    Usuario: admin_1
    Contraseña: ElectroLab
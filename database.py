import sqlite3

# Crear o conectar a la base de datos
conn = sqlite3.connect('mascotas.db')
c = conn.cursor()

# Crear tabla de usuario
c.execute('''CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT,
            apellido_usuario TEXT,
            correo_usuario TEXT,
            contrasena TEXT,
            direccion_usuario TEXT,
            edad_usuario INTEGER,
            ciudad_usuario TEXT,
            fono_usuario INTEGER)''')

# Crear tabla de publicacion
c.execute('''CREATE TABLE IF NOT EXISTS publicacion (
            id_publicacion INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            id_mascota INTEGER,
            estado TEXT,
            fecha_publicacion TEXT,
            descripcion TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
            FOREIGN KEY (id_mascota) REFERENCES mascota (id_mascota))''')

# Crear tabla de mascota
c.execute('''CREATE TABLE IF NOT EXISTS mascota (
            id_mascota INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            especie TEXT,
            raza TEXT,
            descripcion TEXT,
            ubicacion TEXT,
            estado TEXT,
            fecha_registro TEXT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario))''')

# Crear tabla de mensaje
c.execute('''CREATE TABLE IF NOT EXISTS mensaje (
            id_mensaje INTEGER PRIMARY KEY AUTOINCREMENT,
            id_remitente INTEGER,
            id_destinatario INTEGER,
            id_publicacion INTEGER,
            fecha_envio TEXT,
            FOREIGN KEY (id_remitente) REFERENCES usuario (id_usuario),
            FOREIGN KEY (id_destinatario) REFERENCES usuario (id_usuario),
            FOREIGN KEY (id_publicacion) REFERENCES publicacion (id_publicacion))''')

conn.commit()
conn.close()

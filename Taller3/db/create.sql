CREATE TABLE tipo_sensores (
    referencia VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR (200) NOT NULL,
    variable VARCHAR (100) NOT NULL,
    precio INTEGER(10),
    salida VARCHAR(100),
    imagen VARCHAR (200)
)
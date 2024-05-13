# constantes
CONFIG_FILE = "config.ini"
BACKUP_FILE = 'backup_db.sql'
TABLE_CATEGORIA = """
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL);"""
TABLE_PRODUCTO = """
CREATE TABLE IF NOT EXISTS Producto (
    id_producto SERIAL PRIMARY KEY,
    categoria INT REFERENCES Categoria(id_categoria),
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad_stock INT NOT NULL);"""
TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion TEXT NOT NULL,
    no_celular BIGINT NOT NULL);"""
TABLE_FACTURA_VENTA = """
CREATE TABLE IF NOT EXISTS Factura_Venta (
    folio_venta SERIAL PRIMARY KEY,
    cliente INT REFERENCES Cliente(id_cliente),
    fecha DATE NOT NULL);"""
TABLE_DETALLE_F_VENTA = """
CREATE TABLE IF NOT EXISTS Detalle_F_Venta (
    id_detalle SERIAL PRIMARY KEY,
    folio_venta INT REFERENCES Factura_Venta(folio_venta),
    producto INT REFERENCES Producto(id_producto),
    cantidad INT NOT NULL,
    precio_venta DECIMAL(10, 2) NOT NULL,
    ingreso_total DECIMAL(10, 2));"""
TABLE_PROVEEDOR = """
CREATE TABLE IF NOT EXISTS Proveedor (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_negocio VARCHAR(50) NOT NULL,
    nombre_contacto VARCHAR(50) NOT NULL,
    direccion TEXT NOT NULL,
    no_celular BIGINT NOT NULL);"""
TABLE_FACTURA_COMPRA = """
CREATE TABLE IF NOT EXISTS Factura_Compra (
    folio_compra SERIAL PRIMARY KEY,
    proveedor INT REFERENCES Proveedor(id_proveedor),
    fecha DATE NOT NULL);"""
TABLE_DETALLE_F_COMPRA = """
CREATE TABLE IF NOT EXISTS Detalle_F_Compra (
    id_detalle SERIAL PRIMARY KEY,
    folio_compra INT REFERENCES Factura_Compra(folio_compra),
    producto INT REFERENCES Producto(id_producto),
    cantidad INT NOT NULL,
    precio_compra DECIMAL(10,2) NOT NULL,
    gasto_total DECIMAL(10,2));"""
productos = {}

def agregar_producto(codigo, descripcion, stock, precio, fecha_vencimiento, tipo):
    producto = [descripcion, stock, precio, fecha_vencimiento, tipo]
    productos[codigo] = producto

def eliminar_producto(codigo):
    if codigo in productos:
        del productos[codigo]
        print("Producto eliminado.")
    else:
        print("El producto no existe.")


def listar_productos():
    for codigo, producto in productos.items():
        descripcion, stock, precio, fecha_vencimiento, tipo = producto
        print("Código: ", codigo)
        print("Descripción: ", descripcion)
        print("Stock: ", stock)
        print("Precio: ", precio)
        print("Fecha de vencimiento: ", fecha_vencimiento)
        print("Tipo: ", tipo)
        print("--------------------")

def vender_producto(nombre, cantidad):
    encontrado = False
    for codigo, producto in productos.items():
        descripcion, stock, precio, fecha_vencimiento, tipo = producto
        if descripcion.lower() == nombre.lower():
            encontrado = True
            if cantidad <= stock:
                stock -= cantidad
                productos[codigo] = [descripcion, stock, precio, fecha_vencimiento, tipo]
                print(f"Venta realizada de {cantidad} unidad(es) de {nombre}. Stock actualizado.")
            else:
                print("No hay suficiente stock para realizar la venta.")
            break

    if not encontrado:
        print("El producto no existe.")
def proceso_venta_automatico():
    num_ventas = 5

    ventas = [
        ("Leche", 5),
        ("Pan", 10),
        ("Harina", 5),
        ("Huevos", 3),
        ("Palta", 4),
    ]

    for i in range(num_ventas):
        
        nombre, cantidad = ventas[i % len(ventas)]
        
        
        vender_producto(nombre, cantidad)

        
        print("\n====================\n")

        
        listar_productos()

agregar_producto("001", "Leche", 50, 3.5, "2023-07-31", "L")
agregar_producto("002", "Pan", 150, 4.0, "2023-07-20", "V")
agregar_producto("003", "Harina", 110, 9.0, "2023-07-31", "V")
agregar_producto("004", "Huevos", 30, 8.0, "2023-07-28", "V")
agregar_producto("005", "Palta", 60, 6.0, "2023-07-14", "V")

proceso_venta_automatico()

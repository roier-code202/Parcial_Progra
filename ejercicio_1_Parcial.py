class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad

    def reducir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            return False


class Proveedor:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos  

# Lista de los productos que el proveedor maneja

    def surtir_tienda(self, tienda, producto_nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == producto_nombre:
                tienda.recibir_producto(producto, cantidad)
                return f"Proveedor {self.nombre} surtió {cantidad} unidades de {producto_nombre}."
        return f"Producto {producto_nombre} no encontrado en el proveedor {self.nombre}."


class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre

    def comprar(self, tienda, compras):
        recibo = []
        total = 0
        total_dinero = 0
        for producto_nombre, (cantidad, dinero) in compras.items():
            precio = tienda.vender_producto(producto_nombre, cantidad)
            if precio is None:
                recibo.append(f"Producto {producto_nombre} no disponible o cantidad insuficiente.")
                continue
            total += precio
            cambio = dinero - precio
            total_dinero += dinero
            if cambio < 0:
                recibo.append(f"Falta dinero para {producto_nombre}.")
            else:
                recibo.append(f"Producto: {producto_nombre}, Cantidad: {cantidad}, Total: ${precio:.2f}, Dinero: ${dinero:.2f}, Cambio: ${cambio:.2f}")
        recibo.append(f"\nTotal compra: ${total:.2f}, Dinero entregado: ${total_dinero:.2f}, Vuelto total: ${total_dinero - total:.2f}")
        return "\n".join(recibo)

    def elegir_productos(self, tienda):
        compras = {}
        print("Elige los productos que deseas comprar (escribe 'salir' para terminar):")
        while True:
            print("\nInventario actual:")
            print(tienda.mostrar_inventario())
            producto_nombre = input("Producto: ").strip()
            if producto_nombre.lower() == 'salir':
                break
            if producto_nombre not in tienda.productos:
                print("Producto no disponible.")
                continue
            try:
                cantidad = int(input(f"Cantidad de {producto_nombre}: ").strip())
                dinero = float(input(f"Dinero entregado para {producto_nombre} (por {cantidad} unidades): ").strip())
                compras[producto_nombre] = (cantidad, dinero)
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número válido para la cantidad y el dinero.")
                continue
        return compras


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}  

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].agregar_stock(producto.cantidad)
        else:
            self.productos[producto.nombre] = producto

    def recibir_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].agregar_stock(cantidad)
        else:
            self.productos[producto.nombre] = Producto(producto.nombre, cantidad, producto.precio)

    def vender_producto(self, producto_nombre, cantidad):
        if producto_nombre in self.productos:
            producto = self.productos[producto_nombre]
            if producto.reducir_stock(cantidad):
                return producto.precio * cantidad
        return None

    def mostrar_inventario(self):
        return "\n".join([str(p) for p in self.productos.values()])


# Productos del proveedor actual
prod1 = Producto("Leche", 100, 1.20)
prod2 = Producto("Pan", 200, 0.80)
prod2 = Producto("Cafe", 50, 1.80)
prod2 = Producto("Arroz", 320, 2.00)


# Proveedor
proveedor = Proveedor("Proveedor1", [prod1, prod2])

# Tienda
tienda = Tienda("Tienda Local")


print(proveedor.surtir_tienda(tienda, "Leche", 50))
print(proveedor.surtir_tienda(tienda, "Pan", 150))


print("Inventario después de surtir:")
print(tienda.mostrar_inventario())


cliente = Cliente("Juan")
compras = cliente.elegir_productos(tienda)
if compras:  
    print(cliente.comprar(tienda, compras))


print("Inventario después de la compra:")
print(tienda.mostrar_inventario())

# Basandose en el problema principal, se creo un programa para que el usuario seleccione el producto que desea comprar,
# eligiendo la cantidad que va a comprar y la cantidad de dinero que entregara para el pago, ya con los datos anteriores
# el programa calculara el total que debera de dar de cambio y mostrara los datos que se han seleccionado 

class Hotel:
    def __init__(self):
        self.habitaciones = {
            "Simple": 50,
            "Doble": 80,
            "Suite": 120
        }
        self.servicios_extra = {
            "Piscina": 10,
            "Cancha de golf": 20
        }

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for tipo, precio in self.habitaciones.items():
            print(f"- {tipo}: ${precio} por noche")

    def realizar_reserva(self):
        self.mostrar_habitaciones()
        tipo_habitacion = input("Elija el tipo de habitación: ")
        precio_noche = self.habitaciones.get(tipo_habitacion, 0)
        if precio_noche == 0:
            print("Tipo de habitación no válido.")
            return

        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        noches = int(input("Ingrese el número de noches: "))

        # Servicios extra
        servicios = []
        while True:
            servicio = input("¿Desea algún servicio extra? (s/n): ")
            if servicio.lower() == 'n':
                break
            servicio = input("Ingrese el servicio: ")
            if servicio in self.servicios_extra:
                servicios.append(servicio)
            else:
                print("Servicio no disponible.")

        self.generar_factura(nombre, apellidos, tipo_habitacion, noches, servicios)

    def generar_factura(self, nombre, apellidos, tipo_habitacion, noches, servicios):
        total = self.habitaciones[tipo_habitacion] * noches
        for servicio in servicios:
            total += self.servicios_extra[servicio]

        print("\n--- Factura ---")
        print(f"Nombre: {nombre} {apellidos}")
        print(f"Habitación: {tipo_habitacion}")
        print(f"Noches: {noches}")
        print("Servicios extra:")
        for servicio in servicios:
            print(f"- {servicio}")
        print(f"Total: ${total}")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.realizar_reserva()

# Basandose en el problema, se creo un programa para que el cliente seleccione lo que necesita y al terminar de seleccionar lo que
# necesita, el programa mostrara el resultado de lo que ha seleccionado y el total que tendra que pagar


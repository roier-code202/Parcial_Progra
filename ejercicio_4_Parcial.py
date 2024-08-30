class Empleado:
    def __init__(self, nombre, años_laborados):
        self.nombre = nombre
        self.años_laborados = años_laborados

    def calcular_bono(self):
        # Bono adicional si ha trabajado más de 5 años
        if self.años_laborados > 5:
            return 500  # Bono fijo por más de 5 años
        return 0

    def calcular_sueldo(self):
        raise NotImplementedError("Debe implementar el método calcular_sueldo en las subclases")

class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, años_laborados, salario_base, comisiones):
        super().__init__(nombre, años_laborados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_sueldo(self):
        # Sueldo base más comisiones
        return self.salario_base + self.comisiones + self.calcular_bono()

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, años_laborados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, años_laborados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_sueldo(self):
        # Sueldo basado en horas trabajadas
        return (self.horas_trabajadas * self.tarifa_por_hora) + self.calcular_bono()

def ingresar_datos_empleados():
    empleados = []
    while True:
        tipo_empleado = input("Ingrese el tipo de empleado (plaza fija/por horas): ").strip().lower()
        nombre = input("Ingrese el nombre del empleado: ").strip()
        años_laborados = int(input("Ingrese los años laborados: "))
        
        if tipo_empleado == "plaza fija":
            salario_base = float(input("Ingrese el salario base: "))
            comisiones = float(input("Ingrese las comisiones: "))
            empleado = EmpleadoPlazaFija(nombre, años_laborados, salario_base, comisiones)
        elif tipo_empleado == "por horas":
            horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
            empleado = EmpleadoPorHoras(nombre, años_laborados, horas_trabajadas, tarifa_por_hora)
        else:
            print("Tipo de empleado no válido. Intente de nuevo.")
            continue
        
        empleados.append(empleado)
        
        otra = input("¿Desea ingresar otro empleado? (sí/no): ").strip().lower()
        if otra != "sí":
            break
    
    return empleados

def main():
    empleados = ingresar_datos_empleados()
    
    total_sueldo = 0
    for empleado in empleados:
        sueldo = empleado.calcular_sueldo()
        total_sueldo += sueldo
        print(f"Sueldo de {empleado.nombre}: ${sueldo:.2f}")
    
    print(f"\nTotal de sueldos: ${total_sueldo:.2f}")

if __name__ == "__main__":
    main()

# Basandose en el problema, el programa solicita saber si el empleado que va a registrar es de plaza fija o si es por horas,
# seleccionara manualmente el bono si es el caso y luego mostrara el resultado si el empleado tiene o no el bono

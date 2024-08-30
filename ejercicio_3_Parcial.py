from datetime import datetime

class Estudiante:
    """
    Clase que representa a un estudiante. Cada estudiante tiene un nombre, un ID único,
    y un historial de asistencia.
    """
    
    def __init__(self, nombre, id_estudiante):
        """
        Inicializa un nuevo estudiante con un nombre y un ID.
        
        Args:
        nombre (str): Nombre del estudiante.
        id_estudiante (int): ID único del estudiante.
        """
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.asistencia = []  # Lista para almacenar registros de asistencia

    def registrar_asistencia(self, fecha, estado, motivo=None):
        """
        Registra la asistencia de un estudiante para una fecha específica.
        
        Args:
        fecha (str): Fecha de la asistencia en formato "YYYY-MM-DD".
        estado (str): Estado de la asistencia ("Presente", "Permiso", "Inasistencia").
        motivo (str, opcional): Motivo del permiso si el estado es "Permiso". Por defecto es None.
        """
        registro = {
            "fecha": fecha,
            "estado": estado,
            "motivo": motivo
        }
        self.asistencia.append(registro)

    def ver_historial_asistencia(self):
        """
        Devuelve el historial de asistencia del estudiante.
        
        Returns:
        list: Lista de registros de asistencia.
        """
        return self.asistencia


class Docente:
    """
    Clase que representa a un docente. El docente puede gestionar a los estudiantes
    y registrar su asistencia.
    """
    
    def __init__(self, nombre, id_docente):
        """
        Inicializa un nuevo docente con un nombre y un ID.
        
        Args:
        nombre (str): Nombre del docente.
        id_docente (int): ID único del docente.
        """
        self.nombre = nombre
        self.id_docente = id_docente
        self.estudiantes = []  # Lista para almacenar estudiantes registrados

    def agregar_estudiante(self, nombre, id_estudiante):
        """
        Agrega un nuevo estudiante a la lista de estudiantes del docente.
        
        Args:
        nombre (str): Nombre del estudiante.
        id_estudiante (int): ID único del estudiante.
        """
        nuevo_estudiante = Estudiante(nombre, id_estudiante)
        self.estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nombre} registrado exitosamente con ID {id_estudiante}.")

    def registrar_asistencia_estudiante(self, id_estudiante, fecha, estado, motivo=None):
        """
        Registra la asistencia de un estudiante por su ID.
        
        Args:
        id_estudiante (int): ID del estudiante.
        fecha (str): Fecha de la asistencia en formato "YYYY-MM-DD".
        estado (str): Estado de la asistencia ("Presente", "Permiso", "Inasistencia").
        motivo (str, opcional): Motivo del permiso si el estado es "Permiso". Por defecto es None.
        """
        # Busca al estudiante por ID
        estudiante = next((e for e in self.estudiantes if e.id_estudiante == id_estudiante), None)
        if estudiante:
            estudiante.registrar_asistencia(fecha, estado, motivo)
        else:
            print(f"Estudiante con ID {id_estudiante} no encontrado.")

    def generar_reporte_diario(self, fecha):
        """
        Genera un reporte diario de asistencia para una fecha específica.
        
        Args:
        fecha (str): Fecha para la cual se desea generar el reporte (formato "YYYY-MM-DD").
        
        Returns:
        list: Lista de diccionarios que contienen el reporte de cada estudiante.
        """
        reporte = []
        # Itera sobre los estudiantes y busca su asistencia para la fecha proporcionada
        for estudiante in self.estudiantes:
            asistencia = next((a for a in estudiante.asistencia if a["fecha"] == fecha), None)
            if asistencia:
                reporte.append({
                    "nombre": estudiante.nombre,
                    "id_estudiante": estudiante.id_estudiante,
                    "estado": asistencia["estado"],
                    "motivo": asistencia["motivo"]
                })
        return reporte

    def ver_estudiantes(self):
        """
        Muestra la lista de estudiantes registrados en la consola.
        """
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("Estudiantes registrados:")
            for estudiante in self.estudiantes:
                print(f"Nombre: {estudiante.nombre}, ID: {estudiante.id_estudiante}")


class Director:
    """
    Clase que representa al director de la escuela. El director puede revisar los reportes
    de asistencia generados por los docentes.
    """
    
    def __init__(self, nombre):
        """
        Inicializa un nuevo director con un nombre.
        
        Args:
        nombre (str): Nombre del director.
        """
        self.nombre = nombre

    def revisar_reporte(self, reporte):
        """
        Revisa el reporte diario de asistencia generado por el docente.
        
        Args:
        reporte (list): Lista de diccionarios que contienen los registros de asistencia
                        de los estudiantes para una fecha específica.
        """
        for registro in reporte:
            print(f"Estudiante: {registro['nombre']} (ID: {registro['id_estudiante']})")
            print(f"  Estado: {registro['estado']}")
            if registro['estado'] == 'Permiso':
                print(f"  Motivo del permiso: {registro['motivo']}")
            print("-" * 20)


# Funciones para interacción con el usuario
def registrar_nuevos_estudiantes(docente):
    """
    Permite al usuario agregar nuevos estudiantes a través del teclado.
    
    Args:
    docente (Docente): El docente que está registrando a los estudiantes.
    """
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            docente.agregar_estudiante(nombre, id_estudiante)
        except ValueError:
            print("Por favor, ingrese un ID válido.")

def registrar_asistencias(docente):
    """
    Permite al usuario registrar la asistencia de un estudiante a través del teclado.
    
    Args:
    docente (Docente): El docente que está registrando la asistencia de los estudiantes.
    """
    try:
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        id_estudiante = int(input("Ingrese el ID del estudiante para registrar asistencia: "))
        estado = input("Ingrese el estado del estudiante ('Presente', 'Permiso', 'Inasistencia'): ").capitalize()
        motivo = None
        if estado == "Permiso":
            motivo = input("Ingrese el motivo del permiso: ")

        docente.registrar_asistencia_estudiante(id_estudiante, fecha_hoy, estado, motivo)
    except ValueError:
        print("ID de estudiante no válido.")

def ver_historial(docente):
    """
    Permite al usuario ver el historial de asistencia de un estudiante específico.
    
    Args:
    docente (Docente): El docente que está consultando el historial de los estudiantes.
    """
    try:
        id_estudiante_historial = int(input("Ingrese el ID del estudiante para ver su historial de asistencia: "))
        estudiante = next((e for e in docente.estudiantes if e.id_estudiante == id_estudiante_historial), None)
        if estudiante:
            print("Historial de asistencia:")
            for registro in estudiante.ver_historial_asistencia():
                print(f"Fecha: {registro['fecha']}, Estado: {registro['estado']}, Motivo: {registro['motivo']}")
        else:
            print(f"Estudiante con ID {id_estudiante_historial} no encontrado.")
    except ValueError:
        print("ID no válido.")


def main():
    """
    Función principal del programa. Permite registrar nuevos estudiantes, registrar su
    asistencia, generar reportes diarios y consultar el historial de asistencia.
    """
    # Inicializa el docente
    docente = Docente("Prof. García", 100)

    # Registrar nuevos estudiantes
    registrar_nuevos_estudiantes(docente)

    # Mostrar lista de estudiantes registrados
    docente.ver_estudiantes()

    # Registrar asistencia
    registrar_asistencias(docente)

    # Generar reporte diario
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    reporte_diario = docente.generar_reporte_diario(fecha_hoy)
    director = Director("Sr. Rodríguez")
    director.revisar_reporte(reporte_diario)

    # Ver historial de un estudiante
    ver_historial(docente)


if __name__ == "__main__":
    main()

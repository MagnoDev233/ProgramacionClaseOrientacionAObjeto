
    app = Veterinaria()
    app.registrar_mascota("Fido", "Perro", 5)
    app.registrar_mascota("Misu", "Gato", 2)
    app.registrar_mascota("Kiwi", "Loro", 10)
    
    app.ejecutar()class Mascota:
    """Representa una mascota con sus atributos básicos."""
    def __init__(self, nombre: str, especie: str, edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        """Devuelve una representación legible de la mascota."""
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años"

class Veterinaria:
    """Gestiona el registro de mascotas y sus funcionalidades."""
    def __init__(self):
        self.registro = []

    def registrar_mascota(self, nombre: str, especie: str, edad: int) -> bool:
        """
        Registra una nueva mascota en el sistema.
        Devuelve True si se registró con éxito, False si ya existe un nombre o la edad es inválida.
        """
        try:
            edad_int = int(edad)
            if edad_int < 0:
                print("Error: La edad no puede ser negativa.")
                return False
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return False
            
        if any(m.nombre.lower() == nombre.lower() for m in self.registro):
             print(f"Error: Ya existe una mascota registrada con el nombre '{nombre}'.")
             return False
        
        nueva_mascota = Mascota(nombre, especie, edad_int)
        self.registro.append(nueva_mascota)
        print(f"Mascota '{nombre}' registrada con éxito.")
        return True

    def buscar_mascota_por_nombre(self, nombre_buscado: str):
        """Busca una mascota por su nombre (sin distinguir mayúsculas/minúsculas)."""
        for mascota in self.registro:
            if mascota.nombre.lower() == nombre_buscado.lower():
                return mascota
        return None

    def listar_todas_las_mascotas(self):
        """Muestra el listado completo de todas las mascotas registradas."""
        if not self.registro:
            print("\nEl registro de la veterinaria está vacío.")
            return
        
        print("\n--- Listado Completo de Mascotas ---")
        for i, mascota in enumerate(self.registro):
            print(f"{i+1}. {mascota}")
        print("------------------------------------\n")

    def obtener_edad_promedio(self) -> float:
        """Calcula y devuelve la edad promedio de todas las mascotas registradas."""
        if not self.registro:
            return 0.0

        suma_edades = sum(mascota.edad for mascota in self.registro)
        total_mascotas = len(self.registro)

        promedio = suma_edades / total_mascotas
        return promedio

    def mostrar_menu(self):
        """Muestra el menú de opciones al usuario."""
        print("\n=============================================")
        print("           SISTEMA DE VETERINARIA")
        print("=============================================")
        print("1. Registrar nueva mascota")
        print("2. Buscar mascota por nombre")
        print("3. Consultar listado completo")
        print("4. Obtener edad promedio")
        print("5. Salir")
        print("=============================================")

    def ejecutar(self):
        """Bucle principal de la aplicación."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre de la mascota: ")
                especie = input("Ingrese la especie de la mascota: ")
                edad = input("Ingrese la edad de la mascota (años): ")
                self.registrar_mascota(nombre, especie, edad)
            
            elif opcion == '2':
                nombre_buscado = input("Ingrese el nombre de la mascota a buscar: ")
                mascota = self.buscar_mascota_por_nombre(nombre_buscado)
                if mascota:
                    print(f"\nMascota '{nombre_buscado}' encontrada:")
                    print(f"   {mascota}")
                else:
                    print(f"\nLa mascota '{nombre_buscado}' no se encuentra registrada.")
            
            elif opcion == '3':
                self.listar_todas_las_mascotas()
            
            elif opcion == '4':
                promedio = self.obtener_edad_promedio()
                if self.registro:
                    print(f"\nLa edad promedio de las {len(self.registro)} mascotas registradas es: {promedio:.2f} años.")
                else:
                    print("\nNo hay mascotas registradas para calcular el promedio.")

            elif opcion == '5':
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            
            else:
                print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":

import os
from file_reader import FileReader

class Menu:
    def __init__(self):
        self.opciones = {
            "1": self.cargar_archivo,
            "2": self.exportar,
            "3": self.salir
        }
        self.df = None  # Inicializamos df como propiedad de la clase
    
    def mostrar_menu(self):
        print("\nMenú de Opciones:")
        print("1. Cargar archivo")
        print("2. Exportar archivo")
        print("3. Salir")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("❌ Opción no válida. Intente de nuevo.")
    


    def cargar_archivo(self):
        ruta = input("Ingrese la ruta del archivo: ")
        file_reader = FileReader(ruta)
        self.df = file_reader.read_file()  # Guardamos el DataFrame como propiedad

        if self.df is not None:
            print("✅ Archivo cargado exitosamente.")
        else:
            print("❌ Error al cargar el archivo.")
    




    def exportar(self):
        if self.df is None:  # Verifica si el df está cargado
            print("❌ Error: No se ha cargado un archivo. Primero cargue un archivo.")
            return


        # Preguntar al usuario el formato de exportación
        print("¿En qué formato deseas exportar el archivo?")
        print("1. CSV")
        print("2. XLSX")
        print("3. JSON")
        print("4. Base de datos")


        # ensuciar el archivo
        # poner en null las columnas: adults, children
        # en reservation_status_date, tomar cada fecha y ponerle un formato random, por ejemplo dd/mm/yyyy o dd-mm-yyyy
        # guardarlo como dirty.csv

        # normalizar el archivo
        # en los null de las columnas adults y children, ponerles como valor el promedio de todas las demas
        # en reservation_status_date normalizar las fechas con format dd/mm/yyyy
        # guardarlo como final.csv
        

        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            # Exportar a CSV
            archivo = input("Introduce el nombre del archivo CSV (sin extensión): ")
            self.df.to_csv(f"{archivo}.csv", index=False)
            print(f"Archivo exportado como {archivo}.csv")
        
        elif opcion == '2':
            # Exportar a XLSX
            archivo = input("Introduce el nombre del archivo XLSX (sin extensión): ")
            self.df.to_excel(f"{archivo}.xlsx", index=False)
            print(f"Archivo exportado como {archivo}.xlsx")
        
        elif opcion == '3':
            # Exportar a JSON
            archivo = input("Introduce el nombre del archivo JSON (sin extensión): ")
            self.df.to_json(f"{archivo}.json", orient="records", lines=True)
            print(f"Archivo exportado como {archivo}.json")
        
        elif opcion == '4':
            # YO HAGO ESTO saludos al mencho
            # Exportar a Base de datos (aquí necesitarías adaptar para tu base de datos)
            print("Exportar a base de datos aún no implementado.")
        
        else:
            print("❌ Opción inválida. Por favor, elige entre 1 y 4.")

        print("✅ Archivo exportado exitosamente.")






    def salir(self):
        print("🚪 Saliendo del programa...")
        exit()

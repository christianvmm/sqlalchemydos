import os
from file_reader import FileReader
from data_processor import DataProcessor

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

        # =========================================
        # Ensuciar el archivo
        # =========================================
        dirty_df = self.df.copy()
        
        # Poner valores NULL en algunas filas de las columnas: adults, children
        for col in ['adults', 'children']:
            if col in dirty_df.columns:
                dirty_df.loc[dirty_df.sample(frac=0.1).index, col] = None
        
        # En reservation_status_date, cambiar el formato de forma aleatoria
        if 'reservation_status_date' in dirty_df.columns:
            def random_date_format(date):
                formats = ["%d/%m/%Y", "%d-%m-%Y"]
                return pd.to_datetime(date).strftime(random.choice(formats))
            
            dirty_df['reservation_status_date'] = dirty_df['reservation_status_date'].apply(random_date_format)
        

        dirty_df.to_csv("dirty.csv", index=False)
        print("📂 Archivo sucio guardado como dirty.csv")



        # =========================================
        # Preguntar al usuario el formato de exportación
        # =========================================
        print("¿En qué formato deseas exportar el archivo?")
        print("1. CSV")
        print("2. XLSX")
        print("3. JSON")
        print("4. Base de datos")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            archivo = input("Introduce el nombre del archivo CSV (sin extensión): ")
            final_df.to_csv(f"{archivo}.csv", index=False)
            print(f"Archivo exportado como {archivo}.csv")
        
        elif opcion == '2':
            archivo = input("Introduce el nombre del archivo XLSX (sin extensión): ")
            final_df.to_excel(f"{archivo}.xlsx", index=False)
            print(f"Archivo exportado como {archivo}.xlsx")
        
        elif opcion == '3':
            archivo = input("Introduce el nombre del archivo JSON (sin extensión): ")
            final_df.to_json(f"{archivo}.json", orient="records", lines=True)
            print(f"Archivo exportado como {archivo}.json")
        
        elif opcion == '4':
            print("Exportar a base de datos aún no implementado.")
        
        else:
            print("❌ Opción inválida. Por favor, elige entre 1 y 4.")




        # =========================================
        # Normalizar el archivo
        # =========================================
        final_df = dirty_df.copy()
        
        # Reemplazar NULL con el promedio de cada columna en 'adults' y 'children'
        for col in ['adults', 'children']:
            if col in final_df.columns:
                final_df[col] = final_df[col].fillna(final_df[col].mean())
        
        # Normalizar las fechas en 'reservation_status_date' al formato dd/mm/yyyy
        if 'reservation_status_date' in final_df.columns:
            final_df['reservation_status_date'] = pd.to_datetime(final_df['reservation_status_date'], dayfirst=True).dt.strftime('%d/%m/%Y')
        


        # =========================================
        # guardarlo como csv, xlsx, json o meterlo a la base de datos dependiendo de lo que eligieron los putos
        # =========================================
        final_df.to_csv("final.csv", index=False)

        print("✅ Archivo exportado exitosamente.")



    def salir(self):
        print("🚪 Saliendo del programa...")
        exit()

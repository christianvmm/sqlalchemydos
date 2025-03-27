import pandas as pd
import os

class FileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_file_extension(self):
        """Obtiene y retorna la extensión del archivo en minúsculas."""
        return os.path.splitext(self.file_path)[1].lower()

    def read_file(self):
        """Lee un archivo CSV, XLSX o JSON y lo devuelve como un DataFrame."""
        if not os.path.exists(self.file_path):
            print(f"Error: El archivo '{self.file_path}' no existe.")
            return None

        try:
            ext = self._get_file_extension()

            if ext == ".csv":
                df = pd.read_csv(self.file_path)
            elif ext in [".xls", ".xlsx"]:
                df = pd.read_excel(self.file_path)
            elif ext == ".json":
                df = pd.read_json(self.file_path)
            else:
                print(f"Error: Formato de archivo '{ext}' no soportado.")
                return None
            
            print(f"Archivo '{self.file_path}' cargado correctamente.")
            return df

        except pd.errors.EmptyDataError:
            print(f"Error: El archivo '{self.file_path}' está vacío.")
        except pd.errors.ParserError:
            print(f"Error: Hubo un problema al parsear el archivo '{self.file_path}'.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        return None  # Retorna None en caso de error
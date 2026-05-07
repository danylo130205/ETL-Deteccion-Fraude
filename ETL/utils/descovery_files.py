import os
from ETL.utils.logger import get_logger
lg = get_logger()
def discover_files(path:str) -> dict:
    try:
        lg.info(f"Descubriendo archivos en {path}")
        files = {}
        for root, dirs, file_list in os.walk(path):
            for file in file_list:
                if file.endswith(".csv"):
                    fil= os.path.join(root, file)
                    files[file] = fil
        lg.info(f"Archivos descubiertos: {list(files.keys())}")
        return files
    except Exception as e:
        raise ValueError(f"Error al descubrir archivos: {e}")
    
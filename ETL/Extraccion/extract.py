import pandas as pd
from ETL.utils.logger import get_logger
lg = get_logger()
def extract(files:dict) -> list[pd.DataFrame]:
    try:
        lg.info("Iniciando extracción")
        df = []
        file = {}
        for file_name, file_path in files.items():
            data = pd.read_csv(file_path, index_col=0)
            file[file_name] = data 
            
            lg.info(f"Extracción exitosa de {file_name}")
        df.append(file)
        return df
    except Exception as e:
        raise ValueError(f"Error al extraer datos: {e}")
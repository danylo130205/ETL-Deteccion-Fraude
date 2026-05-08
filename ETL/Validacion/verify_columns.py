import pandas as pd
from ETL.utils.logger import get_logger
import ETL.utils.config as config
lg = get_logger()
def verify_columns(df:list[dict[str,pd.DataFrame]]) -> list[dict[str,pd.DataFrame]]:
    try:
        lg.info("Iniciando verificación de columnas")
        for data in df:
            missing_columns = []
            for file_name , dataF in data.items():
                for col in config.COLUMNS_TO_KEEP:
                    if col not in dataF.columns:
                        missing_columns.append(col)
                if missing_columns:
                    raise ValueError(f"Faltan columnas: {list(missing_columns)} en el DataFrame {file_name}")
                lg.info(f"Verificación de columnas exitosa en {file_name}")
        lg.info("Verificación de columnas exitosa")
        return df
    except Exception as e:
        raise ValueError(f"Error en la verificación de columnas: {e}")
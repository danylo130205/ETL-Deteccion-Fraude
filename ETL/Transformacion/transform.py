import pandas as pd
from ETL.utils.logger import get_logger
from ETL.Transformacion.delete import delete
from ETL.Transformacion.standardize import standardize
from ETL.Transformacion.adding import adding
lg = get_logger()
def transform(df:list[dict[str,pd.DataFrame]]) -> list[dict[str,pd.DataFrame]]:
    try:
        lg.info("Iniciando transformación")
        #Eliminar
        df_T = []
        df_T = delete(df)
        #Estandarizar
        df_T = standardize(df_T)
        #Agregando
        df_T = adding(df_T)
        lg.info("Transformación exitosa")
        return df_T
    except Exception as e:
        raise ValueError(f"Error al transformar datos: {e}")
import pandas as pd
from ETL.utils.logger import get_logger
import ETL.utils.config as config
lg = get_logger()
def delete(df:list[dict[str,pd.DataFrame]]) -> list[dict[str,pd.DataFrame]]:
    try:
        lg.info("Iniciando a eliminar columnas")
        df_deleted = []
        dct_deleted = {}
        delete_column = []
        for data in df:
            for file_name, datF in data.items():
                for col in datF.columns:
                    if col not in config.COLUMNS_TO_KEEP:
                        delete_column.append(col)
                lg.info(f"{file_name}:Columns eliminadas {list(delete_column)}")
                cleaned_df = datF.drop(columns=delete_column)
                dct_deleted[file_name] = cleaned_df
                delete_column.clear()
        df_deleted.append(dct_deleted)
        lg.info("Eliminación exitosa de columnas")
        return df_deleted
    except Exception as e:
        raise ValueError(f"Error al transformar datos: {e}")
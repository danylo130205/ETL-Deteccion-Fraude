import pandas as pd
from ETL.utils.logger import get_logger
lg = get_logger()
def standardize(df:list[dict[str,pd.DataFrame]]) -> list[dict[str,pd.DataFrame]]:
    try:
        lg.info("Iniciando estandarización")
        df_standardized = []
        dct_standardized = {}
        for data in df:
            for file_name, datF in data.items():
                #Estandarizar nombres de columnas
                datF.columns = datF.columns.str.strip().str.lower().str.replace(" ","_")
                #fechas
                colum_fechas = datF.filter(like="date").columns
                for col in colum_fechas:
                    datF[col] = pd.to_datetime(datF[col], errors="coerce")
                dct_standardized[file_name]=datF
                lg.info(f"{file_name}: Estandarización correcta de las columnas {datF.columns}")
                
        df_standardized.append(dct_standardized)
        lg.info("Estandarización exitosa")
        return df_standardized
    except Exception as e:
        raise ValueError(f"Error al estandarizar datos: {e}")
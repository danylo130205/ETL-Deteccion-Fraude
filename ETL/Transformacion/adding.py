import pandas as pd
from ETL.utils.logger import get_logger
lg = get_logger()
def adding(df:list[dict[str,pd.DataFrame]]) -> list[dict[str,pd.DataFrame]]:
    try:
        lg.info("Iniciando agregación de columnas")
        df_added = []
        dict_added = {}
        for data in df:
            for file_name, datF in data.items():
                #Agregar columna de año
                datF["year"] = datF["trans_date_trans_time"].dt.year
                #Agregar columna de mes
                datF["month"] = datF["trans_date_trans_time"].dt.month
                #Agregar columna de día de semana
                datF["day"] = datF["trans_date_trans_time"].dt.dayofweek
                #Agregar colman de día del mes
                datF["day_month"] = datF["trans_date_trans_time"].dt.day
                #Agregar columna de hora
                datF["hour"] = datF["trans_date_trans_time"].dt.hour
                #Agregar bolleano de transacciones nocturnas
                datF["is_night"] = datF["hour"].apply(lambda x: 1 if x >= 22 or x < 6 else 0)
                # Convertimos a datetime y extraemos solo la fecha
                datF["trans_date"] = pd.to_datetime(datF["trans_date_trans_time"]).dt.date
                dict_added[file_name] = datF
                lg.info(f"{file_name}: Agregación de columnas correcta")
        df_added.append(dict_added)
        lg.info("Agregación de columnas exitosa")
        return df_added
    except Exception as e:
        raise ValueError(f"Error al agregar columnas: {e}")
import pandas as pd
from ETL.utils.logger import get_logger
from ETL.utils.config import destino
lg = get_logger()
def load(df : list[dict[str,pd.DataFrame]]) -> None:
    try:
        lg.info("Iniciando carga de datos")
        for data in df:
            for file_name, datF in data.items():
                destino_path = f"{destino}/{file_name}"
                datF.to_csv(destino_path, index=False)
                lg.info(f"{file_name}: Carga exitosa en formato CSV")
        lg.info("Carga de datos exitosa")
    except Exception as e:
        raise ValueError(f"Error al cargar datos: {e}")
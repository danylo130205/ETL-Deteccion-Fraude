from ETL.utils.logger import get_logger
import pandas as pd
from ETL.utils.descovery_files import discover_files
import ETL.utils.config as config
from ETL.Extraccion.extract import extract
from ETL.Validacion.verify_columns import verify_columns
from ETL.Transformacion.transform import transform
from ETL.Carga.load import load
lg = get_logger()
def main():
    try:
        lg.info("-------------------------------------------")
        lg.info("Iniciando PIPELINE")
        #Descubriendo archivos en la carpeta de origen
        files = discover_files(config.DATA_CONFIG["raw_path"])
        #Extrayendo los datos de los archivos descubiertos
        df = extract(files)
        #Verificacion de columnas 
        df = verify_columns(df)
        #Transformación de los datos
        df = transform(df)
        #Caga de datos
        load(df)

        lg.info("PIPELINE finalizado exitosamente")
    except Exception as e:
        raise ValueError(f"Error en el PIPELINE {e}")
    
if __name__ == "__main__":
    main()
    
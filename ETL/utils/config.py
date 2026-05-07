import os
ubicacion = os.path.dirname(__file__)
ub_etl = os.path.dirname(ubicacion)
ub_raiz = os.path.dirname(ub_etl)
destino = os.path.join(ub_raiz, "Data","processed")
origenes = os.path.join(ub_raiz, "Data","raw")
DATA_CONFIG = {
    "raw_path": origenes,
    "file_pattern": "*.csv",
    "domain_strategy": "filename_suffix"
}
COLUMNS_TO_KEEP = [
    "trans_date_trans_time",
    "cc_num",
    "merchant",
    "category",
    "amt",
    "lat",
    "long",
    "city_pop",
    "dob",
    "trans_num",
    "unix_time",
    "merch_lat",
    "merch_long",
    "is_fraud"
]
destino = os.path.join(destino)
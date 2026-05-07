import os
import logging as lg
def get_logger():
    ubicacion = os.path.dirname(__file__)
    ub_etl = os.path.dirname(ubicacion)
    ub_raiz = os.path.dirname(ub_etl)
    ud_destino = os.path.join(ub_raiz,"logs")
    if not os.path.exists(ud_destino):
        os.mkdir(ud_destino)
    logger = lg.getLogger("etl")
    logger.setLevel(lg.INFO)
    log_destino = os.path.join(ud_destino,"etl.log")
    if not logger.handlers:
        handler = lg.FileHandler(log_destino)
        format = lg.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(format)
        logger.addHandler(handler)
    return logger
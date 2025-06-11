#\\MÓDULOS DE UTILIDADE//#

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def obter_logger(nome):
    return logging.getLogger(nome)

def safe_int(valor, default=None):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return default

def safe_float(valor, default=None):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return default

def e_valido(campo):
    return campo not in [None, '', 'N/A']

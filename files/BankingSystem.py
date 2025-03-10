import os # Operational System
import re # RegEx
from datetime import datetime # Data

# Funçao para Data em formato xx/xx/xxxx
def data_formatada(data):
    return data.strftime('%d/%m/%Y')

# Validando formato de data inserida
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False # Returning False if input the wrong date format

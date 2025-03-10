import os # Operational System
import re # RegEx
from datetime import datetime # Data

# Funçao para Data em formato xx/xx/xxxx
def data_formatada(data):
    return data.strftime('%d/%m/%Y')

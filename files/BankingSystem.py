import os # Operational System
import re # RegEx
from datetime import datetime # Data
import time # Wait for clean terminal


# Clean the terminal
def cleanTerminal():
    # Verifica o sistema operacional e limpa a tela
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

# Clean the lines
def clean_lines():
    # Move o cursor para cima duas linhas (uma para a mensagem de erro e outra para a entrada da data)
    print("\033[F\033[K", end="")  # Move para cima e limpa a linha
    print("\033[F\033[K", end="")  # Move para cima novamente e limpa a linha
    print("\033[F\033[K", end="")  # Move para cima novamente e limpa a linha

# Function for Date in format xx/xx/xxxx
def data_formatada(data):
    return data.strftime('%d/%m/%Y')

# Validating entered date format
def validar_data(data_str):
    try:
        dateBirth = datetime.strptime(data_str, '%d/%m/%Y')
        return dateBirth
    except ValueError:
        return False # Returning False if input the wrong date format



# Register part
def register():
    print("------------- BANK CLEAN -------------\n")
    # Entering full user name
    name = input("Enter full client name: ")
    
    # Loop for check correct format in date birth
    while True:
        data_str = input("Enter Client Date of Birth(dd/mm/yyyy): ")
        data = validar_data(data_str) # Checking date
        if data:
            break
        else:
            print("Invalid date format. Please use dd/mm/yyyy")
            input("Press Enter to try again...")  # Pausa para o usuário ver a mensagem
            clean_lines()  # Limpa as linhas anteriores
        
    # Customer's cell phone number
    phone = input("Enter Client Cell Phone: ")
    # Email
    email = input("Enter Client Email: ")
    
    # Entering Balance for client
    saldo = float(input("Balance for Client: "))
    saldo_formatado = f"{saldo:,.2f}"  # Formata com separadores de milhares e duas casas decimais
    
    input("Click Enter for Continue...")
        
    # Wait two(2) seconds
    time.sleep(2)
    # Clean terminal
    cleanTerminal()
    
    print("Successful Registration!")
    # Wait two(2) seconds
    time.sleep(3)
    cleanTerminal()
    
    
# Call the Function 
register()

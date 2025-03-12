import os # Operational System
import re # RegEx
from datetime import datetime # Data
import time # Wait for clean terminal

# Global variable
saldo = 1.0 # Every Client initial with $1 dolar in account


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
def data_format(data):
    return data.strftime('%d/%m/%Y')

# Validating entered date format
def checking_data(data_str):
    try:
        dateBirth = datetime.strptime(data_str, '%d/%m/%Y')
        return dateBirth
    except ValueError:
        return False # Returning False if input the wrong date format



# Register part
def register():
    
    global name # Permission for modified this variable
    
    print("------------------ BANK CLEAN ------------------\n")
    # Entering full user name
    name = input("-> Enter full client name: ")
    
    # Loop for check correct format in date birth
    while True:
        data_str = input("-> Enter Client Date of Birth(dd/mm/yyyy): ")
        data = checking_data(data_str) # Checking date
        if data:
            break
        else:
            print("Invalid date format. Please use dd/mm/yyyy")
            input("Press Enter to try again...")  # Pausa para o usuário ver a mensagem
            clean_lines()  # Limpa as linhas anteriores

    # Loop for check CPF
    while True:
        cpf = input("-> CPF Client(Only Numbers): ").strip() # Strip remove white spaces
        if len(cpf) == 11 and cpf.isdigit(): # Check this eleven numbers
            break
        else:
            print("Invalid CPF. Please use only 11 numbers")
            input("Press Enter to try again...") 
            clean_lines()  # Limpa as linhas anteriores
    
    # Customer's cell phone number
    phone = input("-> Enter Client Cell Phone: ")
    # Email
    email = input("-> Enter Client Email: ")
    
    # Entering Balance for client
    saldo = float(input("-> Balance for Client(first time customer, starts with $1): "))
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
    

# Deposit Function
def deposit(saldo):
    while True:
        try:
            # Request the deposit amount
            valor = float(input("-> Enter deposit amount: "))
            time.sleep(2)
            cleanTerminal()
            
            if valor > 0:
                saldo += valor
                print("")
                print(f"Deposit successful! New balance in the account {name}: {saldo:,.2f}")
                return saldo
            else:
                print("Invalid deposit amount. Please enter a positive value.")
        except ValueError:
            print("Invalid deposit amount. Please enter a valid number.")
    
# Call the Function
register()
saldo = deposit(saldo)

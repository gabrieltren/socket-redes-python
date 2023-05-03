

def tam_number(str_number):
    return len(str_number)

def par_impar_number(str_number):
    number = int(str_number)
    return b'PAR' if number % 2 == 0 else b'IMPAR'
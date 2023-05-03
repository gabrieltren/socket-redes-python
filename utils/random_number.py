import random
import uuid

def random_number_int_tam(tam):
    number = random.randint((10**tam-1) ,(10**tam) -1)
    return f"{number}"

def random_number_int():
    tam = random.randint(1,40)
    number = random.randint(0,10**tam) if tam<=30 else random.randint(0,10**30)
    return f"{number}"

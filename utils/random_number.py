import random
import uuid

def random_number_int_tam(tam):
    number = random.randint((10**tam-1) ,(10**tam) -1)
    return f"{number}"


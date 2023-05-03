import random
import string

def string_random(tam):
    return bytes(''.join(random.choices(string.ascii_letters + string.digits, k=tam)), 'utf-8')
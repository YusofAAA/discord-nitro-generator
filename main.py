import random
import string
def random_string(length=32):
    character_set = string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))

for i in range(int(input('How many codes? '))):
    codes = random_string(24)
    print('Code: ' + 'https://discord.gift/ + codes)
input('Please click enter too continue.')

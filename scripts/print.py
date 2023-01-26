def custom_print(secret_stuff=None):
    some_stuff = get_stuff(secret_stuff)
    print(f'Função será chamada: {some_stuff}')

def get_stuff(secret_stuff):
    print(secret_stuff)
    return 'stuff'

if __name__ == "__main__":
    custom_print()
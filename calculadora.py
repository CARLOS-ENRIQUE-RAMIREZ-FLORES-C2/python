# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount


def run():
    print(' _______    _______    _          _______    _     _    _          _______    ______     _______    ______     _______ ')
    print('(_______)  (_______)  (_)        (_______)  (_)   (_)  (_)        (_______)  (______)   (_______)  (_____ \   (_______)')
    print(' _          _______    _          _          _     _    _          _______    _     _    _     _    _____) )   _______ ')
    print('| |        |  ___  |  | |        | |        | |   | |  | |        |  ___  |  | |   | |  | |   | |  |  __  /   |  ___  |')
    print('| |_____   | |   | |  | |_____   | |_____   | |___| |  | |_____   | |   | |  | |__/ /   | |___| |  | |  \ \   | |   | |')
    print(' \______)  |_|   |_|  |_______)   \______)   \_____/   |_______)  |_|   |_|  |_____/     \_____/   |_|   |_|  |_|   |_|')
    print()

    ammount = float(input('Ingresa la cantidad de pesos Mexicanos: $'))
    print()
    res = foreign_exchange_calculator(ammount)


    print()
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, res))
    print()


if __name__ == '__main__':
    run()
    print('    ___ _       ')
    print('   / __|_)      ')
    print(' _| |__ _ ____  ')
    print('(_   __) |  _ \ ')
    print('  | |  | | | | |')
    print('  |_|  |_|_| |_|')             
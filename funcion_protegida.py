# -*- coding: utf-8 -*-
def protected(func):
    def wrapper(password):
        if password == 'password':
            return func()
        else:
            print('La contraseña es INCORRECTA')
        
    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)
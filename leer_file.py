"""
‘r’ = leer
’w’ = escribir
’a’ = añadir
’r+’ = leer y escribir
"""
def run():
    counterLetter = 0
    with open("alepth.txt", 'r') as f:
        for line in f:    
            counterLetter += line.count('Beatriz')
    print('Beatriz se encontro {} veces'. format(counterLetter))
if __name__ == '__main__':
    run()
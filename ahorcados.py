# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_index = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_index.append(idx)

        if len(letter_index) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print()
                print('HO HO! PERDISTE!!! la palabra era {}'.format(word))
                print()
                print()

                print('                       .~#########%%;~.')
                print('                     /############%%;`\ ')
                print('                    /######/~\/~\%%;,;,\ ')
                print('                   |#######\    /;;;;.,.| ')
                print('                   |#########\/%;;;;;.,.| ')
                print('          XX       |##/~~\####%;;;/~~\;,|       XX ')
                print('        XX..X      |#|  o  \##%;/  o  |.|      X..XX ')
                print('      XX.....X     |##\____/##%;\____/.,|     X.....XX ')
                print(' XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX ')
                print('X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X ')
                print('X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X ')
                print('X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X ')
                print(' X# \.X        @#%,.@                  @#%,.@        X./  # ')
                print('  ##  X          @#%,.@              @#%,.@          X   # ')
                print(', "# #X            @#%,.@          @#%,.@            X ## ')
                print('   `###X             @#%,.@      @#%,.@             ####¨ ')
                print('  . ¨ ###              @#%.,@  @#%,.@              ###`" ')
                print('    . ";"                @#%.@#%,.@                ;"` ¨ . ')
                print('      ¨                    @#%,.@                   ,. ')
                print('      ` ,                @#%,.@  @@                ` ')
                print('                          @@@  @@@   ')
                break
        else:
            for idx in letter_index:
                hidden_word[idx] = current_letter

            letter_index = []
        try:
            hidden_word.index('-')
        except ValueError:
            print()
            print('############  G A N A S T E ################')
            print()
            print()
            print('     .     .       .  .   . .   .   . .    +  . ')
            print('  .     .  :     .    .. :. .___---------___. ')
            print('       .  .   .    .  :.:. _".^ .^ ^.  ¨.. :"-_. . ')
            print('    .  :       .  .  .:../:            . .^  :.:\. ')
            print('        .   . :: +. :.:/: .   .    .        . . .:\ ')
            print(' .  :    .     . _ :::/:               .  ^ .  . .:\ ')
            print('  .. . .   . - : :.:./.                        .  .:\ ')
            print('  .      .     . :..|:                    .  .  ^. .:| ')
            print('    .       . : : ..||        .                . . !:| ')
            print('  .     . . . ::. ::\(                           . :)/ ')
            print(' .   .     : . : .:.|. ######              .#######::| ')
            print('  :.. .  :-  : .:  ::|.#######           ..########:| ')
            print(' .  .  .  ..  .  .. :\ ########          :######## :/ ')
            print('  .        .+ :: : -.:\ ########       . ########.:/ ')
            print('    .  .+   . . . . :.:\. #######       #######..:/ ')
            print('      :: . . . . ::.:..:.\           .   .   ..:/ ')
            print('   .   .   .  .. :  -::::.\.       | |     . .:/ ')
            print('      .  :  .  .  .-:.":.::.\             ..:/ ')
            print(' .      -.   . . . .: .:::.:.\.           .:/ ')
            print('.   .   .  :      : ....::_:..:\   ___.  :/ ')
            print('   .   .  .   .:. .. .  .: :.:.:\       :/ ')
            print('     +   .   .   : . ::. :.:. .:.|\  .:/| ')
            print('     .         +   .  .  ...:: ..|  --.:| ')
            print('.      . . .   .  .  . ... :..:.."(  ..)" ')
            print(' .   .       .      :  .   .: ::/  .  .::\ ')
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()

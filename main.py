a = list(input())
Morse = []

for i in range(0, len(a)):
    if (a[i] == 'А') or (a[i] == 'а'):
        Morse.append('*-')
    elif (a[i] == 'Б') or (a[i] == 'б'):
        Morse.append('-***')
    elif (a[i] == 'В') or (a[i] == 'в'):
        Morse.append('*--')
    elif (a[i] == 'Г') or (a[i] == 'г'):
        Morse.append('--*')
    elif (a[i] == 'Д') or (a[i] == 'д'):
        Morse.append('-**')
    elif (a[i] == 'Е') or (a[i] == 'е'):
        Morse.append('*')
    elif (a[i] == 'Ж') or (a[i] == 'ж'):
        Morse.append('***-')
    elif (a[i] == 'З') or (a[i] == 'з'):
        Morse.append('--**')
    elif (a[i] == 'И') or (a[i] == 'и'):
        Morse.append('**')
    elif (a[i] == 'Й') or (a[i] == 'й'):
        Morse.append('*---')
    elif (a[i] == 'К') or (a[i] == 'к'):
        Morse.append('-*-')
    elif (a[i] == 'Л') or (a[i] == 'л'):
        Morse.append('*-**')
    elif (a[i] == 'М') or (a[i] == 'м'):
        Morse.append('--')
    elif (a[i] == 'Н') or (a[i] == 'н'):
        Morse.append('-*')
    elif (a[i] == 'О') or (a[i] == 'о'):
        Morse.append('---')
    elif (a[i] == 'П') or (a[i] == 'п'):
        Morse.append('*--*')
    elif (a[i] == 'Р') or (a[i] == 'р'):
        Morse.append('*-*')
    elif (a[i] == 'С') or (a[i] == 'с'):
        Morse.append('***')
    elif (a[i] == 'Т') or (a[i] == 'т'):
        Morse.append('-')
    elif (a[i] == 'У') or (a[i] == 'у'):
        Morse.append('**-')
    elif (a[i] == 'Ф') or (a[i] == 'ф'):
        Morse.append('**-*')
    elif (a[i] == 'Х') or (a[i] == 'х'):
        Morse.append('****')
    elif (a[i] == 'Ц') or (a[i] == 'ц'):
        Morse.append('-*-*')
    elif (a[i] == 'Ч') or (a[i] == 'ч'):
        Morse.append('---*')
    elif (a[i] == 'Ш') or (a[i] == 'ш'):
        Morse.append('----')
    elif (a[i] == 'Щ') or (a[i] == 'щ'):
        Morse.append('--*-')
    elif (a[i] == 'Ъ') or (a[i] == 'ъ'):
        Morse.append('*--*-*')
    elif (a[i] == 'Ы') or (a[i] == 'ы'):
        Morse.append('-*--')
    elif (a[i] == 'Ь') or (a[i] == 'ь'):
        Morse.append('-**-')
    elif (a[i] == 'Э') or (a[i] == 'э'):
        Morse.append('**-**')
    elif (a[i] == 'Ю') or (a[i] == 'ю'):
        Morse.append('**--')
    elif (a[i] == 'Я') or (a[i] == 'я'):
        Morse.append('*-*-')
    else:
        Morse.append(a[i])

print(''.join(Morse))
frase = str(input('digite uma frase:\n'))
print('A = ', frase.count('A'))
print('a = ', frase.count('a'))
print('a letras "a" aparece pela 1º em', frase.lower().find('a'))
print('a letras "a" aparece pela ultima vez em',frase.lower().rfind('a'))
# Invertir palabras de una frase dada por el usuario

def frase_invertida(frase):

    palabras = frase.split(' ')

    invertir = ' '.join(reversed(palabras))
    
    return invertir

if __name__ == "__main__":

    tufrase = input("Introduce una frase: ")
  
    print(frase_invertida(tufrase))
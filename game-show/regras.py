from random import randint


def sorteia_numero():
    numero = randint(0,9) 
    return numero


def verifica_resultado(resposta, numero_conhecido, numero_gerado):
    if numero_conhecido == numero_gerado:
        return f"O próximo foi {numero_gerado}.\n{numero_gerado} = {numero_conhecido}, Você Empatou!"
    elif numero_gerado < numero_conhecido:
        if resposta == "menor":
            return f"O próximo foi {numero_gerado}.\n{numero_gerado} < {numero_conhecido}, Você Acertou!"
        else:
            return f"O próximo foi {numero_gerado}.\n{numero_gerado} < {numero_conhecido}, Você Errou!"
    else:
        if resposta == "maior":
            return f"O próximo foi {numero_gerado}.\n{numero_gerado} > {numero_conhecido}, Você Acertou!"
        else:
            return f"O próximo foi {numero_gerado}.\n{numero_gerado} > {numero_conhecido}, Você Errou!"


def soma_pontos(texto_resultado,ponto_atual):
    if "Acertou" in texto_resultado:
        return ponto_atual + 1
    else:
        return ponto_atual


def controle_tentativas(texto_resultado, tetantivas):
    if "Errou" in texto_resultado:
        return tetantivas - 1
    else:
        return tetantivas


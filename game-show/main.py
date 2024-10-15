import flet as ft
from random import randint

def sorteia_numero():
    numero = randint(0,9) 
    return int(numero)

numero_sorteado = sorteia_numero()
proximo = sorteia_numero()

def criar_container_texto(componente_texto):
    """
    Retorna uma instancia do comopnete Container,
    com as configurações estabeleciadas para o grupo de texto
    """

    instancia_container = ft.Container(
        content=componente_texto,
        alignment=ft.alignment.center,
        padding=5
        )
    return instancia_container


def main(page: ft.Page):
    
    # configurações iniciais da janela
    page.title = "GAME SHOW - Adivinhe o Próximo Número"
    page.window.width = 380       
    page.window.height = 480
    page.update()

    def atualiza_valores_botoes(aleatorio_atual):
        novo_aleatorio = sorteia_numero()
        data = [aleatorio_atual,novo_aleatorio]
        botao_menor.data = data 
        botao_maior.data = data 
        # botao_maior.data[1] = novo_aleatorio

    def evento_botao_menor(e):
        aleatorio_atual = botao_menor.data[0]
        if botao_menor.data[1] < botao_menor.data[0]:
            texto_resultado.value = f"O próximo foi {botao_menor.data[1]}, você Acertou"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_menor.data[1]}"
            atualiza_valores_botoes(botao_menor.data[1])
            page.update()
        elif botao_menor.data[0] == botao_menor.data[1]:
            texto_resultado.value = f"O próximo foi {botao_menor.data[1]}, Foi empate"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_menor.data[1]}"
            atualiza_valores_botoes(botao_menor.data[1])
            page.update()
        else:
            texto_resultado.value = f"O próximo é {botao_menor.data[1]}, você Errou"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_menor.data[1]}"
            atualiza_valores_botoes(botao_menor.data[1])
            page.update()
            

    def evento_botao_maior(e):
        if botao_maior.data[1] > botao_maior.data[0]:
            texto_resultado.value = f"O próximo é {botao_maior.data[1]}, você Acertou"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_maior.data[1]}"
            atualiza_valores_botoes(botao_maior.data[1])
            page.update()
        elif botao_maior.data[0] == botao_maior.data[1]:
            texto_resultado.value = f"O próximo é {botao_maior.data[1]}, Foi empate"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_maior.data[1]}"
            atualiza_valores_botoes(botao_maior.data[1])
            page.update()
            
        else:
            texto_resultado.value = f"O próximo é {botao_maior.data[1]}, você Errou"
            text_numero_sorteado.value = f"O número Sorteado é: {botao_maior.data[1]}"
            atualiza_valores_botoes(botao_maior.data[1])
            page.update()
            


    # componentes de texto
    text_cabecalho = ft.Text("Bem Vindo ao Jogo de Adivinhação",text_align=ft.TextAlign.CENTER,size=18)
    text_numero_sorteado = ft.Text(f"O número Sorteado é: {numero_sorteado}",size=14)
    texto_info_estatica = ft.Text("O próximo número será?",text_align=ft.TextAlign.CENTER,size=14)
    texto_resultado = ft.Text("",text_align=ft.TextAlign.CENTER,size=18)

    # componentes de botões
    botao_menor = ft.ElevatedButton("Menor",on_click=evento_botao_menor,data=[numero_sorteado,proximo])
    botao_maior = ft.ElevatedButton("Maior",on_click=evento_botao_maior,data=[numero_sorteado,proximo])
    
    # estrutura de coluna com os componente de texto
    grupo_texto_coluna = [
        criar_container_texto(text_cabecalho),
        criar_container_texto(text_numero_sorteado),
        criar_container_texto(texto_info_estatica)
    ]
    page.add(
        ft.Column(grupo_texto_coluna))
    
    # agrupa os botões maior e menor em um componente de linha
    linha_grupo_botoes = ft.Row([botao_menor, botao_maior], alignment=ft.MainAxisAlignment.CENTER)
    
    proximo_sorteio = sorteia_numero()
    
    # adiciona o componente de linha dos botões em um container com estilos de espaçamento
    container_botoes = ft.Column(
        [ft.Container(
        margin=15,
        padding=10,
        content=linha_grupo_botoes)]
    )
    page.add(container_botoes)
    page.add(criar_container_texto(texto_resultado))

ft.app(main)
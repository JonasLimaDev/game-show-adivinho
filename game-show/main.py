import flet as ft
from random import randint

def main(page: ft.Page):
    def sorteia_numero():
        return randint(0,9)
    page.title = "Adivinhe o Próximo Número"
    page.window.width = 380       
    page.window.height = 480
    
    page.update()
    numero_sorteado = sorteia_numero()
    lista_textos_coluna = []
    
    inicio = ft.Text("Bem Vindo ao Jogo de Adivinhação",text_align=ft.TextAlign.CENTER,size=18)
    lista_textos_coluna.append(ft.Container(
        content=inicio,
        alignment=ft.alignment.center,
        padding=10,
 
        ))


    texto_numero_sorteado = ft.Text(f"O número Sorteado é: {numero_sorteado}",size=14)
    lista_textos_coluna.append(ft.Container(
        content=texto_numero_sorteado,
        alignment=ft.alignment.center,
        padding=5,
 
        ))
    
    texto_info_estatica = ft.Text("O próximo número será?",text_align=ft.TextAlign.CENTER)
    
    lista_textos_coluna.append(ft.Container(
        content=texto_info_estatica,
        alignment=ft.alignment.center,
        padding=5,
        
        ))
    
    page.add(
        ft.Column(lista_textos_coluna))
    
    # cria os botões de maior e menor
    botao_menor = ft.ElevatedButton("Menor")
    botao_maior = ft.ElevatedButton("Maior")

    # agrupa os botões mair e menor em linha
    linha_grupo_botoes = ft.Row([botao_menor, botao_maior], alignment=ft.MainAxisAlignment.CENTER)
    proximo_sorteio = sorteia_numero()
    # adiciona o grupo de botões em um container com estilizações
    container_botoes = ft.Column(
        [ft.Container(
        margin=15,
        padding=10,
        content=linha_grupo_botoes)])
    
    page.add(container_botoes)

ft.app(main)
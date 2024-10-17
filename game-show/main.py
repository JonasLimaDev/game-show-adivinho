import flet as ft
from random import randint

from regras import (
    sorteia_numero, verifica_resultado, 
    soma_pontos, controle_tentativas
    )


numero_sorteado = sorteia_numero()
# proximo = sorteia_numero()
pontuacao = 0
tentativas = 3

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
    page.window.width = 400       
    page.window.height = 480
    page.update()

    def evento_click_resposta(evento):
        global numero_sorteado
        global pontuacao
        global tentativas
        novo_sorteado = sorteia_numero()
        resposta = evento.control.text.lower()
        resultado = verifica_resultado(resposta, numero_sorteado, novo_sorteado)
        texto_resultado_modal.value = resultado 
        page.open(dlg_modal)
        numero_sorteado = novo_sorteado
        pontuacao = soma_pontos(resultado, pontuacao)
        tentativas = controle_tentativas(resultado, tentativas)
        atualiza_textos_globais()
        
    
    def atualiza_textos_globais():
        text_numero_sorteado.value = f"O número Sorteado é: {numero_sorteado}"
        texto_tenativas_restantes.value = f"Ainda restam {tentativas} Tentativas"
        texto_pontuacao.value = f"Atualmente você fez {pontuacao} Ponto(s)"


    text_cabecalho = ft.Text("Bem Vindo ao Jogo de Adivinhação",text_align=ft.TextAlign.CENTER,size=18)
    text_numero_sorteado = ft.Text(f"O número Sorteado é: {numero_sorteado}",size=14)
    texto_pergunta = ft.Text("O próximo número será?",text_align=ft.TextAlign.CENTER,size=14)
    texto_tenativas_restantes = ft.Text(f"Ainda restam {tentativas} Tentativas",text_align=ft.TextAlign.CENTER,size=16)
    texto_pontuacao = ft.Text("",text_align=ft.TextAlign.CENTER,size=16)
    

    # componentes de botões
    botao_menor = ft.ElevatedButton("Menor",on_click=evento_click_resposta)
    botao_maior = ft.ElevatedButton("Maior",on_click=evento_click_resposta)
    
    # estrutura de coluna com os componente de texto
    grupo_texto_coluna = [
        criar_container_texto(text_cabecalho),
        criar_container_texto(text_numero_sorteado),
        criar_container_texto(texto_pergunta)
    ]
    page.add(
        ft.Column(grupo_texto_coluna))
    
    # agrupa os botões maior e menor em um componente de linha
    linha_grupo_botoes = ft.Row([botao_menor, botao_maior], alignment=ft.MainAxisAlignment.CENTER)

    # adiciona o componente de linha dos botões em um container com estilos de espaçamento
    container_botoes = ft.Column(
        [ft.Container(
        margin=15,
        padding=10,
        content=linha_grupo_botoes)]
    )

    def handle_close(e):
        page.close(dlg_modal)
        page.update()
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
    texto_resultado_modal = ft.Text("",text_align=ft.TextAlign.CENTER,size=16)
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Resultado",text_align=ft.TextAlign.CENTER,size=20),
        content=texto_resultado_modal,
        actions=[
            ft.TextButton("Continuar", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.add(container_botoes)
    page.add(
        criar_container_texto(texto_tenativas_restantes),
        criar_container_texto(texto_pontuacao)
    )

ft.app(main)
import PySimpleGUI as sg

#Definindo o layout
layout = [
    [[sg.text('Digite seu nome: '), sg.Input(key='-NOME-')],
     [sg.Text('Digite seu email: '), sg.Input(key='-EMAIL-')]],

    [[sg.Text('Digite seu fone: '), sg.Input(key='-FONE-')],
    [sg.Button('Enviar'), sg.Button('Sair')]],
]

#Crianado a janela
janela =sg.Window('Minha Primeira Interface', layout)

#Loop de eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break
    if evento == 'Enviar':
        sg.popup(f'Olá, {valores["-NOME-"]}!')

#Fechando a janela
janela.close()




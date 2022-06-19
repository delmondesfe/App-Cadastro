import PySimpleGUI as sg


layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login'),sg.Button('fechar')],
    [sg.Text('',key='mensagem')],
]


janela = sg.Window('login',layout=layout)
#janela = sg.theme('dark')

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'fechar':
        break
    elif event == 'login':
        senha_correta = 'fe270495'
        usuario_correto = 'ludelmondes'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            janela['mensagem'].update('Login realizado com sucesso')
        else:
            janela['mensagem'].update('Usuario ou senha invalidos')
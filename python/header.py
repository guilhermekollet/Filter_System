import PySimpleGUI as sg

class tela:
    def __init__(self):
        #layout
        layout = [
            [sg.text('Tela inicial')]
            [sg.Button()]
        ]
        #janela
        janela = sg.Window("Filter System").layout(layout)
        #extrair os dados da tela
        self.button, self.values = janela.ProgressBarColor(tuple[1,2])
    def Iniciar(self):
        print(self.values)
telaPy = tela()
telaPy.Iniciar()
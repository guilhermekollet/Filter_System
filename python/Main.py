import pandas as pd
import PySimpleGUI as sg
import re

class filter:
    def __init__(self,url,tag,status):
        base = pd.read_excel(r'E:\Usuários\GuiSk\GitHub\Filter_System\data\Lista de Aprovados.xlsx')
        columns = base.shape[1]
        print(f'Quantidade de Colunas Detectada: {columns}')
        columns = columns - 1

        for list in range(int(columns)):
            bt = base.iloc[:,[list]]
            if status == 'inteiro':
                bt = re.sub('[0-9]', '', base)
                print(bt)
            elif status == 'string':
                bt = re.sub('[^0-9]', '', base)
                
            if bt == tag:
                print('true')
            else:
                print('false')
        '''
        
        print(columns)
        for validation in range(columns):
            for vale
        '''
class tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Caminho do arquivo',size=(22,0)),sg.Input(size=(35,0),key='caminho')],
            [sg.Text('Palavra TAG',size=(22,0)),sg.Input(size=(35,0),key='tag')],
            [sg.Button('Gerar Inspeção')]
        ]
        #janela
        janela = sg.Window("Filter System").layout(layout)
        #extrair os dados da tela
        self.button, self.values = janela.Read()
    def Iniciar(self):
        url = self.values['caminho']
        tag = self.values['tag']

        try:
            val = int(tag)
            status = "inteiro"
        except ValueError:
            status = "string"


        filter(url,tag,status)

telaPy = tela()
telaPy.Iniciar()

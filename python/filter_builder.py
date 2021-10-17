#===========================IMPORT================================₢

import pandas as pd
import re

#============================READ=================================₢

base = pd.read_excel(r'E:\Usuários\GuiSk\GitHub\Filter_System\data\Lista de Aprovados.xlsx')

print(f'''
---------------------------------------------------------------------------₢
Informações coletadas:

{base}

---------------------------------------------------------------------------₢
''')

#=========DESCOBRE QUANTAS LINHAS E COLUNAS A BASE TÊM============₢

lines, columns = base.shape

#=================================================================₢


#============================SHOW=================================₢

print(f'''
Quantidade de Linhas na Base de dados
- {lines}

Quantidade de Colunas
- {columns}

''')

#=============================TAG=================================₢

#usuário escolhe a tag (inseri de teste)
filter_motor = "BERNARDO"

#tag tratada
filter_motor = filter_motor.upper()

#verifica a veracidade da informação e categoriza:
    # [ Algoritmo tenta converter para inteiro ]
    # [ Caso não consiga, retorna um erro, logo é um string ]

        # motivo: se o usuário desejar pesquisar por uma matrícula, ele pode

try:
        val = int(filter_motor)
        status = "inteiro"
except ValueError:
        status = "string"

#armazena o resultado do teste em status
print(f'''
Detalhes do Filtro de Busca

Filtro: {filter_motor}
Tipo detectado: {status}

---------------------------------------------------------------------------₢
''')

#====================IMPRIME A BASE DE DADOS======================₢
print('As colunas da base de dados:\n')
for list in base:
    print(list)
print('---------------')
#=============================IMP=================================₢
auxColumn = 0
auxLine = 0
for x in base:
    auxColumn += 1
    print(f'Coluna: {auxColumn}')

    for y in range(0,lines):
        #verificar x y
        data_tratted = base.loc[y, x]
        
        #for n in data_tratted:
         #   print(n)
        '''
        data_tratted = data_tratted.split()
        for n in data_tratted:
            #if (status == "string" && filter_motor == n):
             #   if n 
             print(n)
                 
        print(f'Linha: {auxLine} - {data_tratted}')
        auxLine += 1

        if auxLine >= lines:
            auxLine = 0

'''
#fazer desenho no papel
print(base.count())
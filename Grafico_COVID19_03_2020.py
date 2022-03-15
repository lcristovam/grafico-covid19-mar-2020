#Grafico de Previsão de infectabilidade do COVID19 - 03-2020 / 04-2020
""""""

# Crescimento da população brasileira 1980-2016

import matplotlib.pyplot as plt
dados = open("ESTADOS_BRASIL.csv").readlines()
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []
x7 = []
y7 = []



for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x1.append(str(linha[0]))
        y1.append(int(linha[1]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x2.append(str(linha[0]))
        y2.append(int(linha[2]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x3.append(str(linha[0]))
        y3.append(int(linha[3]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x4.append(str(linha[0]))
        y4.append(int(linha[4]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x5.append(str(linha[0]))
        y5.append(int(linha[5]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x6.append(str(linha[0]))
        y6.append(int(linha[6]))
for i in range(len(dados)):
   if i !=0:
        linha = dados[i].split(";")
        x7.append(str(linha[0]))
        y7.append(int(linha[7]))
print(x7)

plt.title(" COVID19 - Infectividade no Brasil - Março - 2020")
plt.xlabel("Dias")
plt.ylabel("Nº Casos confirmados ")
plt.plot(x1,y1 , label = "São Paulo", color = "r", linestyle ="-" )
plt.plot(x2,y2, label = "Rio de Janeiro", color = "b", linestyle =":")
plt.plot(x3,y3, label = "Distrito Federal", color = "k",   linestyle ="-.")
plt.plot(x4,y4, label = "Rio Grande do Sul", color = "k",   linestyle ="-")
plt.plot(x5,y5, label = "Santa Catarina", color = "c",   linestyle ="-")
plt.plot(x6,y6, label = "Paraná", color = "b",   linestyle ="--")
plt.plot(x7,y7, label = "Minais Gerais", color = "g",   linestyle ="--")
plt.legend()
plt.show()


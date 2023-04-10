frase = "   Curso em video Python   "
print(frase[3]) #Dando print da 3 letra
print(frase[3:13]) #Dando print da 3 letra ate a 13°
print(frase[::2]) #Começando da letra 0 ate o final pulando 2 casas
print(frase[1:21:2])#Dando print da primeira letra ate a 21 pulando 2 casas
print(frase.count("o"))#Contando quantos "o" Existem na frase
print(frase.count("O"))#Contando quantos "O" Existem na frase
print(frase.upper().count("o"))#Colocando a frase em maisculo + Contando quantos "o" Existem na frase
print(frase.upper().count("O"))#Colocando a frase em maisculo + Contando quantos "O" Existem na frasee
print(len(frase))#Mostrando o tamanho da frase
print(len(frase.strip()))#Mostrando o tamanho da frase e cortando todos os espaços desnecessarios exceto os do meio
print(frase.replace("Python","Roblox")) #Subistitui Python por Roblox
print("Curso" in frase) #Perguntando se a palavra "Curso" Esta na frase
frase = frase.replace("Python","Roblox") #Subistitui Python por Roblox e Salvei na variavel
print(frase.find("Curso"))#Procurar a palavra "Curso" na frase
print(frase.lower().find("Curso"))#Colocando a frase em minusculo + Procurar a palavra "Curso" na frase
dividido = frase.split()#Criando a variavel "dividido" e dizendo parar dividir a frase aonde possui espaços
print(dividido[0])#Pegando a primeira divisao (0)  da frase e mostrando na tela
print(dividido[0][3])##Pegando da primeira divisao (0) e mostrando na tela a 3° letra
#Dentro de alguns codigos você consegue colocar no começo a letra "l" ou "r" para começar a ler da esquerda ou da direita
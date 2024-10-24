nome = input('nome:')
sobrenome= input('sobrenome:')
idade=input('idade:')

listaA=[nome,sobrenome,idade]

print(listaA)

#Ex2
mes=int(input("Digite um mes de 1 á 12"))

listaB=["'janeiro', 'fevereiro', 'março', 'abril', 'maio','junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro'"]

print(listaB[mes])

#ex3 extra 
user= ("insira a lista escolhida")
if listaA:
    print('listaA escolhida')
else:
    listaB
    print('listaB escolhida')
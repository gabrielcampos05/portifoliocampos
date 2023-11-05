#Gabriel Campos Amaral Ribeiro
#25/05/2023
cont=0
tupla='Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90,'Post-it',9.90

comprimento = len(tupla)
#print(comprimento)

#Mostra tudo da tupla um embaixo do outro
#for elemento in tupla:
#    print(elemento)

for i in range(0, comprimento, 2):
        print(f'{tupla[i] :.<30} R$ {tupla[i+1]:.2f}')





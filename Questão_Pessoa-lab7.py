#Para criar um dicionário, você começa pelo nome do cidionário e o faz receber '{}'
#Dicionários vão ter uma 'chave' e um 'valor' em cada posição, assim:
#Nome  =  {key1 : valor1,      key2   : valor2,    key3  : valor3}
Pessoa = {'nome':'Rafael', 'sobrenome':'Serafim', 'idade': '19'}

#Para acessar um valor de um dicionário, basta chamar seu nome e inserir uma chave entre colchetes, assim:

print(Pessoa['nome']) #Esse print retorna 'Rafael'

print(f"{Pessoa['nome']} {Pessoa['sobrenome']}, {Pessoa['idade']} anos")

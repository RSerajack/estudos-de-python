num_favoritos = {'Fernanda' : 15, 'Serafim' : 7, 'Isa' : 9, 'Levi' : 12}
#Nessa questão, usaremos o for para acessar todos os elementos de um dicionário
#Vamos criar a estrutura da seguinte forma
for k, v in num_favoritos.items():
  print(f"O número favorito de {k} é {v}");

#Esse for conta com dois parâmetros, o primeiro ('k') é a chave e
#o segundo ('v') é o valor atrelado a chave 'k'.

#então fazemos k e y tomar os valores dos itens contidos no dicionário

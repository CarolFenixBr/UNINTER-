class Calculadora: #classe chamada calculadora
  def __init__(self):
    self.num1=5
    self.num2=9
    self.result=0

  #Função dentro da classe, operações matemáticas
  def soma(self,num1,num2):  #definição de soma
    self.num1=num1
    self.num2=num2
    self.result= self.num1 + self.num2
    return self.result

  def subtrair(self,num1,num2):    #definição para subtrair
    self.num1=num1
    self.num2=num2
    self.result= self.num1 - self.num2
    return self.result

  def multiplicar(self,num1,num2):  #definição para a multiplicação
    self.num1=num1
    self.num2=num2
    self.result= self.num1 * self.num2
    return self.result

  def dividir(self,num1,num2):    #definição para a divisão
    self.num1=num1
    self.num2=num2
    self.result= self.num1 / self.num2
    return self.result

  def expoente(self,num1,num2):  #definição para o expoente
    self.num1=num1
    self.num2=num2
    self.result= self.num1 ** self.num2
    return self.result

  def resto(self,num1,num2):     #definição para o resto
    self.num1=num1
    self.num2=num2
    self.result= self.num1 % self.num2
    return self.result

def continuar(entrada):        #verificação se irá continuar ou não
  if entrada:
    return True
  else:
    return False

def menu():                   # Definição para a apresentação do menu
  opcao = {1: 'Adição',
           2: 'Subtração',
           3: 'Multiplicação',
           4: 'Divisão',
           5: 'Exponenciação',
           6: 'Módulo(resto)'}
  cal = Calculadora()
  print("""Qual é a operação matemática desejada?
    1-> Adição
    2-> Subtração
    3-> Multiplicação
    4-> Divisão
    5-> Exponenciação
    6-> Módulo(resto)
    Digite o número desejado e apaerter ENTER""")
  #criando uma nova variável, quando a calculadora for verdadeira
  calcular = True
  while calcular:
    opc = input("\nEscolha a opção de cálculo (1, 2, 3, 4, 5 ou 6)") #implementação das opções
    if not(opc in '1 2 3 4 5 6'):   #se não for estas opção irá aparecer a mensagem que está no print
      print("Opção escolhida é inválida.")
      continue
    else:
      opc = int(opc)  #somente números inteiros
      print(f"Opção escolhida foi {opcao[opc]}.")
      print("Apenas números inteiros serão trabalhados!")
    if opc== 1:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.soma(num1, num2)
      print(f"O valor da operação adição é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))
    
    if opc== 2:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.subtrair(num1, num2)
      print(f"O valor da operação subtração é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    if opc== 3:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.multiplicar(num1, num2)
      print(f"O valor da operação multiplicação é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    if opc== 4:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.dividir(num1, num2)
      print(f"O valor da operação divisão é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    if opc== 5:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.expoente(num1, num2)
      print(f"O valor da operação expoenciação é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))

    if opc== 6:
      num1= int(input("Digite o penúltimo número do seu RU:"))
      num2= int(input("Digite o último número do seu RU"))
      result = cal.resto(num1, num2)
      print(f"O valor da operação módulo é {result}")
      calcular = continuar(input("Digite alguma coisa para continuar ou apertar ENTER para sair da calculadora."))
      print("Cálculo encerrado")

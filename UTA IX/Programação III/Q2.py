class Estado: 

    def __init__(self, sigla, nome): 

        self.sigla = sigla 

        self.nome = nome 

        self.proximo = None 

 

class TabelaHash: 

    def __init__(self): 

        self.tamanho = 10 

        self.tabela = [None] * self.tamanho 

 

    def funcao_hash(self, sigla): 

        if sigla == "DF": 

            return 7 

        else: 

            char1_ascii = ord(sigla[0]) 

            char2_ascii = ord(sigla[1]) 

            return (char1_ascii + char2_ascii) % self.tamanho 

 

    def inserir(self, estado): 

        posicao = self.funcao_hash(estado.sigla) 

        if self.tabela[posicao] is None: 

            self.tabela[posicao] = estado 

        else: 

            estado.proximo = self.tabela[posicao] 

            self.tabela[posicao] = estado 

             

    def imprimir(self): # Define imprimir as a method within the class 

        for i, estado in enumerate(self.tabela): 

            estados_na_posicao = [] 

            while estado: 

                estados_na_posicao.append(estado.sigla) 

                estado = estado.proximo 

 

            # Always append "None" at the end 

            estados_na_posicao.append("None")   

            print(f"{i}: {'->'.join(estados_na_posicao)}") 

 

 

                                   

 

# Criando a tabela hash 

tabela_hash = TabelaHash() 

 

# Imprimindo a tabela hash inicial (todos None) 

print("Tabela hash inicial:") 

tabela_hash.imprimir() 

 

# Inserindo os estados e o Distrito Federal 

estados = [ 

    Estado("AC", "Acre"), 

    Estado("AL", "Alagoas"), 

    Estado("AP", "Amapá"), 

    Estado("AM", "Amazonas"), 

    Estado("BA", "Bahia"), 

    Estado("CE", "Ceará"), 

    Estado("ES", "Espírito Santo"), 

    Estado("GO", "Goiás"), 

    Estado("MA", "Maranhão"), 

    Estado("MT", "Mato Grosso"), 

    Estado("MS", "Mato Grosso do Sul"), 

    Estado("MG", "Minas Gerais"), 

    Estado("PA", "Pará"), 

    Estado("PB", "Paraíba"), 

    Estado("PR", "Paraná"), 

    Estado("PE", "Pernambuco"), 

    Estado("PI", "Piauí"), 

    Estado("RJ", "Rio de Janeiro"), 

    Estado("RN", "Rio Grande do Norte"), 

    Estado("RS", "Rio Grande do Sul"), 

    Estado("RO", "Rondônia"), 

    Estado("RR", "Roraima"), 

    Estado("SC", "Santa Catarina"), 

    Estado("SP", "São Paulo"), 

    Estado("SE", "Sergipe"), 

    Estado("TO", "Tocantins"), 

    Estado("DF", "Distrito Federal") 

] 

 

for i in range(len(estados)): 

    tabela_hash.inserir(estados[i]) 

     

 

# Imprimindo a tabela hash sem o estado fictício 

print("Tabela hash sem o estado fictício:") 

tabela_hash.imprimir() 

print() 

 

# Inserindo o estado fictício 

estado_ficticio = Estado("CC", "Caroline Vargas da Silva Costa") 

tabela_hash.inserir(estado_ficticio) 

 

# Imprimindo a tabela hash com o estado fictício 

print("Tabela hash com o estado fictício:") 

tabela_hash.imprimir()

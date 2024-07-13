class Nodo: 

    def __init__(self, numero, cor): 

        self.numero = numero 

        self.cor = cor 

        self.proximo = None 

 

# Função para inserir um Nodo no final da lista 

def inserirSemPrioridade(Nodo, head): 

    if not head: 

        head = Nodo 

    else: 

        atual = head 

        while atual.proximo: 

            atual = atual.proximo 

        atual.proximo = Nodo 

    return head 

 

# Função para inserir um Nodo após todos os Nodos com cor "A" 

def inserirComPrioridade(Nodo, head): 

    if not head: 

        head = Nodo 

    else: 

        if Nodo.cor == "A": 

            if Nodo.numero <= 201: 

                Nodo.proximo = head 

                head = Nodo 

            else: 

                atual = head 

                while atual.proximo and atual.proximo.cor == "A" and atual.proximo.numero <= 201: 

                    atual = atual.proximo 

                Nodo.proximo = atual.proximo 

                atual.proximo = Nodo 

        else: 

            atual = head 

            while atual.proximo and atual.proximo.cor == "A": 

                atual = atual.proximo 

            Nodo.proximo = atual.proximo 

            atual.proximo = Nodo 

    return head 

 

 

# Função para inserir um paciente na fila 

def inserir(head): 

    cor = input("Digite a cor do cartão (A ou V): ") 

    numero = int(input("Digite o número do cartão: ")) 

    Nodo_Nodo = Nodo(numero, cor) 

 

    if cor == "V": 

        head = inserirSemPrioridade(Nodo_Nodo, head) 

    elif cor == "A": 

        head = inserirComPrioridade(Nodo_Nodo, head) 

    return head 

 

# Função para imprimir a lista de espera 

def imprimirListaEspera(head): 

    # Criar uma lista para armazenar os pacientes 

    pacientes = [] 

    atual = head 

    while atual: 

        pacientes.append(atual) 

        atual = atual.proximo 

     

    # Ordenar a lista de pacientes, priorizando a cor "A" e depois o número 

    pacientes.sort(key=lambda paciente: (paciente.cor != "A", paciente.numero)) 

     

    # Imprimir a lista ordenada 

    for paciente in pacientes: 

        print(f"Cartão {paciente.cor}: {paciente.numero}") 

 

# Função para atender o próximo paciente 

def atenderPaciente(head): 

    if not head: 

        print("Não há pacientes na fila.") 

        return head 

 

    # Encontrar o paciente com cartão "A" de menor número 

    paciente_a_atender = None 

    atual = head 

    while atual: 

        if atual.cor == "A" and (paciente_a_atender is None or atual.numero < paciente_a_atender.numero): 

            paciente_a_atender = atual 

        atual = atual.proximo 

 

    # Se não houver pacientes com cartão "A", atender o primeiro da fila 

    if paciente_a_atender is None: 

        paciente = head 

        head = head.proximo 

    else: 

        # Remover o paciente a ser atendido da lista 

        if paciente_a_atender == head: 

            head = head.proximo 

        else: 

            anterior = head 

            while anterior.proximo != paciente_a_atender: 

                anterior = anterior.proximo 

            anterior.proximo = paciente_a_atender.proximo 

        paciente = paciente_a_atender 

 

    print(f"Chamando paciente com cartão {paciente.cor}: {paciente.numero}") 

    return head 

 

# Função principal (menu) 

def main(): 

    head = None 

    while True: 

        print("\nMenu:") 

        print("1 - Adicionar paciente à fila") 

        print("2 - Mostrar pacientes na fila") 

        print("3 - Chamar paciente") 

        print("4 - Sair") 

        opcao = int(input("Escolha uma opção: ")) 

 

        if opcao == 1: 

            head = inserir(head) 

        elif opcao == 2: 

            imprimirListaEspera(head) 

        elif opcao == 3: 

            head = atenderPaciente(head) 

        elif opcao == 4: 

            break 

        else: 

            print("Opção inválida. Tente novamente.") 

 

if __name__ == "__main__": 

    main() 

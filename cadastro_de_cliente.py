clients = []

def add_client():
    client = {}
    client['name'] = input("Nome do cliente: ").strip()
    client['phone'] = input("Número de telefone: ").strip()
    client['address'] = input("Endereço: ").strip()
    client['cpf'] = input("CPF: ").strip()
    while True:
        birth_date = input("Data de nascimento (DD/MM/AAAA): ").strip()
        if validate_date(birth_date):
            client['birth_date'] = birth_date
            break
        else:
            print("Data inválida! Tente novamente.")
    clients.append(client)
    print("Cliente cadastrado com sucesso!")

def list_clients():
    if not clients:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLista de clientes cadastrados:")
        for i, client in enumerate(clients, start=1):
            print(f"Cliente {i}:")
            print(f"  Nome: {client['name']}")
            print(f"  Telefone: {client['phone']}")
            print(f"  Endereço: {client['address']}")
            print(f"  CPF: {client['cpf']}")
            print(f"  Data de nascimento: {client['birth_date']}")
            print("-" * 30)

def validate_date(date):
    try:
        day, month, year = map(int, date.split('/'))
        return 1 <= day <= 31 and 1 <= month <= 12 and year >= 1900
    except ValueError:
        return False

def find_client_by_name(name):
    for index, client in enumerate(clients):
        if client['name'].lower() == name.lower():
            return index
    return -1

def update_client():
    name = input("Nome do cliente a ser atualizado: ").strip()
    index = find_client_by_name(name)
    if index == -1:
        print("Cliente não encontrado.")
    else:
        print("Deixe o campo vazio para manter o valor atual.")
        new_phone = input("Novo número de telefone: ").strip()
        new_address = input("Novo endereço: ").strip()
        new_cpf = input("Novo CPF: ").strip()
        while True:
            new_birth_date = input("Nova data de nascimento (DD/MM/AAAA): ").strip()
            if not new_birth_date or validate_date(new_birth_date):
                break
            print("Data inválida! Tente novamente.")
        
        if new_phone:
            clients[index]['phone'] = new_phone
        if new_address:
            clients[index]['address'] = new_address
        if new_cpf:
            clients[index]['cpf'] = new_cpf
        if new_birth_date:
            clients[index]['birth_date'] = new_birth_date
        print("Cliente atualizado com sucesso!")

def remove_client():
    name = input("Nome do cliente a ser removido: ").strip()
    index = find_client_by_name(name)
    if index == -1:
        print("Cliente não encontrado.")
    else:
        clients.pop(index)
        print("Cliente removido com sucesso!")

def menu():
    while True:
        print("\n1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Atualizar dados do cliente")
        print("4. Remover cliente")
        print("5. Sair")
        option = input("Escolha uma opção: ").strip()
        if option == '1':
            add_client()
        elif option == '2':
            list_clients()
        elif option == '3':
            update_client()
        elif option == '4':
            remove_client()
        elif option == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()

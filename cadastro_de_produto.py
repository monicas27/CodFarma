products = []
product_count = 0


def find_product_by_name(name):
    for index, product in enumerate(products):
        if product["name"].lower() == name.lower():
            return index
    return -1


def add_product():
    global product_count
    if len(products) >= 100:
        print("Erro: Capacidade máxima de produtos atingida.")
        return
    
    name = input("Nome do produto: ").strip()
    if find_product_by_name(name) != -1:
        print("Erro: Produto já cadastrado.")
        return
    
    try:
        value = float(input("Valor do produto: "))
        quantity = int(input("Quantidade em estoque: "))
        prescription_needed = input("Precisa de receita médica? (s/n): ").strip().lower() == 's'
    except ValueError:
        print("Erro: Dados inválidos. Tente novamente.")
        return

    product = {
        "id": product_count + 1,
        "name": name,
        "value": value,
        "quantity": quantity,
        "prescription_needed": prescription_needed
    }
    products.append(product)
    product_count += 1
    print("Produto cadastrado com sucesso!")


def list_products():
    if not products:
        print("\nNenhum produto cadastrado.")
        return

    print("\nLista de produtos cadastrados:")
    for product in products:
        print(f"ID: {product['id']}")
        print(f"Nome: {product['name']}")
        print(f"Valor: R${product['value']:.2f}")
        print(f"Quantidade em estoque: {product['quantity']}")
        print(f"Precisa de receita médica: {'Sim' if product['prescription_needed'] else 'Não'}")
        print("-----------------------------")


def edit_product():
    name = input("Nome do produto a ser editado: ").strip()
    index = find_product_by_name(name)
    if index == -1:
        print("Erro: Produto não encontrado.")
        return
    
    try:
        products[index]["name"] = input("Novo nome do produto: ").strip()
        products[index]["value"] = float(input("Novo valor do produto: "))
        products[index]["quantity"] = int(input("Nova quantidade em estoque: "))
        print("Produto editado com sucesso!")
    except ValueError:
        print("Erro: Dados inválidos. Tente novamente.")


def menu():
    while True:
        print("\n1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Editar produto")
        print("4. Sair")
        option = input("Escolha uma opção: ").strip()
        if option == "1":
            add_product()
        elif option == "2":
            list_products()
        elif option == "3":
            edit_product()
        elif option == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()

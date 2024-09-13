from utils import gerarCartelas, salvarCartelas, lerCartelas, imprimirCartelas

def menu():
    cartelas = {}
    while True:
        print("\n1. Gerar Cartelas")
        print("2. Salvar Cartelas")
        print("3. Ler Cartelas")
        print("4. Imprimir Cartelas")
        print("5. Sair")
        
        escolha = input("Escolha: ").strip()
        
        if escolha == '1':
            n = int(input("Quantidade: "))
            sucesso, resultado = gerarCartelas(n)
            if sucesso:
                cartelas = resultado
                print(f"Geradas: {len(cartelas)}")
            else:
                print(f"Erro: {resultado}")

        elif escolha == '2':
            sucesso, mensagem = salvarCartelas(cartelas)
            print(mensagem)

        elif escolha == '3':
            sucesso, resultado = lerCartelas()
            if sucesso:
                cartelas = resultado
                print("Lidas.")
            else:
                print(f"Erro: {resultado}")

        elif escolha == '4':
            if not cartelas:
                print("Nenhuma cartela.")
                continue
            id_c = input("Número da cartela: ").strip()
            sucesso, resultado = imprimirCartelas(id_c, cartelas)
            if sucesso:
                print(f"Cartela {id_c}:\n{resultado}")
            else:
                print(f"Erro: {resultado}")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

# gerenciador de tarefas

import os
import json

# funcao para carregar tarefas
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    return []

# exibe todas as tarefas
def listar_tarefas(tarefas):
    print("Tarefas: ")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['status'] else "Pendente"
        print(f"ID: {tarefa['id']}, Título {tarefa['titulo']}, Status: {status}")

# escreve no arquivo e salva as tarefas
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# gerar id
def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]['id'] + 1 # última tarefa com id 3, nova tarefa com id 4


# adicionar tarefas
def adicionar_tarefa(tarefas):
    print("Adicionar nova tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")

    tarefa = {
        "id": gerar_id(tarefas),
        "titulo": titulo,
        "descricao": descricao,
        "status": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# concluir tarefa
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['status']:
                    print("A tarefa já está concluída")
                else:
                    tarefa['status'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluída com sucesso.")
                return
        print("Tarefa não encontrada")
    except ValueError:
        print("ID inválido.")

# menu principal
def menu():
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")
    return int(input("Escolha uma opção: "))

# Loop das ações
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()

        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            listar_tarefas(tarefas)
        elif opcao == 3:
            concluir_tarefa(tarefas)
        elif opcao == 4:
            excluir_tarefa(tarefas)
        elif opcao == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")
# inicialização da função main()
if __name__ == '__main__':
    main()
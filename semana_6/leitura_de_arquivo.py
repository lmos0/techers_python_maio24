#Crie uma função ler_arquivo(nome_arquivo) que recebe o nome de um arquivo e tenta ler seu conteúdo. Utilize try-except para tratar o caso de o arquivo não existir.

def ler_arquivo(caminho__do_arquivo):
    try:
        with open(caminho__do_arquivo, 'r') as arquivo:
            return arquivo.read()
    except:
        return "Erro: Não há nenhum arquivo no diretório mencionado"


caminho_do_arquivo = "tarefa2.txt"

print(ler_arquivo(caminho_do_arquivo))

# Requisitos 11 e 12
def analyzer_menu():
    options = int(input("Selecione uma das opções a seguir: \n" +
                        " 0 - Popular o banco com notícias;\n" +
                        " 1 - Buscar notícias por título;\n" +
                        " 2 - Buscar notícias por data;\n" +
                        " 3 - Buscar notícias por categoria;\n" +
                        " 4 - Listar top 5 categorias;\n" +
                        " 5 - Sair.\n"))

    if options == 5:
        return None

    if options == 0:
        first_option = input("Digite quantas notícias serão buscadas:")


print(analyzer_menu())

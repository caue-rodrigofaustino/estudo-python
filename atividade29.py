import os
import shutil

def criar_diretorio(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretório {diretorio} criado")
            except PermissionError:
                print(f"Erro: Você não tem permissões para criar {diretorio}")
            except Exception as e:
                print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivos(diretorio_o):
    for arquivo in os.listdir(diretorio_o):
        caminho_arquivo = os.path.join(diretorio_o, arquivo)

        if os.path.isfile(caminho_arquivo):
            # Melhor forma de pegar a extensão
            partes = arquivo.split('.')
            if len(partes) > 1:
                extensao = partes[-1].lower()

                if extensao in ['pdf', 'jpg', 'txt']:
                    diretorio_destino = os.path.join(diretorio_o, extensao)
                    try:
                        shutil.move(caminho_arquivo, diretorio_destino)
                        print(f"Sucesso: {arquivo} movido para {diretorio_destino}")
                    except Exception as e:
                        print(f"Erro ao mover {arquivo}: {e}")
                else:
                    # Agora o print está no lugar certo para avisar sobre arquivos ignorados
                    print(f"Aviso: Extensão .{extensao} não suportada para o arquivo {arquivo}")

def main():
    diretorio_trabalho = "diretorio_trabalho"
    # Criamos as subpastas baseadas nas extensões permitidas
    diretorios = [os.path.join(diretorio_trabalho, ext) for ext in ['pdf', 'jpg', 'txt']]

    criar_diretorio(diretorios)
    mover_arquivos(diretorio_trabalho)

if __name__ == "__main__":
    main()
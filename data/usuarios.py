import json
import os


ARQUIVO_DADOS = os.path.join(
    os.path.dirname(__file__),
    "usuarios.json"
)


def carregar_usuarios():
    """Carrega os usuários armazenados no arquivo JSON."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_usuarios(usuarios):
    """Salva os usuários no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def gerar_id(usuarios):
    """Gera um novo identificador numérico para o usuário."""
    if not usuarios:
        return 1

    return max(usuario["id"] for usuario in usuarios) + 1
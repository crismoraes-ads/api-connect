from flask import request, jsonify

from data.usuarios import (
    carregar_usuarios,
    salvar_usuarios,
    gerar_id
)


def cadastrar_usuario():
    """Cadastra um novo usuário."""

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "error": "A requisição deve conter dados em formato JSON."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "error": "Os campos nome e email são obrigatórios."
        }), 400

    nome = nome.strip()
    email = email.strip()

    if not nome or not email:
        return jsonify({
            "error": "Os campos nome e email não podem estar vazios."
        }), 400

    usuarios = carregar_usuarios()

    novo_usuario = {
        "id": gerar_id(usuarios),
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    return jsonify({
        "data": novo_usuario
    }), 201


def listar_usuarios():
    """Retorna todos os usuários cadastrados."""

    usuarios = carregar_usuarios()

    return jsonify({
        "data": usuarios
    }), 200


def buscar_usuario(usuario_id):
    """Busca um usuário pelo seu identificador."""

    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario.get("id") == usuario_id:
            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado.",
        "id_solicitado": usuario_id
    }), 404


def atualizar_usuario(usuario_id):
    """Atualiza os dados de um usuário existente."""

    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario.get("id") == usuario_id:

            dados = request.get_json(silent=True)

            if not isinstance(dados, dict):
                return jsonify({
                    "error": "A requisição deve conter dados em formato JSON."
                }), 400

            nome = dados.get("nome")
            email = dados.get("email")

            if not nome or not email:
                return jsonify({
                    "error": "Os campos nome e email são obrigatórios."
                }), 400

            usuario["nome"] = nome.strip()
            usuario["email"] = email.strip()

            salvar_usuarios(usuarios)

            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado.",
        "id_solicitado": usuario_id
    }), 404


def remover_usuario(usuario_id):
    """Remove um usuário pelo seu identificador."""

    usuarios = carregar_usuarios()

    for indice, usuario in enumerate(usuarios):
        if usuario.get("id") == usuario_id:

            usuario_removido = usuarios.pop(indice)
            salvar_usuarios(usuarios)

            return jsonify({
                "data": usuario_removido
            }), 200

    return jsonify({
        "error": "Usuário não encontrado.",
        "id_solicitado": usuario_id
    }), 404
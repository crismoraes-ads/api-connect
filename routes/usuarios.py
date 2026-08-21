from flask import Blueprint

from controllers.usuarios_controller import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)


usuarios_bp = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)


@usuarios_bp.route("", methods=["POST"])
def criar():
    return cadastrar_usuario()


@usuarios_bp.route("", methods=["GET"])
def listar():
    return listar_usuarios()


@usuarios_bp.route("/<int:usuario_id>", methods=["GET"])
def buscar(usuario_id):
    return buscar_usuario(usuario_id)


@usuarios_bp.route("/<int:usuario_id>", methods=["PUT"])
def atualizar(usuario_id):
    return atualizar_usuario(usuario_id)


@usuarios_bp.route("/<int:usuario_id>", methods=["DELETE"])
def remover(usuario_id):
    return remover_usuario(usuario_id)
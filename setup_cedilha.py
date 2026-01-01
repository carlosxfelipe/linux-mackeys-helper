#!/usr/bin/env python3
# Este script corrige um bug presente no Linux Mint 22.2 e em outras distribuições
# Linux, onde ao tentar digitar o cedilha (ç) aparece o caractere ć no lugar.
# Ele ajusta o arquivo .XCompose do usuário para garantir que ´ + c produza ç corretamente.
from pathlib import Path

# Conteúdo do arquivo .XCompose para cedilha
XCOMPOSE_CONTENT = """include "%L"

# Cedilha com dead_acute (´ + c)
<dead_acute> <C>       : "Ç" Ccedilla  # LATIN CAPITAL LETTER C WITH CEDILLA
<dead_acute> <c>       : "ç" ccedilla  # LATIN SMALL LETTER C WITH CEDILLA
"""


def setup_xcompose():
    """Cria ou atualiza o arquivo .XCompose no diretório home"""
    xcompose_path = Path.home() / ".XCompose"

    try:
        with open(xcompose_path, "w", encoding="utf-8") as f:
            f.write(XCOMPOSE_CONTENT)

        print(f"✅ Cedilha configurada em: {xcompose_path}")
        print("Reinicie o aplicativo ou faça logout/login para ativar.")

    except Exception as e:
        print(f"\n❌ Erro ao criar .XCompose: {e}")


if __name__ == "__main__":
    print("Configurando cedilha para US Internacional...")
    setup_xcompose()

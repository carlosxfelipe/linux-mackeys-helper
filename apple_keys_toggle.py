#!/usr/bin/env python3
import subprocess

# Opção para trocar Ctrl com Alt (Command no K380s modo Mac)
OPTION = "ctrl:swap_lalt_lctl"


def enable():
    subprocess.run(["setxkbmap", "-option", ""])
    subprocess.run(["setxkbmap", "-layout", "us", "-variant", "intl"])
    subprocess.run(["setxkbmap", "-option", OPTION])
    print("🍎 Ctrl esquerdo trocado com Alt esquerdo")
    print("⌨️  Layout alterado para US Internacional")


def disable():
    subprocess.run(["setxkbmap", "-option", ""])
    print("🔄 Troca de Ctrl e Alt desfeita")


def menu():
    print("=" * 50)
    print("  Configuração de Teclado K380s - Linux Mint")
    print("=" * 50)

    while True:
        print("""
    1) Ativar Ctrl ↔ Command (estilo macOS)
    2) Desfazer troca de Ctrl e Alt
    3) Definir layout ABNT2 (não recomendado para o K380s)
    4) Sair
    """)
        c = input("Escolha uma opção > ").strip()

        if c == "1":
            enable()
        elif c == "2":
            disable()
        elif c == "3":
            print(
                "⚠️  O layout ABNT2 não é recomendado para teclados que não seguem o padrão ABNT2, pois pode causar incompatibilidades nas teclas."
            )
            subprocess.run(["setxkbmap", "-layout", "br", "-variant", "abnt2"])
            print("🔄 Layout ABNT2 aplicado")
        elif c == "4":
            print("\n👋 Até logo!\n")
            break
        else:
            print("❌ Opção inválida")


if __name__ == "__main__":
    menu()

#!/usr/bin/env python3
import subprocess

LAYOUT = "us"
VARIANT = "intl"

# Opção para trocar Ctrl com Alt (Command no K380s modo Mac)
OPTION = "ctrl:swap_lalt_lctl"
SCHEMAS = [
    ("org.cinnamon.desktop.input-sources", "Cinnamon"),
    ("org.gnome.desktop.input-sources", "GNOME"),
]


def _run(cmd):
    return subprocess.run(cmd, text=True, capture_output=True)


def _schema_available(schema):
    result = _run(["gsettings", "list-schemas"])
    return result.returncode == 0 and schema in result.stdout


def _set_sources(schema, layout, variant):
    source = f"[('xkb', '{layout}+{variant}')]" if variant else f"[('xkb', '{layout}')]"
    _run(["gsettings", "set", schema, "sources", source])


def _set_options(schema, options):
    data = "[]" if not options else f"['{options}']"
    _run(["gsettings", "set", schema, "xkb-options", data])


def _apply_session(layout, variant, option=None):
    _run(["setxkbmap", "-option", ""])
    cmd = ["setxkbmap", "-layout", layout]
    if variant:
        cmd += ["-variant", variant]
    _run(cmd)

    if option:
        _run(["setxkbmap", "-option", option])


def _apply_persistent(layout, variant, option=None):
    applied = []

    for schema, label in SCHEMAS:
        if not _schema_available(schema):
            continue
        _set_sources(schema, layout, variant)
        _set_options(schema, option)
        applied.append(label)

    if not applied:
        print(
            "ℹ️  Nenhum schema de ambiente gráfico detectado no gsettings. Aplicando apenas na sessão atual."
        )
        return

    print(f"💾 Configuração persistente salva em: {', '.join(applied)}")


def enable():
    _apply_session(LAYOUT, VARIANT, OPTION)
    _apply_persistent(LAYOUT, VARIANT, OPTION)
    print("🍎 Ctrl esquerdo trocado com Alt esquerdo")
    print("⌨️  Layout alterado para US Internacional")


def disable():
    _apply_session(LAYOUT, VARIANT)
    _apply_persistent(LAYOUT, VARIANT)
    print("🔄 Troca de Ctrl e Alt desfeita")


def apply_abnt2():
    _apply_session("br", "abnt2")
    _apply_persistent("br", "abnt2")
    print("🔄 Layout ABNT2 aplicado")


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
            apply_abnt2()
        elif c == "4":
            print("\n👋 Até logo!\n")
            break
        else:
            print("❌ Opção inválida")


if __name__ == "__main__":
    menu()

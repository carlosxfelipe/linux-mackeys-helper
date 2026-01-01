# Linux MacKeys Helper

Scripts para facilitar o uso de teclados como o Logitech K380s e outros modelos que não possuem layout ABNT2, mas sim um layout semelhante ao da Apple, que é o US Internacional. Este script é destinado ao uso em sistemas Linux.

## Scripts

- **apple_keys_toggle.py**: Permite trocar as teclas Ctrl e Alt (Command) para um comportamento estilo macOS, alterar o layout do teclado para US Internacional, entre outras funções.

- **setup_cedilha.py**: Corrige o bug em algumas distribuições Linux (ex: Linux Mint) onde ao digitar o cedilha (ç) aparece o caractere ć. O script ajusta o arquivo .XCompose do usuário para garantir que ´ + c produza ç corretamente no layout US Internacional.

## Como executar

No terminal Linux, execute:

```
python3 apple_keys_toggle.py
```

Ou, se preferir, usando uv:

```
uv run apple_keys_toggle.py
```

Repita o mesmo padrão para o script `setup_cedilha.py`, substituindo o nome do arquivo no comando. Execute este script apenas se você estiver enfrentando o bug em que, ao digitar o cedilha (ç), aparece o caractere ć.

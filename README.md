# Ascii Room
Um escape room simples feito em python

## Instalação de Módulos
É necessário ter a versão mais atual de [python](https://www.python.org/) instalada para baixar os módulos. (lembre-se de clicar em "Add python to PATH" quando instalar.)

unidecode (necessário)
  ```
  pip install unidecode
  ```
pyinstaller
  ```
  pip install pyinstaller
  ```
## Como Jogar
Para jogar, basta baixar a ultima versão nos lançamentos. Caso queira alterar o código, será preciso clonar o repositório, baixar os módulos necessários e abrir o arquivo `game.py`.

Caso queira compilar o jogo em um executável, digite ```pyinstaller --onefile game.py``` com o pyinstaller instalado no local do arquivo. Ele será compilado e o executável guardado dentro da pasta `dist` que aparecerá.

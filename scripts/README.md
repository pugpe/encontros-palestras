# Descrição dos scripts disponíveis

## pugpe.py

Este script contém um spider que vai coletar os dados de cada edição do PUG-PE. Para rodar, basta fazer:

    $ python pugpe.py 62

Onde "62" é o número da edição do PUG. Os dados serão armazenados no diretório temp em arquivos json no seguinte formato: talks_{edition}.json

Após coletar os dados, o mesmo script vai gerar um README para cada evento a partir do readme_generator.py.
A estrutura de diretórios vai ser: `ano/edição/README.md`.
# Descrição dos scripts disponíveis

## pugpe.py

Este script contém um spider que vai coletar os dados de cada edição do PUG-PE. Para rodar, basta fazer:

    $ python pugpe.py lxii

Onde "lxii" é o número da edição do PUG em algarismos romanos. É necessário que seja em algarismos romanos, pois precisa dar match com a URL do evento. Os dados serão armazenados no diretório temp em arquivos json no seguinte formato: talks_{edition}.json

Após coletar os dados, o mesmo script vai gerar um README para cada evento a partir do readme_generator.py.
A estrutura de diretórios vai ser: `ano/edição/README.md`.
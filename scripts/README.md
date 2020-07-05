# Descrição dos scripts disponíveis

## pugpe.py

Este script contém um spider que vai coletar os dados de cada edição do PUG-PE. Para rodar, basta fazer:

    $ python pugpe.py 62

Onde "62" é o número da edição do PUG. Os dados serão armazenados no diretório temp em arquivos json no seguinte formato: talks_{edition}.json

Após coletar os dados, o mesmo script vai gerar um README para cada evento a partir do readme_generator.py.
A estrutura de diretórios vai ser: `ano/edição/README.md`.

## rank.py

Este script vai coletar os dados de todas as palestras já realizadas no PUG-PE, que estão disponíveis no site e ranquear os palestrantes por quantidade de palestras. Para executar é simples:

    $ python rank.py

O spider vai armazenar todas as palestras e respectivos palestrantes no arquivo `temp/talks_all.csv`.
Em seguida, o script vai ler esse arquivo, contar as palestras de cada palestrante e gerar um arquivo com o rank final em `rank.csv`.
Atualmente, se for rodar mais de uma vez esse script, é importante antes deletar os dois arquivos acima citados.
# Híbrida

É um projeto que assegura a redução no tempo de tramitação dos processos, a concretização do princípio da eficiência administrativa, auxilia no descongestionado do sistema judicial, assegura incremento da agilidade associando possiveis códigos de assunto locais com os codigos de assuntos CNJ.

## Começando

Para executar o projeto, será necessário instalar:

- [Python 3 (ou acima) : Necessário para executar o projeto](https://www.python.org/downloads)

## Desenvolvimento

Para iniciar o desenvolvimento, você poderá acessar pelo site : ????????    ou poderá clonar o projeto direto na sua máquina em um diretório de sua preferência. 

shell
cd "diretorio de sua preferencia"
git clone https://github.com/CNJ/Hibrida


### Executar

Para executar o projeto via web basta utilizar o link: http://191.235.110.9:8000/

Ou no computador local, após a instalação das depedências no shell
$ python3.7 manager.py runserver


O comando irá baixar todas as dependências do projeto e criar um diretório target com os artefatos construídos.

## Configuração

Para o ótimo desempenho do projeto é impressindivel que os aquivos para a classificação sejam PDF ou txt. O nome do arquivo a ser enviado para a classificação não poder
a conter caracteres especiais e/ou pontuações. 

## Ambiente

Apos a inserção do arquivo pdf e/ou txt o hibrida classificará se a peça se enquadra em um tema repetitivo do 1007 ou não. Caso seja positiva esta afirmação, a máquina sugirá códigos de assuntos dos tribunais TRF3, TRF4 e CNJ para a correta classificação da peça.

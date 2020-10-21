# CNJ-1

![hibrIdA](https://user-images.githubusercontent.com/37173966/96740018-cec57000-1396-11eb-8f6d-cb90afb63760.jpeg)


# Híbrida

É um projeto que assegura a redução no tempo de tramitação dos processos, a concretização do princípio da eficiência administrativa, auxilia no descongestionado do sistema judicial, assegura incremento da agilidade associando possiveis códigos de assunto locais com os codigos de assuntos CNJ.

## Começando .

Para executar o projeto, será necessário instalar:

- [Python 3 (ou acima) : Necessário para executar o projeto](https://www.python.org/downloads)
- [Django 3 (ou acima) : Necessário para executar o projeto](https://www.djangoproject.com/download/)


## Desenvolvimento

Híbrida têm uma aplicação relativamente simples, para iniciar o desenvolvimento, basta acessar pelo navegador de sua preferência o link (http://191.235.110.9:8000/)  

O link levará direto ao ambiente executável de Híbrida em que o usuário poderá navegar como advogado ou magistrado.  

No comando advogado, é possivel incluir peças digitalizadas ou não, para que a máquina detecte se trata de um Tema repetitivo ou não. Os arquivos enviados serão lidos, os textos e palavras vetorizadas, para então fazer um levantamento otimizado do conjunto de palavras, que caracterizam como atributos necessários para a classificação de um tema repetitivo.

![tela2adv](https://user-images.githubusercontent.com/37173966/96637481-1c899c00-12f5-11eb-9ad3-a287a8b5bd69.png)

Após realizada esta análise, Híbrida retorna com uma assertividade maior que 93% de que o texto e seu conjunto de palavras pertencem a um tema repetitivo. (O protótipo analisa apenas o tema repetitivo 1007)

![tela3Conc](https://user-images.githubusercontent.com/37173966/96638347-55764080-12f6-11eb-9efc-233c11ccece7.png)


shell
```
cd "diretorio de sua preferencia"
git clone https://github.com/andersonsimplicio/hibrida.git
```

### Executar

Para executar o projeto via web basta utilizar o link: http://191.235.110.9:8000/

Ou no computador local, após a instalação das depedências descrita no requirements.txt no shell
user@maqui:diretorio_projeto/ python3.7 manager.py runserver


O comando irá baixar todas as dependências do projeto e criar um diretório target com os artefatos construídos.

# Instalando Dependência
```
$ pip3 install -r requirements.txt
```
OBS: algumas bibliotecas terão dependência especifica de acordo com o sistema operacional usado, o sistema hibrida foi projetado
para servidores debian/ubuntu.

## Configuração

Para o ótimo desempenho do projeto é impressindivel que os aquivos para a classificação sejam PDF ou txt. O nome do arquivo a ser enviado para a classificação não poder
a conter caracteres especiais e/ou pontuações. 

## Ambiente

Apos a inserção do arquivo pdf e/ou txt o hibrida classificará se a peça se enquadra em um tema repetitivo do 1007 ou não. Caso seja positiva esta afirmação, a máquina sugirá códigos de assuntos dos tribunais TRF3, TRF4 e CNJ para a correta classificação da peça.

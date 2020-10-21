# CNJ-1

![hibrIdA](https://user-images.githubusercontent.com/37173966/96740018-cec57000-1396-11eb-8f6d-cb90afb63760.jpeg)


# Híbrida

É um projeto que tem por objetivo assegurar a redução no lapso temporal da tramitação dos processos, concretizando os princípios da eficiência e eficácia administrativa, celeridade processual e acesso à justiça. Garante o incremento da agilidade, associando possíveis códigos de assunto locais dos Tribunais com os códigos de assuntos do Conselho Nacional de Justiça - CNJ.

O presente projeto visa atender as demandas propostas pelo desafio 1 TEMPO E PRODUTIVIDADE do edital CNJ INOVA fase 1.


## Começando .

Para executar o projeto, será necessário instalar:

- [Python 3 (ou acima) : Necessário para executar o projeto](https://www.python.org/downloads)
- [Django 3 (ou acima) : Necessário para executar o projeto](https://www.djangoproject.com/download/)


## Desenvolvimento

![desenvolvimento](https://user-images.githubusercontent.com/25744353/96757803-4f429b80-13ac-11eb-8834-ffca3dc95cc9.jpeg)

Híbrida tem uma aplicação relativamente simples e fácil manuseio. Para iniciar o desenvolvimento basta acessar pelo navegador de sua preferência o link (http://191.235.110.9:8000/).

O link levará direto ao ambiente executável de Híbrida, em que o usuário poderá navegar como advogado ou magistrado/servidor do Judiciário.  

No comando advogado é possível incluir peças digitalizadas ou não, para que a máquina detecte se se trata de um Tema Repetitivo ou não. Os arquivos enviados serão lidos, textos e palavras vetorizados, para então se fazer um levantamento otimizado do conjunto de palavras que caracterizam como atributos necessários para a classificação de um Tema Repetitivo.

![tela2adv](https://user-images.githubusercontent.com/37173966/96637481-1c899c00-12f5-11eb-9ad3-a287a8b5bd69.png)

Após, realizada esta análise, Híbrida retorna com uma assertividade maior que 93% ao informar que o texto e seu conjunto de palavras pertencem ou não a um tema repetitivo. (O protótipo analisa apenas o tema repetitivo 1007).

![tela3Conc](https://user-images.githubusercontent.com/37173966/96638347-55764080-12f6-11eb-9efc-233c11ccece7.png)

Em resumo:

![funcionamento](https://user-images.githubusercontent.com/25744353/96758272-f293b080-13ac-11eb-86aa-576d2fef3ae3.jpeg)


### Executar na web

Para executar o projeto via web basta utilizar o link: http://191.235.110.9:8000/


### Processo de instalação em um computador local

shell

```
cd "diretorio de sua preferencia"
git clone https://github.com/andersonsimplicio/hibrida.git
```

### Executar

No computador local, após a instalação das depedências descritas no requirements.txt no shell
user@computador:diretorio_projeto/ python3.7 manager.py runserver


O comando irá baixar todas as dependências do projeto e criar um diretório target com os artefatos construídos.

# Instalando Dependência

```
$ pip3 install -r requirements.txt
```
OBS: Algumas bibliotecas terão dependência específica de acordo com o sistema operacional utilizado. O sistema Híbrida foi projetado para servidores debian/ubuntu.

## Configuração

Para o ótimo desempenho do projeto é imprescindível que os aquivos para a classificação sejam PDF ou txt. O nome do arquivo a ser enviado para a classificação não pode conter caracteres especiais e/ou pontuações. 

## Ambiente

Advogado

Após a inserção do arquivo pdf e/ou txt o Híbrida classificará se a peça se enquadra em um tema repetitivo do 1007 ou não. Caso seja positiva esta afirmação, proporcionará ao advogado informar se está em acordo com a IA ou não, quanto a identificação do tema repetitivo.

Magistrado/servidor do Judiciário

Na área restrita ao magistrado e/ou servidor poderá ser avaliado cada processo ajuizado e verificar quais são as demandas repetitivas e em seguida realizar o parecer/decisão do magistrado. Nesta parte, se houver uma divergência entre a IA e o advogado haverá uma sinalização na tela com a frase "divergência Apontada".

## Youtube
[![image](https://user-images.githubusercontent.com/25744353/96781107-56c16f00-13c3-11eb-87b3-a510e00d8fab.png)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE "Pitch Híbrida. 21/10/20")
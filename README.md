# curriculo
PROJETO WEB PARA CRIAÇÃO DE CURRICULO

## DEPENDENCIAS
* Este projeto depende do python3:5 ou superior assim como de algumas libs
- python3:5
- pip3
    - gunicorn
    - pymongo
    - pillow
    - pycep-correios
    - requests (opcional uso somente para testes)

Também é necessário ter acesso a um banco de dados MongoDB

## INSTALAÇÃO
Para instalar este projeto é simples. O primeiro passo é resolver as depêndencias acima ou usar o Dockerfile para criar uma imagem já configurada.

É necessário criar um arquivo dentro da pasta do flask com o nome "config.py". Neste arquivo vamos colocar parametros de conexão ao banco de dados entre outros. O modelo do arquivo deve seguir o modelo ilustrado abaixo:

```
# Variaveis usadas para conectar no mongodb
mongo_usuario = 'usuario_mongo'
mongo_senha = 'senha_mongo'
mongo_banco = 'banco_mongo'
mongo_servidor = 'ip_servidor_mongo'
mongo_porta = 27017

# REGISTRA A CONTRA-SENHA
contra_senha = 'senha_para_o_input_de_dados_inicial'

## Chave secreta do aplicativo para controle dos sessions
chave_secreta = b'uyIB\xcd\x17\xd1a\x03\xd6U\x05$\x05\x933\xce\xca\xeb\x84J)\xfa\xd7'
```
## DOCUMENTAÇÃO


## TESTES

- /info_curriculo

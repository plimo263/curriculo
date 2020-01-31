# -*- coding: utf-8 -*-
'''
Autor:	Marcos Felipe da Silva Jardim
-------------------------------------------------
'''
from flask import Flask, render_template, session, request, url_for, redirect
import config, modelo, time, sys, json, re, requests, os
from time import time
from bson import ObjectId
from hashlib import sha1
from PIL import Image, ExifTags
import pycep_correios

app = Flask(__name__)
#app.register_blueprint(vendas)

# SOMENTE PARA DESENVOLVIMENTO. FAZ O INPUT INICIAL DOS DADOS
@app.route('/input_inicial')
def input_inicial():
    if not 'contra_senha' in request.args.keys() or not 'contra_senha' in dir(config) or request.args['contra_senha'] != config.contra_senha:
        return json.dumps({'erro': 'ACESSO NAO AUTORIZADO'})
    

    mdb = modelo.Consulta.obter_db_mongo()
    # Carrega o arquivo pickle e faz o inupt inicial dos dados
    import pickle
    with open('./pickles/estados_e_cidades.pickle', 'rb') as arq:
        obj = pickle.load(arq)
    # Sai fazendo a insercao dos estados no banco de dados do db
    mdb.estados.delete_many({})
    for linha in obj:
        mdb.estados.insert_one(linha)
    # INSERE OS ESTADOS CIVIS
    mdb.estado_civil.delete_many({})
    mdb.estado_civil.insert_many([
        {'chave':'solteiro', 'valor': 'SOLTEIRO(A)'}, 
        {'chave':'casado', 'valor': 'CASADO(A)'},
        {'chave':'divorciado', 'valor': 'DIVORCIADO(A)'},
        {'chave':'viuvo', 'valor': 'VIÚVO(A)'},
        {'chave':'separado', 'valor': 'SEPARADO(A)'}
    ])
    # INSERE AS FORMACOES ESCOLARES
    mdb.formacao.delete_many({})
    mdb.formacao.insert_many([
        {'chave': 'fundamental', 'valor': 'FUNDAMENTAL'},
        {'chave': 'medio', 'valor': 'MEDIO'},
        {'chave': 'superior_incompleto', 'valor': 'SUPERIOR INCOMPLETO'},
        {'chave': 'superior', 'valor': 'SUPERIOR COMPLETO'},
    ])

    return json.dumps({'sucesso': 'ENTRADA INICIAL DE DADOS FEITA COM SUCESSO'})


@app.route('/trabalhe_conosco', methods = ['GET', 'POST'])
def trabalhe_conosco():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST': # Registrando um curriculo
        return json.dumps({})

@app.route('/info_curriculo', methods = ['GET'])
def info_curriculo():
    mdb = modelo.Consulta.obter_db_mongo()
    params = request.args
    dados = {} # Consulta de tipos a serem pesquisados
    # Veja se veio um cpf
    if 'cpf' in params.keys():
        dados['cpf'] = False
        # Veja se o cpf são 11 numeros seguidos
        if len(params['cpf']) != 11:
            return json.dumps(dados)
        # No padrao, veja se o cpf existe na base de dados
        if mdb.curriculos.find({'cpf': params['cpf']}).count() == 1:
            dados['cpf'] = True
    # Veja se a consulta espera um estado
    if 'estado' in params.keys():
        dados['estado'] = []
        if 'true' in params['estado']:
            # Retorna os estados como um array
            dados['estado'] = [
                {'valor': reg['nome'] , 'chave': reg['sigla']} for reg in mdb.estados.find({})
            ]
        elif mdb.estados.find({'sigla': params['estado']}).count() == 1: # Veja se o estado solicitado existe
            for reg in mdb.estados.find({'sigla': params['estado']}):
                dados['estado'] = reg['cidades']
    # Busca por registros do estado civil
    if 'estado_civil' in params.keys():
        dados['estado_civil'] = [{'chave': reg['chave'], 'valor': reg['valor']} for reg in mdb.estado_civil.find({})]
    # Busca as formacoes academicas
    if 'formacao' in params.keys():
        dados['formacao'] = [{'chave': reg['chave'], 'valor': reg['valor']} for reg in mdb.formacao.find({})]
    # Uma busca solicitando informacoes do cep repassado
    if 'cep' in params.keys():
        dados['cep'] = {'bairro': '', 'cidade': '', 'logradouro': '', 'uf': ''}
        if len(params['cep']) == 8:
            try:
                resultado = pycep_correios.consultar_cep(params['cep'])
                dados['cep']['bairro'] = resultado['bairro'] # bairro
                dados['cep']['cidade'] = resultado['cidade'] # cidade
                dados['cep']['logradouro'] = resultado['end'] # logradouro
                dados['cep']['uf'] = resultado['uf'] # uf
            except pycep_correios.excecoes.ExcecaoPyCEPCorreios as err:
                print(err)
                pass

            
    
    
    return json.dumps(dados)
## Chave secreta do app
app.secret_key = config.chave_secreta

app.debug = True
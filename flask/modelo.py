# -*- coding: utf8 -*- #

"""

Autor: Marcos Felipe da Silva Jardim

"""
import sys, json, re
from pymongo import MongoClient
import re, time, os, pickle
from PIL import Image, ExifTags
import config

# Variaveis usadas para conectar no mongodb
mongo_usuario = config.mongo_usuario
mongo_senha = config.mongo_senha
mongo_banco = config.mongo_banco
mongo_servidor = config.mongo_servidor
mongo_porta = config.mongo_porta

dirbase = './static/imagens' # DIRETORIO PRA ARMAZENAMENTO DAS IMAGENS

FORMATOS = set(['png','jpg','jpeg']) # FORMATOS DE ARQUIVOS ACEITOS

STATICA = '/static/imagens/' # DIRETORIO BASE DAS IMAGENS

## Classe que gera datas em formato formulario e banco mssql
class Data:
    __de = ''
    __ate = ''
    def __init__(self):
        self.__obterData()

    def __obterData(self):
        try:
            self.__de = session['de']
            self.__ate = session['ate']
        except KeyError:
            dataAtual = datetime.now()
            self.__de = '%04d-%02d-%02d' % (dataAtual.year, dataAtual.month, dataAtual.day)
            self.__ate = '%04d-%02d-%02d' % (dataAtual.year, dataAtual.month, dataAtual.day)

    def getDataForm(self):
        '''Obtem a data no formato tradicional'''
        return [self.__de, self.__ate]

    def getData(self):
        '''Obtem a data no formato de acesso ao banco de dados '''
        de = self.__de.replace('-','')
        ate = self.__ate.replace('-','')
        return [de, ate]
        
    ## Funcao que verifica a data
    @staticmethod
    def verifica_data(de, ate):
        padrao = re.compile('^[2][0][1-9][0-9]-([0][1-9]|[1][0-2])-([3][0-1]|[0][1-9]|[1-2][0-9])$')
        if padrao.match(de) and padrao.match(ate):
            return True
        else:
            return False

## Classe usada para trabalhar com consultas do tipo select. Contem muitos metodos uteis como ordenacao de colunas e filtros de campos
class Consulta:
    @staticmethod
    def obter_db_mongo():
        ''' Retorna o banco de daddos do mongodb informado pelos parametros de acesso em config.py'''
        c = MongoClient('mongodb://%s:%s@%s' % (mongo_usuario, mongo_senha, mongo_servidor))
        return c[mongo_banco]

# Classe para utilitarios
class Utils:
    
    # Metodo para rotacionar um arquivo
    @staticmethod
    def rotate_image(filepath, size = None, novo_nome = None):
        try:
            image = Image.open(filepath)
            exf = None
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                        exf = orientation
            if not exf is None and not image._getexif() is None:
                exif = dict(image._getexif().items())
                
                if exif[exf] == 3:
                    image = image.transpose(Image.ROTATE_180)
                elif exif[exf] == 6:
                    image = image.transpose(Image.ROTATE_270)
                elif exif[exf] == 8:
                    image = image.transpose(Image.ROTATE_90)
            
            # Se tiver a tupla de dimensoes, defina e salve
            if not size is None:
                image = image.resize(size, Image.ANTIALIAS)
            # Se tiver o novo nome então salve neste novocaminho
            if not novo_nome is None:
                image.save(novo_nome)
            else:
                image.save(filepath, quality=95)
            image.close()
        except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
            print('ERRO FUNCAO DE ROTACIONAR IMAGEM')
            pass
    
    # FUNCAO PARA VALIDAR ARQUIVOS
    @staticmethod
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FORMATOS
    
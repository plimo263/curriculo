'''
Autor:  Marcos Felipe da Silva Jardim
versão: 1.0
data:   31-01-2020
------------------------------------------
Historico:
v1.0 31-01-2020: Teste para recuperar informacoes complementares ao curriculo
'''

import json
from requests import Session
import unittest
from urllib.parse import urlencode

class TestCurriculo(unittest.TestCase):

    def __init__(self, *args, **kargs):
        super(TestCurriculo, self).__init__(*args, **kargs)
        self._c = Session()
        self._host = 'http://localhost'
        self._url = '/info_curriculo'
    
    def test_a_cpf_inexistente(self):
        ''' TESTA ENVIO COM UM CPF INEXISTENTE '''
        q = {'cpf': '08777759599'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('cpf', resp.keys())
        self.assertFalse(resp['cpf'])
        #print(resp)
    
    def test_b_estado_todos(self):
        ''' TESTA RECUPERACAO DE TODOS OS ESTADOS '''
        q = {'estado': 'true'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('estado', resp.keys())
        self.assertIsInstance(resp['estado'], list)    
        #print(resp)
    
    def test_c_estado_civil_todos(self):
        ''' RETORNA TODOS OS ESTADOS CIVIS '''
        q = {'estado_civil': 'true'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('estado_civil', resp.keys())
        self.assertIsInstance(resp['estado_civil'], list) 
        #print(resp) 
    
    def test_d_formacao_todos(self):
        ''' RETORNA TODOS AS FORMACOES '''
        q = {'formacao': 'true'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('formacao', resp.keys())
        self.assertIsInstance(resp['formacao'], list)
        #print(resp) 
    
    def test_e_cep(self):
        ''' TESTA A RECUPERACAO DE UM ENDERECO ENVIANDO O CEP '''
        q = {'cep': '30535100'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('cep', resp.keys())
        self.assertIsInstance(resp['cep'], dict)
        #print(resp) 
    
    def test_f_combinados(self):
        ''' FAZ O TESTE TENTANDO RECUPERAR ESTADO, ESTADO CIVIL E FORMACAO '''
        q = {'estado': 'MG', 'formacao': 'true', 'estado_civil': 'true'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('estado', resp.keys())
        self.assertIsInstance(resp['estado'], list)
        self.assertIn('formacao', resp.keys())
        self.assertIsInstance(resp['formacao'], list)
        self.assertIn('estado_civil', resp.keys())
        self.assertIsInstance(resp['estado_civil'], list)
        #print(resp)
            
    def test_g_estado_mg(self):
        ''' TESTA PARA TRAZER TODAS AS CIDADES DO ESTADO DE MINAS GERAIS '''
        q = {'estado': 'MG'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('estado', resp.keys())
        self.assertIsInstance(resp['estado'], list)
        print(resp)
    
    def test_h_cep_nao_existe(self):
        ''' TESTA A RECUPERACAO DE UM ENDERECO ENVIANDO O CEP QUE NAO EXISTE'''
        q = {'cep': '30200000'}
        q = '?'+urlencode(q)
        resp = self._c.get(self._host+self._url+q).json()
        self.assertIn('cep', resp.keys())
        self.assertIsInstance(resp['cep'], dict)
        #print(resp) 


if __name__ == '__main__':
    unittest.main()


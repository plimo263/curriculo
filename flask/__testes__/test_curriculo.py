'''
Autor:  Marcos Felipe da Silva Jardim
versão: 1.0
data:   30-01-2020
------------------------------------------
Historico:
v1.0 30-01-2020: Testa o envio do curriculo com todos os campos obrigatorios
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
        self._url = '/trabalhe_conosco'
    
    def test_a_envio_sem_cp_dados(self):
        ''' FAZ O ENVIO SEM CONTER O CAMPO DADOS '''
        dados = {'outros': json.dumps({
            'nome': 'MARCOS FELIPE'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_b_envio_cp_dados_nao_json(self):
        ''' FAZ O ENVIO DE UM CAMPO DADOS QUE NÃO SEJA JSON'''
        dados = {'dados': {
            'nome': 'MARCOS FELIPE'
        }}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_c_envio_atr_nome_ausente(self):
        ''' FAZ O ENVIO DE UM CAMPO DADOS SEM ATR nome '''
        dados = {'dados': json.dumps({
            'ausente': 'MARCOS FELIPE'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_d_envio_nome_menos_de_5_letras(self):
        ''' ENVIA O ATR nome COM MENOS DE 5 letras '''
        dados = {'dados': json.dumps({
            'nome': 'MAR'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_e_envio_sem_atr_cpf(self):
        ''' ENVIA SEM O ATRIBUTO cpf '''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            #'cpf': '00000000000'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    def test_f_envio_atr_cpf_digitos_incorretos(self):
        ''' ENVIA O ATRIBUTO cpf COM APENAS 9 DIGITOS'''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            'cpf': '000000000'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_g_envio_atr_cpf_invalido(self):
        ''' ENVIA O ATRIBUTO cpf COM NÚMERO INVÁLIDO '''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            'cpf': '12348745899'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_h_envio_atr_nascimento_ausente(self):
        ''' ENVIA O ATRIBUTO NASCIMENTO AUSENTE '''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            'cpf': '11111111111'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_i_envio_atr_nascimento_nao_padrao(self):
        ''' ENVIA O ATR nascimento FORA DO PADRAO AAAA-MM-DD '''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            'cpf': '11111111111',
            'nascimento': '200-01-01'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())
    
    def test_h_envio_atr_nascimento_no_futuro(self):
        ''' ENVIA O ATR nascimento COM DATA MAIOR QUE DATABASE ATUAL '''
        dados = {'dados': json.dumps({
            'nome': 'MARCOS FELIPE', 
            'cpf': '11111111111',
            'nascimento': '2040-01-01'
        })}
        dados = self._c.post(self._host+self._url, data = dados).json()
        self.assertIn('erro', dados.keys())




if __name__ == '__main__':
    unittest.main()


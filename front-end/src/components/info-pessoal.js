import React from 'react'
import '../css/InfoPessoal.css'

class InfoPessoal extends React.Component {

    render(){
        return (
            <div className="InfoPessoal">
                <div className="row">
                    <div className="col-sm-6">
                        <div className='cp-form' ><span>NOME: </span>
                            <input className="form-control" type="text" id="nome_completo" placeholder="DIGITE SEU NOME  COMPLETO"  />
                        </div>
                    </div>
                    <div className="col-sm-3">
                        <div className='cp-form' ><span>CPF: </span>
                            <input className="form-control" type="text" id="cpf" placeholder="DIGITE SEU CPF"  />
                        </div>
                    </div>

                    <div className="col-sm-3">
                        <div className='cp-form' ><span>NASCIMENTO: </span>
                            <input className="form-control" type="date" id="nascimento"  />
                        </div>
                    </div>
                </div>
                <br/>
                <div className="row">
                    <div className="col-sm-3">
                        <div className='cp-form' ><span>SEXO: </span>
                            <select className='form-control input-sm' defaultValue='feminino' name="sexo" id="sexo">
                                <option value="masculino">MASCULINO</option>
                                <option value="feminino">FEMININO</option>
                            </select>
                        </div>
                    </div>
                    <div className="col-sm-3">
                        <div className='cp-form' ><span style={{whiteSpace:'nowrap'}}>ESTADO CIVIL: </span>
                            <select className='form-control input-sm' defaultValue='solteiro' name="estado_civil" id="estado_civil">
                                <option value="solteiro">SOLTEIRO(A)</option>
                                <option value="casado">CASADO(A)</option>
                                <option value="divorciado">DIVORCIADO(A)</option>
                                <option value="viuvo">VIÚVO(A)</option>
                                <option value="separado">SEPARADO(A)</option>
                            </select>
                        </div>
                    </div>

                    <div className="col-sm-6">
                        <div className='cp-form' ><span>EMAIL: </span>
                            <input className="form-control" type="email" id="email" placeholder="DIGITE SEU EMAIL"  />
                        </div>
                    </div>
                </div><br/>
                <div className="row">
                    <div className="col-sm-3">
                        <div className='cp-form' ><span>CEP: </span>
                            <input className="form-control" type="text" id="cep" placeholder="00000-000"  />
                        </div>
                    </div>
                    <div className="col-sm-6">
                        <div className='cp-form' ><span>LOGRADOURO: </span>
                            <input className="form-control" type="text" id="endereco" placeholder="RUA / AV, LOGRADOURO"  />
                        </div>
                    </div>
                    <div className="col-sm-1">
                        <div className='cp-form' ><span>NUMERO </span>
                            <input className="form-control" type="number" id="numero" placeholder="1"  />
                        </div>
                    </div>
                     <div className="col-sm-2">
                        <div className='cp-form' ><span>COMPLEMENTO: </span>
                            <input className="form-control" type="text" id="complemento" placeholder="CASA "  />
                        </div>
                    </div>
                </div><br/>
                 <div className="row">
                  <div className="col-sm-3">
                        <div className='cp-form' ><span>BAIRRO: </span>
                            <input className="form-control" type="text" id="bairro" placeholder="CENTRO "  />
                        </div>
                    </div>
                    <div className="col-sm-3">
                        <div className='cp-form' ><span>ESTADO: </span>
                            <input className="form-control" type="text" id="estado" placeholder="RUA / AV, LOGRADOURO"  />
                        </div>
                    </div>
                    <div className="col-sm-3">
                        <div className='cp-form' ><span>CIDADE: </span>
                            <input className="form-control" type="text" id="cidade" placeholder="00000-000"  />
                        </div>
                    </div>
                    <div className="col-sm-3">
                        <div className='cp-form' ><span style={{whiteSpace:'nowrap'}}>ESCOLARIDADE </span>
                            <select className='form-control input-sm' defaultValue='2_grau_completo' name="escolaridade" id="escolaridade">
                                <option value="1_grau_incompleto">PRIMEIRO GRAU INCOMPLETO</option>
                                <option value="1_grau_completo">PRIMEIRO GRAU COMPLETO</option>
                                <option value="2_grau_incompleto">SEGUNDO GRAU INCOMPLETO</option>
                                <option value="2_grau_completo">SEGUNDO GRAU COMPLETO</option>
                                <option value="superior_incompleto">SUPERIOR INCOMPLETO</option>
                                <option value="superior_completo">SUPERIOR COMPLETO</option>
                            </select>
                        </div>
                    </div>
                    
                </div>
            </div>
        )
    }
}

export default InfoPessoal
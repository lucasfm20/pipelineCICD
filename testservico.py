import pytest
from servico import cadastrar_usuario

        
def testcadastrousuario():
    resultado = cadastrar_usuario("João")
    assert resultado[1] == "João"   

def testcadastroinvalido():
    with pytest.raises(Exception):
        cadastrarusuario(None)   
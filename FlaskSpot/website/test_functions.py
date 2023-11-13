from .models import Condicao

def test_verifica_tainha():
    gamboa = Condicao(2, "Gamboa", 140, 270, 180, 270, 180, 270, 1.4, 2.2, 1.6, 2.5, 2, 2.5, 67, 135, 67, 110, 67, 110, "fechado")
    assert gamboa.verifica_tainha() == True


def test_excutarNorte():
    guarda = Condicao(1,"Guarda do Embaú", 65, 270, 45, 270, 22, 270, 1.1, 2.2, 1.4, 2.2, 1.6, 2.5, 45, 180, 45, 180, 45, 180, "fechado")
    assert guarda.executarNorte(10, 1.9, 130) == "classico"

def test_executarSul():
    silveirasul = Condicao(6, "Silveira Sul", 135, 360, 157, 360, 180, 360, 1.6, 4, 2, 4, 2.3, 4, 90, 180, 90, 180, 100, 160, "bandeira")
    assert silveirasul.executarSul(200, 1.5, 90) == True
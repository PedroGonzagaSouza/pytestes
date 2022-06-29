

def test_consultar_livros_retorna_resultado_formato_string():

    resultado = consultar_livros('Agatha Christie')
    assert type resultado == str
from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert 'lakers' in get_phrases("Los Angeles Lakers")
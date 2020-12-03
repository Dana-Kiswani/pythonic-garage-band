from pythonic_garage_band import __version__
from pythonic_garage_band.band import  Band,Guitarist,Bassist,Drummer,Musician
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def prep_data():
    Michael_Bublé = Bassist("Michael_Bublé","Bassist")
    enrique_iglesias = Guitarist("enrique_iglesias")
    avril_lavigne = Drummer("avril_lavigne")
    Sia = Band("Sia",[Michael_Bublé,enrique_iglesias,avril_lavigne],"She will be loved")
    return {'Michael_Bublé':Michael_Bublé, 'enrique_iglesias':enrique_iglesias, 'avril_lavigne':avril_lavigne , 'Sia': Sia}
# --------------------------------------

def test_play_solos(prep_data):
    expected = ['WjWJjwjajajawiwiwiiw','PweeeeeeeeeeeeeeeeWwWwWwwWWWWWWwwwwwwwww','PoOoMmMmM pPOMMmmmm PummmMMM']              
    actual = prep_data['Sia'].play_solos()
    assert expected==actual
# --------------------------------------

def test_to_list(prep_data):
    expected = Band.to_list()             
    actual = prep_data['Sia'].to_list()
    assert expected == actual
# --------------------------------------

def test_get_gizmo(prep_data):
    expected = 'Guitar'             
    actual = prep_data['enrique_iglesias'].get_gizmo()
    assert expected == actual
# --------------------------------------

def test_play_solo(prep_data):
    expected = 'WjWJjwjajajawiwiwiiw'             
    actual = prep_data['Michael_Bublé'].play_solo()
    assert expected == actual

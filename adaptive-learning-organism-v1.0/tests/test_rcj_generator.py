
from src.rcj_generator import generate_rcj

def test_generate_rcj():
    rcj = generate_rcj("problem-solving")
    assert "reflection" in rcj

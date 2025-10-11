from src.main import read_root

def test_read_root():
    assert read_root() == {"mensaje": "Hola, Leonardo! 🚀 Tu primera API en FastAPI está corriendo."}
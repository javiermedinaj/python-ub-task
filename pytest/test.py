import pytest
from Final import agregar_producto, eliminar_producto, listar_productos, vender_producto, productos

def test_agregar_producto():
    productos.clear()
    agregar_producto("006", "Cereal", 20, 5.0, "2023-07-31", "V")
    assert "006" in productos

def test_eliminar_producto():
    productos.clear()
    agregar_producto("001", "Milk", 50, 1.0, "2023-07-31", "V")
    eliminar_producto("001")
    assert "001" not in productos

def test_vender_producto():
    productos.clear()
    agregar_producto("001", "Milk", 50, 1.0, "2023-07-31", "V")
    vender_producto("001", 5)
    assert productos["001"][1] == 45

def test_listar_productos(capsys):
    productos.clear()
    agregar_producto("001", "Milk", 50, 1.0, "2023-07-31", "V")
    listar_productos()
    captured = capsys.readouterr()
    assert "Milk" in captured.out

if __name__ == "__main__":
    pytest.main()

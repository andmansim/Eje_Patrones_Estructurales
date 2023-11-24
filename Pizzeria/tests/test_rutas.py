import unittest
from unittest.mock import patch
from apps.rutas import app, datos_pizza_per

class TestDatosPizzaPer(unittest.TestCase):
    @patch('apps.rutas.secrets.token_hex', return_value='mocked_token')
    @patch('apps.rutas.guardar_pedido')
    def test_datos_pizza_per(self, mocked_guardar_pedido, mocked_token_hex):
        with app.test_client() as client:
            response = client.post('/datos_pizza_per', data={
                'masa': 'fina',
                'salsa': 'tomate',
                'ingredientes_queso': 'queso',
                # ... otros datos ...
                'coccion': 'horno_de_leña',
                'presentacion': 'caja_de_cartón',
                'bebida': 'agua',
                'postre': 'flan',
            })

        self.assertIn('¡Datos del pedido procesados con éxito!', response.data)
        mocked_guardar_pedido.assert_called_once_with('mocked_token', ..., 'pizza')  # Ajusta los argumentos según tu lógica

if __name__ == '__main__':
    unittest.main()

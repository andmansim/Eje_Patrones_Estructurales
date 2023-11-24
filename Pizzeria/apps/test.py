import unittest
from unittest.mock import patch
from rutas import app

class TestDatosPizzaPer(unittest.TestCase):
    @patch('app.secrets.token_hex', return_value = 'mocked_token')
    @patch('app.request')
    def test_datos_pizza_per(self, mocked_guardar_pedido, mocked_token_hex):
        # Configura la solicitud simulada
        with app.test_client() as client:
            # Simula una solicitud POST con datos específicos
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

        # Realiza afirmaciones (assertions) para verificar el comportamiento esperado
        self.assertIn('¡Datos del pedido procesados con éxito!', response.data)
        mocked_guardar_pedido.assert_called_once_with('mocked_token', ..., 'pizza')  # Ajusta los argumentos según tu lógica

    # Agrega más métodos de prueba según sea necesario para otras combinaciones de datos

if __name__ == '__main__':
    unittest.main()
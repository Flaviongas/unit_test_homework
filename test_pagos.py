from unittest.mock import patch,Mock
from unittest import TestCase
from src.pagos import verificar_saldo_en_banco,procesar_pago



class Tests(TestCase):
  @patch('test_pagos.verificar_saldo_en_banco')
  def test_verificar_saldo_en_banco(self,mock_verificar):
        mock_verificar.return_value = 1000

        saldo = verificar_saldo_en_banco('Juan')
        mock_verificar.assert_called_once_with('Juan')
        self.assertEqual(saldo, 1000)


  def test_procesar_pago_con_saldo_suficiente(self):
        mock_verificador = Mock(return_value=1000)
        resultado = procesar_pago('Juan', 500, mock_verificador)
        mock_verificador.assert_called_once_with('Juan')
        self.assertTrue(resultado)

  def test_procesar_pago_con_saldo_insuficiente(self): 
        mock_verificador = Mock(return_value=300)
        resultado = procesar_pago('Juan', 500, mock_verificador)
        mock_verificador.assert_called_once_with('Juan')
        self.assertFalse(resultado)



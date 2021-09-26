#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from ac2 import exe1, exe2, exe3, exe4, exe5

'''
===============================================================================
Explicação dos testes:

Os casos positivos (casos_positivos) são todos os casos no qual o 
a regex deve permitir a string. Se a regex permitir a string,
a função no qual contém a regex deve retornar um booleano positivo (True),
porém, se não permitir, deve retornar um booleano negativo (False).
Portanto é realizado um loop com um "asssert positive" no qual deve permitir
que caso a função retorne True, o teste se mantém funcionando e caso
porém se retornar um falso o teste encontra um erro e o teste não passa.
O mesmo é realizado com os casos negativos, porém esses devem retornar sempre
False.
O teste só é válido se a função passar por todos os asserts sem retornar um
erro.
=============================================================================== 
'''


class Ac2Tests(unittest.TestCase):
    def test_exe1(self):
        casos_positivos = ["1", "35", "-2", "567", "-4357", "7936"]
        casos_negativos = ["a", "banana", "CEBOLA", "", "$", "foo", " ", "1o1",
                           "o1o", "0.2", "1.2"]
        for positivo in casos_positivos:
            self.assertTrue(exe1(positivo))
        for negativo in casos_negativos:
            self.assertFalse(exe1(negativo))

    def test_exe2(self):
        casos_positivos = ["5", "10", "-20", "5674", "-435678", "79365"]
        casos_negativos = ["a", "banana", "CEBOLA", "", "$", "foo", " ", "1o1",
                           "111", '19', '23', "3333333", "0.2", "1.2"]
        for positivo in casos_positivos:
            self.assertTrue(exe2(positivo))
        for negativo in casos_negativos:
            self.assertFalse(exe2(negativo))

    def test_exe3(self):
        casos_positivos = ["1.000", "25.500", "3.123.000", "48.000.000.001"]
        casos_negativos = ["a", "banana", "CEBOLA", "", "$", "foo", " ", "1o1",
                           "1000", '0.5', "3333333", "109", "00005.900",
                           "444.", ".45", "-1.000.000", "033.00.44",
                           "12.111.00.222", "1.000.00.333.00",
                           "111.111.222.00"]
        for positivo in casos_positivos:
            self.assertTrue(exe3(positivo))
        for negativo in casos_negativos:
            self.assertFalse(exe3(negativo))

    def test_exe4(self):
        casos_positivos = ["ALEX TORQUATO SOUZA CARNEIRO", "MARIA ARAUJO",
                           "JOSE DA SILVA", "ANA APARECIDA"]
        casos_negativos = ["123", "!@3%$ˆ)(*&", "$@#",
                           "alex torquato souza carneiro",
                           " ", "", "JOSÉ DA SILVA", "MaRIa aRaUJo",
                           "ana aparecida", "MAR1A ARAUJO", "100.2", ".00",
                           "@N@ @P@RECID@", "JOSE.DA.SILVA", ".ANA APARECIDA",
                           " MARIA ARAUJO"]
        for positivo in casos_positivos:
            self.assertTrue(exe4(positivo))
        for negativo in casos_negativos:
            self.assertFalse(exe4(negativo))

    def teste_exe5(self):
        pass

if __name__ == "__main__":
    unittest.main()

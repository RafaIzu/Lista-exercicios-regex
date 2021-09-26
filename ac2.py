#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


def exe1(texto):
    """A regex apresentada a baixo significa que a string pode começar
    ou não começar com o caracter "-", O segunte caracter deve ser um dígito
    entre 1 a 9, os demais caracteres que vierem
    podem ser qualquer digito que pode ocorrer mais de uma vez ou não
    não ocorrer. O cifrão indica a condição de parada da regex.
    Sendo que a regex só para de """
    # regex = r"^\-*[1-9][0-9]*$"
    regex = r"^\-*[1-9]\d*$"
    return bool(re.match(regex, texto))

def exe2(texto):
    """A regex apresentada a baixo verifica três possíveis
    condições. A primeira condição é para qualquer string que pode
    ou não começar com "-", o caracter em seguida deve ser entre 1 a 9,
    logo em seguida pode haver 0 ou mais caracteres que sejam números.
    Porém o último caracter deve ser um número 0 ou 5. O cifrão "$" indica
    qual é o último elemento da regex deve considerar. O segundo caso
    é parecido com o primeiro mas só deve terminar com os seguintes números:
    0,2,4,6,8. O último caso é para se for apenas o número cinco, já que o
    primeiro caso não consegue validar apenas o número 5"""
    regex = r"^\-*[1-9]\d*[05]$|^\-*[1-9]\d*[02468]$|^\-*5"
    return bool(re.match(regex, texto))

def exe3(texto):
    """A regex apresentada a abaixo verifica a seguinte condição:
    No primeiro grupo da regex,
    o primeiro caracter deve ser um número entre 1 a 9. Depois, pode vir
    em seguida mais que um carcter que devem ser números. No segundo grupo,
    deve começar com o caracter "." e logo em seguida deve vir exatamente
    3 caracteres que sejam dígitos.Esse segundo grupo pode não ocorrer ou
    pode ocorrer uma ou mais vezes. No último grupo da regex, deve começar com
    "." e logo em seguida dever vir exatamente três caracteres que devem
    ser dígitos. Esse último grupo é condição de parada para a regex no qual
    é indicado pelo cifrão """
    regex = r"([1-9]\d*)(\.\d{3})*(\.\d{3})$"
    return bool(re.match(regex, texto))


def exe4(texto):
    """Na regex a baixo, ele inicia pegando qualquer caracter que comece
    de A até Z em caixa alta. Depois o proximo caracter é um espaço em
    branco " " que pode ou não existir logo seguido de um ou mais caracteres
    de A até Z em caixa alta que devem existir. O próximo caracter a ser
    considerado é um espaço vazio " "  logo seguido se caracteres de A até Z
    em caixa alta que podem ou não existir.
    O [] na formula da regex é uma correção feita para que a regex não quebre
    a string em 2."""
    regex = r"[A-Z][]\s*[A-Z]+\s*[A-Z]*"
    string_encontrados = re.findall(regex, texto)
    tamanho_string_original = len(texto)
    if len(string_encontrados) != 0:
        tamanho_string_achada = len(string_encontrados[0])
    else:
        return False
    if tamanho_string_achada == tamanho_string_original:
        return True
    else:
        return False

def exe5(texto):
    """"""
    pass


# casos_positivos = ["ALEX TORQUATO SOUZA CARNEIRO", "MARIA ARAUJO",
#                    "JOSE DA SILVA", "ANA APARECIDA"]
# casos_negativos = ["123", "!@3%$ˆ)(*&", "$@#", "alex torquato souza carneiro",
#                    " ", "", "JOSÉ DA SILVA", "MaRIa aRaUJo",
#                    "ana aparecida", "MAR1A ARAUJO", "100.2", ".00",
#                    "@N@ @P@RECID@", "JOSE.DA.SILVA", ".ANA APARECIDA",
#                    " MARIA ARAUJO"]


import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorLexico import elementos_del_lenguaje
from sys import stdin

predecencias = 
(
    ('right', )
    ('left', '+', '-')
    ('left', '*', '/')
)


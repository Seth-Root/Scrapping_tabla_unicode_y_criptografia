# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
from prettytable import PrettyTable
import os, subprocess, re

try:
    f=open("lista_en.txt")
    lista_bajada =  f.read()
    f.close()
except:
    crear_LISTA_unicode = subprocess.call("touch lista_en.txt", shell=True)
    f=open("lista_en.txt","w")
    lista_bajada =  f.read()
    f.close()

if lista_bajada == False:

    url_unicode = "https://www.sciencebuddies.org/science-fair-projects/references/table-of-8-bit-ascii-character-codes"

    page = urllib2.urlopen(url_unicode)
    soup = BeautifulSoup(page, "lxml")

    name_box = soup.find('div', attrs={'class': 'content-table page-break-avoid'}) 


    name_boxaaa = soup.find('table')  
    table_headers = name_boxaaa.find_all('tr')
    contable = 0
    lista_unicode = []
    for row in table_headers:
    #if contable < 3:
        lista_unicode.append(str(row))
        contable +=1
    print contable

else:
    contable = 0
    lista_bajada = eval(lista_bajada)
    diccionario_unicode = {}
    for TRs in lista_bajada:
        contable +=1
        print contable
        print TRs
        
        TDs_por_cada_TR = re.findall('<td>([\S* ]+)</td>', TRs)
        Lista_tds = []
        for TDs in TDs_por_cada_TR:
            Lista_tds.append(TDs)
        if "&lt;" in TRs:
            pop_despues= Lista_tds.pop(-1)
            Lista_tds.append("&lt;")
            Lista_tds.append(pop_despues)
        print Lista_tds
        valor = Lista_tds[4]
        Lista_tds.pop(4)
        print Lista_tds
        print Lista_tds[4]
        diccionario_unicode[valor]= Lista_tds
        
        
            
        print " "
        print " "
print diccionario_unicode
print diccionario_unicode["A"]




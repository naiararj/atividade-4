import datetime

n = str(input('digite seu nome:')).strip()
nome = n.split()
print(n.capitalize())
ano = eval(input('nasceu em que ano:'))
mes = eval(input('nasceu em que mês:'))
dia = eval(input('nasceu em que dia:'))
date = ('ano = 1991, mês = 5, dia = 21')
txt = (input('Ana nasceu no dia:'))
print(txt . format(datetime.date(1991,5,21)))


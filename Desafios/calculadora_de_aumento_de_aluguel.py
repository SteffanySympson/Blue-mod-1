# -*- coding: utf-8 -*-
"""Calculadora_de_aumento_de_aluguel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RHmO9qco1UcVD__L0gaFnpWV-PD9DjS6

<a href="https://colab.research.google.com/github/SteffanySympson/Blue-mod-1/blob/main/Calculadora_de_aumento_de_aluguel.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Vamos construir um programa que irá calcular o aumento anual do seu aluguel.

A sua calculadora vai receber o valor do aluguel e calcular o aumento baseado no IGPM de 31%. A calculadora deve apresentar o aluguel reajustado no formato R$ XXXX.XX
"""

#Imputar o valor do aluguel
#variável IGPM de 31% = 0.31

igpm = 0.31

nome = input ("Qual o seu nome? ")
print ("Olá!!! Bem vindo (a) " +nome, "a calculadora de aluguel!")
print ()
Aluguel = float (input ("Informe o valor em Reais - R$ - do seu aluguel: "))
Aumento = (Aluguel * igpm)
print ()
print (f"Total de Aumento: R$ {(Aumento):.2f}")
print (f"Valor Atualizado: R$ {(Aluguel + Aumento):.2f}")
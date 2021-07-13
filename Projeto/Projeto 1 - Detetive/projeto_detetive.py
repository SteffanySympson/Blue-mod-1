# -*- coding: utf-8 -*-
"""Projeto Detetive.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bpPg2LT7h1idJRCZy7vtg41RP0ZvRE5I

**Projeto 01 – Detetive**

Perguntas:

• "Você telefonou para a vítima?"
• " Você esteve no local do crime?"
• " Você mora perto da vítima?"
• " Você devia para a vítima?"
• " Você já trabalhou com a vítima?"
"""

print ("Desafio do Detetive")
print ()
nome_suspeito = input ("Diga seu nome para começar o interrogatório:")
print ("Muito bem ", nome_suspeito.title(), "vamos começar!")
print()
pergunta1 = input ("Você telefonou para a vítima?\n S/N: ").strip().capitalize().replace('a','ã')
if pergunta1 == "Sim":
  resp1 = 1
else:
  resp1 = 0

pergunta2 = input ("Você esteve no local do crime? \n S/N: ").strip().capitalize().replace('a','ã')
if pergunta2 == "Sim":
  resp2 = 1
else:
  resp2 = 0

pergunta3 = input ("Você mora perto da vítima? \n S/N: ").strip().capitalize().replace('a','ã')
if pergunta3 == "Sim":
  resp3 = 1
else:
  resp3 = 0

pergunta4 = input ("Você devia para a vítima? \n S/N: ").strip().capitalize().replace('a','ã')
if pergunta4 == "Sim":
  resp4 = 1
else:
  resp4 = 0

pergunta5 = input ("Você já trabalhou com a vítima? \n S/N: ").strip().capitalize().replace('a','ã')
if pergunta5 == "Sim":
  resp5 = 1
else:
  resp5 = 0

soma = resp1 + resp2 + resp3 + resp4 + resp5
print()

if soma <= 1:
  print ("Você é inocente e está livre!")
elif soma == 2:
    print ("Você é um suspeito dessa investigação. Não saia da cidade!")
elif soma == 3 or soma == 4:
    print ("Você é cúmplice do crime. Entregue o assassino para reduzir sua pena!")
else:
  print ("Você é o culpado e está preso!")

print ()
print ("Fim da investigação!")
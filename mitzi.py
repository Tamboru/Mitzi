#!/usr/bin/env python3.6
# Versão: 0.3

# Variáveis:
info = "uashdua"

# Script

print ("\033[1;34m--------------------------------------------------------------\033[1;34m")
print ("|                                                            |")
print ("|                Bem vindo ao chatbot Mitzi                  |")
print ("|                                                            |")
print ("--------------------------------------------------------------\n")
#Indentifica-se-há-um-nome------------------------------------------------------------------------------
try: 
    nome_existente = open(".nome", "r")

except IOError:
    print ("\033[1;35mMitzi" "\033[0m: Olá! Qual é seu nome?")
    nome = input("\033[1;32mVocê" "\033[0m: ")
    print ("\033[1;35mMitzi" "\033[0m: Olá", nome+"," " como vai você?")
    novo_nome = open(".nome", "a")
    novo_nome.write(nome)
    novo_nome.close()

else:
    nome_existente = open(".nome", "r")
    nome = nome_existente.read()
    print ("\033[1;35mMitzi" "\033[0m: Olá", nome+"," " como vai você?")
    nome_existente.close()

#Loop-de-conversa---------------------------------------------------------------------------------------
while(info != "tchau"):
	info = input("\033[1;32mVocê" "\033[0m: ")
	info = info.lower()

	if info == ("tchau"):
		
		print ("\033[1;35mMitzi" "\033[0m: Ok, até a próxima!")
		exit()
		
	else:

		try:
			responder = open("cérebro/" + info, "r")
	
		except IOError:
			print ("\033[1;35mMitzi" "\033[0m: Ainda não sei o que você quis dizer, o que eu deveria responder?")
			resposta = input("\033[1;32mVocê" "\033[0m: " "\033[1;35m[Resposta literal]: \033[0m")
			novo_arquivo = open("cérebro/" + info, "a") 
			novo_arquivo.write(resposta)
			print ("\033[1;35mMitzi" "\033[0m: Certo, devo falar " "\033[0;34m[", resposta, "]")
			
		else:
			responder = open("cérebro/" + info, "r")
			falar = responder.read()
			print ("\033[1;35mMitzi" "\033[0m: " + falar)
#------------------------------------------------------------------------------------------------------

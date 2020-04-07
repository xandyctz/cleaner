import os
import sys
import time
import asyncio

temp = 'C:\\Windows\\Temp'
confirmar = 'Deseja excluir esses arquivos? S/n ==> '


def main():
	os.system('cls')
	print('===== Clear =====')
	print('Author: Xandy')
	print('Version: 1.0.0')
	print('===== Clear =====')
	print('\n')
	print('1 - Limpar a pasta TEMP')
	print('2 - Limpar a pasta %TEMP%')
	print('3 - Limpar a pasta Prefetch')
	print('4 - Limpar todas pastas acima')
	print('0 - Sair')
	print('\n')
	resposta = input('Escolha uma opcao: ')

	
	if resposta == '1':
		if os.listdir(temp):
			clearTemp()
		else:
			print('Pasta TEMP vazia... Retornando para o menu...')
			time.sleep(2)
			main()
	elif resposta == '2':
		clearOutherTemp()
	elif resposta == '3':
		clearPrefetch()
	elif resposta == '4':
		clearAll()
	elif resposta == '0':
		print('Saindo...')
		time.sleep(1)
		return
	else:
		print('Opcao invalida...')
		time.sleep(1)
		main()


def clearTemp():
	os.chdir(temp)
	print('')
	for files in os.listdir(temp):
		print(files)
	print('')
	resposta = str(input(confirmar))
	if resposta == 'S' or resposta == 's':
		print('Limpando...')
		time.sleep(1)
		os.system('rmdir %s /S /Q'%temp)
		time.sleep(1)
		if not os.listdir(temp):
			print('')
			print('Pasta TEMP limpada com sucesso... Retornando para o menu...')
			time.sleep(1)
			main()
		else:
			print('Algo deu errado...')
	elif resposta == 'N' or resposta == 'n':
		print('Cancelando...')
		time.sleep(1)
		os.system('cls')
		main()
	else:
		print('Opcao invalida...')
		clearTemp()

def clearOutherTemp():
	print('clearOutherTemp')

def clearPrefetch():
	print('clearPrefetch')

def clearAll():
	print('clearAll')

main()
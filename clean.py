import os
import sys
import time
import asyncio

temp = 'C:\\Windows\\Temp'
temp2 = 'C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp'
prefetch = 'C:\\Windows\\Prefetch'
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
		if os.listdir(temp2):
			clearOutherTemp()
		else:
			print('Pasta %TEMP% vazia... Retornando para o menu...')
			time.sleep(2)
			main()

	elif resposta == '3':
		if os.listdir(prefetch):
			clearPrefetch()
		else:
			print('Pasta Prefetch vazia... Retornando para o menu...')
			time.sleep(2)
			main()

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
		main()
	else:
		os.system('cls')
		print('Opcao invalida...')
		clearTemp()

def clearOutherTemp():
	os.chdir(temp2)
	print('')
	for file in os.listdir(temp2):
		print(file)
	print('')
	resposta = str(input(confirmar))

	if resposta == 'S' or resposta == 's':
		print('Limpando...')
		time.sleep(1)
		os.system('rmdir %s /S /Q'%temp2)
		time.sleep(1)
		if not os.listdir(temp2):
			print('')
			print('Pasta TEMP limpada com sucesso... Retornando para o menu...')
			time.sleep(1)
			main()
		else:
			print('Algo deu errado...')


def clearPrefetch():
	# os.chdir acessa a pasta prefetch
	os.chdir(prefetch)
	print('')
	for files in os.listdir(prefetch):
		print(files)

	print('')
	resposta = str(input(confirmar))

	if resposta == 'S' or resposta == 's':
		print('Limpando...')
		time.sleep(1)
		try:
			os.system('rmdir %s /S /Q'%prefetch)
		except:
			print('Erro ao tentar excluir os arquivos...')
		time.sleep(1)

		if not os.listdir(prefetch):
			print('')
			print('Pasta Prefetch limpada com sucesso... Retornando para o menu...')
			time.sleep(1)
			main()
		else:
			print('Algo deu errado...')

	elif resposta == 'N' or resposta == 'n':
		print('Cancelando...')
		time.sleep(1)
		main()
	else:
		os.system('cls')
		print('Opcao invalida...')
		clearPrefetch()

def clearAll():
	print('clearAll')

main()
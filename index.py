import math

def main():
	print 'Validacao de codigos EAN'

	#objFile = open('EAN-Tabela 1.csv', 'r')
	objFile = open('MLBItemsEan-v2.csv', 'r')

	qtdValidos = 0
	qtdNacionais = 0
	qtdImportados = 0

	# pula a primeira linha, cabecalho
	objFile.readline()
	qtdLida = 0

	for line in objFile:
		# codigo = os 13 primeiros caracteres
		codigo = line[:13]
		if validaCodigo(codigo):
			qtdValidos += 1
			# nacionais comecam com 789 ou 790
			if (codigo[0:3] == '789') or (codigo[0:3] == '790'):
				qtdNacionais += 1
			else:
				qtdImportados += 1

		qtdLida += 1
		#if qtdLida > 10:
		#	break

	print 'Total de codigos = ' + str(qtdLida)
	print 'EAN validos = ' + str(qtdValidos)
	print 'EAN nacionais = ' + str(qtdNacionais)
	print 'EAN importados = ' + str(qtdImportados)
	objFile.close()


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


def validaCodigo(codigo):
	# valida para o codigo ter apenas numeros
	for c in codigo:
		if (c != '0') and (c != '1') and (c != '2') and (c != '3') and (c != '4') and (c != '5') and (c != '6') and (c != '7') and (c != '8') and (c != '9'):
			return False

	par = True
	soma = 0
	check = 0
	# calculo eh: pegar cada posicao menos o digito, multiplicar por 1 ou por 3 alternadamente, somar, e subtrair do proximo arredondamento de 10
	for digit in codigo[:12]:
		soma += int(digit) if par else (int(digit)*3)
		par = not par

	check = roundup(soma) - soma
	#print codigo[12:13] + ' = ' + str(check)
	return True if codigo[12:13] == str(check) else False

if __name__ == "__main__":
    main()

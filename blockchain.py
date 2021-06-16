'''

Alcala Coin

p1: Make a save blockchain
p2: Try to hack it
p3: Limit the transactions per block

HASH USE SHA256


BLOCK1('START',t1,t2,t3...) -> HASH_CODE_1
BLOCK2(HASH_CODE_1,t4,t5,t6...) -> HASH_CODE_2
BLOCK3(HASH_CODE_2,t7,t8,t9...) -> HASH_CODE_3

'''

import hashlib
import random



#Esta seria la cadena de bloques
class BlockChain:
	def __init__(self,blocks):
		self.blocks=blocks
	def add_block(self,block):
		self.blocks.append(block)


class Block:

	def __init__(self,previous_block,transaction_list,delimitador=3):
		self.previous_block=previous_block
		#hacemos una copia del la lista de transacciones anterior para poder manipularla
		self.transaction_list_principal=transaction_list
		self.transaction_list_restante=self.transacciones_restantes()
		self.transaction_list=transaction_list[:delimitador]


		self.block_data='-'.join(transaction_list)+'-'+previous_block

		#Llamamos a los datos previamente cargados como si fuera un bloc de notas
		#Con transacciones y la codificamos con hexdigest lo pasamos a string

		self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
		self.delimitador=delimitador
	def transacciones_restantes(self):

		try:
			transaction_list_restante=self.transaction_list_principal[delimitador:]
		except:
			transaction_list_restante=self.transaction_list_principal

		return transaction_list_restante


#We generate  amount of transactiones
def transacciones(transaccion):
	lista_transacciones=[]
	for i in range(transaccion):
		coin=random.randrange(1,10)#Generamos numeros aleatorios del 1 al 10
		t="x send "+str(coin)+" to y"
		lista_transacciones.append(t)

	return lista_transacciones


#Transactions Checker
def checker(block1,block2):
	if block1==block2:
		print("Todo Correcto")
	else:
		print("Han intentado hackear el bloque")


#Transactions

t1=transacciones(25)



#Hacked Transaction



t3_hacked=transacciones(10)



#Bloques
first_block=Block("Genesis",t1)
second_block=Block(first_block.block_hash,first_block.transaction_list_restante)
third_block=Block(second_block.block_hash,second_block.transaction_list_restante)
four_block=Block(third_block.block_hash,third_block.transaction_list_restante)

#Hacked Blocks
first_block=Block("String",t1)
second_block=Block(first_block.block_hash,first_block.transaction_list_restante)
third_block_h=Block(second_block.block_hash,t3_hacked)
four_block_h=Block(third_block_h.block_hash,third_block_h.transaction_list_restante)



'''
Como podemos ver hasta la tercera transaccion los bloques son iguales al cambiar una
transaccion cambiria el resto de bloques qeu la siguen

'''
#BlockChain vacio

cadena_1=BlockChain([])
cadena_2=BlockChain([])

#Miramos el seguimiento de las 2 cadenas

#--Cadena 1

cadena_1.add_block(first_block)
cadena_1.add_block(second_block)
cadena_1.add_block(third_block)
cadena_1.add_block(four_block)

#--Cadena 2

cadena_2.add_block(first_block)
cadena_2.add_block(second_block)
cadena_2.add_block(third_block_h)
cadena_2.add_block(four_block_h)


#Miramos su historial de hases
print("Historial de bloques")
for block_chain in [cadena_1,cadena_2]:
	for block in block_chain.blocks:
		print(block.previous_block)
	print("-------------------------------------------------------")
#Con esto podemos comprobar que os hases de dos cadenas de bloque que son disitintas
#En este caso un hacker habria intentado falsificar un bloque por lo que se generaria
#otra cadena de bloques pero sera aceptada la cadena de bloques que mine mas rapido los
#siguientes bloques por lo que la cadena_2 sera desechada


#Comprovamos que si hay algun bloque corrupto
print("Comprovamos si es valido")
checker(four_block.block_hash,four_block_h.block_hash)

print("-------------------------------------------------------")

#Transacciones que se han quedado por minar
print("Transacciones restantes")
print(four_block_h.transaction_list_restante)
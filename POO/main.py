from classes import Escritor, Caneta, MaquinaDeEscrever


escritor = Escritor("João Ubaldo Ribeiro")
caneta = Caneta("BIC")
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()


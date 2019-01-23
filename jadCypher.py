from jad import Jad

def string_to_bit_array(text):#Convierte un string a una lista de bits
                                
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Obtiene el valor del char en un byte
        array.extend([int(x) for x in list(binval)]) #Agrega una lista de los bits del char a otra lista
    return array

def bit_array_to_string(array): #Transforma un alista de bits a un string
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Retorna el valor binario como string de un largo dado 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "el valor binario es mas largo que el tamaño esperado"
    while len(binval) < bitsize:
        binval = "0"+binval #Agrega ceros necesarios para cumplir con el largo
    return binval

def nsplit(s, n):#Divide una lista en sublistas de tamaño n
    return [s[k:k+n] for k in range(0, len(s), n)]

def avalancha(t1,t2):
    contador = 0
    largo = 0
	
    #t1bit = string_to_bit_array(t1)
    #t2bit = string_to_bit_array(t2)
    t1bit = t1
    t2bit = t2
    if len(t1bit) > len(t2bit):
        largo = len(t2bit)
    else:
        largo = len(t1bit)
    for i in range(len(t1bit)):
        if(t1bit[i] != t2bit[i]):
            contador +=1
    print(contador/largo)
    
class JadCypher():
    def __init__(self):
        self.blocks = list()
        self.vi = list()
    
    def generateBlocks(self,text,size_block):
        self.blocks = []
        blocks = nsplit(text, size_block)
        for block in blocks:
            self.blocks.append(string_to_bit_array(block))
        
    def initvi(self,size_block):
        self.vi = string_to_bit_array("\x00"*size_block)
    
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
    
    def addPadding(self,text,size_block):
        if(len(text) % size_block == 0):
            return text
        pad_len = size_block - (len(text) % size_block)
        for i in range(pad_len):
            text += " "
        return text
    
    def encrypt(self,text,password,size_block):
        result = ""
        text = self.addPadding(text,size_block)
        self.generateBlocks(text,size_block)
        self.initvi(size_block)
        jad = Jad()
        for i in range(len(self.blocks)):
            xor = self.xor(self.vi,self.blocks[i])
            textXor = bit_array_to_string(xor)
            print(len(textXor))
            encryp = jad.encrypt(textXor,password,len(textXor))
            self.vi = string_to_bit_array(encryp)
            result += encryp
        return result 

    def decrypt(self,text,password,size_block):
        result = ""
        self.generateBlocks(text,size_block)
        self.initvi(size_block)
        jad = Jad()
        for i in range(len(self.blocks)):
            texto = bit_array_to_string(self.blocks[i])
            print(len(texto))
            decryp = jad.decrypt(texto,password,len(texto))
            plaintext = self.xor(self.vi,string_to_bit_array(decryp))
            self.vi = self.blocks[i]
            
            result += bit_array_to_string(plaintext)
        return result

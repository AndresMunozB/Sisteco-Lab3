


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
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Agrega ceros necesarios para cumplir con el largo
    return binval

def nsplit(s, n):#Divide una lista en sublistas de tamaño n
    return [s[k:k+n] for k in range(0, len(s), n)]

def addPadding(text,size_block):
        if(len(text) % size_block == 0):
            return text
        pad_len = size_block - (len(text) % size_block)
        for i in range(pad_len):
            text += " "
        return text

string = "hola"
#Por cada letra hay 8 bits.
arrayBits = string_to_bit_array(string)
arraySplit = nsplit(arrayBits,8)
hola = [''.join([str(x) for x in bytes]) for bytes in  nsplit(arrayBits,8)]
print("string:", string)
print("array :", arrayBits)
print("arrayS :", arraySplit)
print("texto: ", bit_array_to_string(arrayBits))

texto = "holacomoestasbi2412321321"
largo = len(texto)
print("texto:", texto, "largo: ", largo)
texto = addPadding(texto,8)
largo = len(texto)
print("texto:", texto, "largo: ", largo)

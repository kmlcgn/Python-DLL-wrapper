import ctypes
 
#loading dll file 

DLLFile = ctypes.CDLL("path/to/dll/file") 
#Simple function call with no return type, -first function
DLLFile.foo()
 
#Second function, Passing integer type arguments and returning sum
print("\nSum:" , (DLLFile.MyAdd(4,5)))
 
print(DLLFile)
 
#Passing a String to dll
DLLFile.textreturn.argtypes = [ctypes.c_char_p,ctypes.c_char_p,ctypes.c_size_t] #defining the datatype of arguments
DLLFile.textreturn.restype = ctypes.c_char_p #defining return type
 
phrase = b"Hello"
result = ctypes.create_string_buffer(100)
res = DLLFile.textreturn(phrase,result,ctypes.sizeof(result))
print(res)
print(result.value)
 

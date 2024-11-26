stack=[]

#push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)
print("stack setelah push",stack)

#pop elemen dari stack
elemen=stack.pop()
print("elemen yang di pop pertama",elemen)
print("stack setelah pop pertama",stack)

#peek elemen teratas
if stack:
    print("elemen teratas",stack[-1])
else:
    print("stack kosong")

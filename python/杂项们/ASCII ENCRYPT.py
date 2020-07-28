def encrpt(txt):
    lst=[]
    for i in txt:
        lst.append(ord(i))
    return(lst)
def imp():
    txt=str(input("type sth."))
    print(encrpt(txt))

imp()
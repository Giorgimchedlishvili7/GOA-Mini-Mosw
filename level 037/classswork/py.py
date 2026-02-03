#mutabble is when an object can be changed after its creation
#immutable is when an object cannot be changed after its creation

name1 = ["Giorgi", "mariko", "nino"]  

name1.pop(0)
name1.insert(2, "Gio")
name1.insert(3, "Avto")
len(name1)
print(name1)

int1 = [11, 4, 9]
int1.reverse()
int1.pop(1)
int1.insert(1, 11)
print(int1)
class a:
    class b:
        value = 3




x = a

setattr(getattr(a,'b'),"value",6)



print(a.b.value)
# 493 a
count = 0
with open('f.txt') as f:
    abobus = "".join(f.readlines())

    abobus = abobus.replace("ab", "♂")

    count = abobus.count("♂")
    print("Кол-во вхождений ab равно", count)


    

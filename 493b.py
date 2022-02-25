# 493b
with open("f.txt") as f:
    if "".join(f.readlines()).find("abcdefg") != -1:
        print("В файл ВХОДИТ сочетание abcdefg")
    else:
        print("В файле НЕТ сочетания abcdefg")

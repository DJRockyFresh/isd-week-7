sl = []
item = input("What is needed? ")
while item != "":
    sl.append(item)
    item = input("What is needed? ")
    if item == "":
        print("List:", sl)

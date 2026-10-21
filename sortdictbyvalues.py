D={"a":5,"b":4,"c":3,"d":2,"e":1}
print(dict(sorted(D.items(), key=lambda item: item[1])))

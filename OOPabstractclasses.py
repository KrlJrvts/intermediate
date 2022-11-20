
class MyFieldVin(str):
    def __new__(cls, string):
        obj = [super.__new__(cls, "wrong length"), super().__new__(cls, string)][len(string) == 3]
        return obj


vin = MyFieldVin("etc")
vin1 = MyFieldVin("as")
c = vin1.count("e")

print(f"{c =}")
print(f"{vin = }")
print(f"{vin = }")

from main import mins, maxs, sums, mul

data = []
with open("data.txt", 'r') as file_obj:
    data = list(map(int, file_obj.read().split()))

print("max=", maxs(data))
print("min=", mins(data))
print("proizvedenie=", mul(data))
print("summa=", sums(data))

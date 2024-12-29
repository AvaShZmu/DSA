a = 2
M = 19
input = [19, 5, 1, 18, 3, 8, 24, 13, 16, 12]
results_mod = []
for i in input:
    if a*i % M in results_mod:
        print("False")
        print(i)
        break
    results_mod.append(a*i % M)
else:
    print("True")

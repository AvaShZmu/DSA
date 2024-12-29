if __name__ == "__main__":
    input = [19, 5, 1, 18, 3, 8, 24, 13, 16, 12]
    M_list = []
    a = 1
    for i in range(max(input)):
        M = len(input)
        while True:
            results = []
            for i in input:
                if a*i % M in results:
                    M += 1
                    break
                results.append(a*i % M)
            else:
                M_list.append(M)
                break
        a += 1

    print(M_list)
    minimum = min(M_list)
    for i in range(len(M_list)):
        if M_list[i] == minimum:
            print(f"a = {i+1}, M = {M_list[i]}")
            break

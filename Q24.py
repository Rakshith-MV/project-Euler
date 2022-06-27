S = ['0','1','2','3','4','5','6','7','8','9']
n = len(S)
first = [None]
for i in range(n):
    first = [str(i)]
    for count in range(n):
        print("for first term = ",i)
        new = []
        for j in first:
            temp_S = []
            for some in S:
                temp_S.append(some)
            for digits in j:
                if digits in temp_S:
                    temp_S.remove(digits)
            
            for k in temp_S:
                new.append(j+k)
        first = new
        print(new)
        F = open("Q24.txt",'r')
        for s in F:
            F.write(s)
        print(len(new))
        if len(first) != 0:
            final = new
        f = input("common")
    print(final,len(final))
    if f == 's':
        break
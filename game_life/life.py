import random
w = 15
h = 10

# def rand:
#     random.randint(0,1)

grille =  [['■' if random.randint(0,1) == 1 else '□' for _ in range(w)] for _ in range(h)]


# for _ in range(h):
#     grille.append('■'*w)

for l in grille:
    for i in l:
        print(i,end='')
    print('')

print(random.randint(0,1))
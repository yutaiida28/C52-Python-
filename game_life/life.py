import random
w = 15
h = 10

# def rand:
#     random.randint(0,1)

# grille =  [['■' if random.randint(0,1) == 1 else '□' for _ in range(w)] for _ in range(h)]
grille =  [['1' if random.randint(0,1) == 1 else '0' for _ in range(w)] for _ in range(h)]


# for _ in range(h):
#     grille.append('■'*w)

for i in range(w):
    for j in range(h):
        if i == 0 or i == w - 1 or j == 0 or j == h - 1:
            grille[j][i] = 0


for l in grille:
    for i in l:
        print(i,end='')
    print('')



            

print(random.randint(0,1))
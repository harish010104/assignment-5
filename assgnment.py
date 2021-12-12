n = 5;
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


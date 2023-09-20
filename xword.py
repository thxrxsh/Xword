print("""

\t,_,_,_,_,_,_,_,_,_|______________________________________________________
\t| | |X|W|0|R|D| | |_____________________________________________________/
\t'-'-'-'-'-'-'-'-'-|----------------------------------------------------'

\tv-1.0
""")

lst = []
matrix = {}
x = 0

output_name = input("Enter the name of outputfile : ")

with open(output_name,"w") as wordlist:
  while (True):
    word = input('Enter words and enter 0 to stop :')
    if (word == '0'):break
    lst.append(word)

  for i in range(3):
    matrix[str(i)] = lst

  for a in matrix['0']:
    wordlist.write(a+"\n")

    for b in matrix['1']:
      wordlist.write(a+b+"\n")
    
      for c in matrix['2']:
        wordlist.write(a+b+c+"\n")

print("[✓]  Word list created successfuly ")

# [[file:README.org::*Udvikling af logik][Udvikling af logik:1]]
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog
inputchoice=input("Skriv 1 for at oversætte til røversprog eller 2 for at oversætte fra røversprog\n")
inputtekst=input("")

def oversaet_til_roeversprog(inputtekst):
    outputtekst= ""
    consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    for i in inputtekst:
        if i.lower in consonants:
            outputtekst += i+"o"+i
        else:
            outputtekst += i
    print(outputtekst)
    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
    outputtekst = ""
    roeversprog=['bob','coc','dod','fof','gog','hoh','joj','kok','lol','mom','pop','qoq','ror','sos','tut','vov','waw','xox','zoz']
    for i in range(roeversprog[i]): 
        if i is i+"o"+i:
            outputtekst -= "o"+i
        else:
            outputtekst += i   
    return outputtekst 
# Udvikling af logik:1 ends here
if inputchoice == 1:
    oversaet_til_roeversprog(inputtekst)
elif inputchoice == 0:
    oversaet_fra_roeversprog_til_andet_sprog(inputtekst)


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
    i = 0
    while i < len(inputtekst):
        bogstav = inputtekst[i]
        # Hvis vi finder et mønster som konsonant + 'o' + samme konsonant, springer vi det rigtige antal tegn over
        if (i+2 < len(inputtekst) and
            inputtekst[i].lower() == inputtekst[i+2].lower() and
            inputtekst[i+1] == 'o' and
            inputtekst[i].lower() in "bcdfghjklmnpqrstvwxz"):
            outputtekst += bogstav
            i += 3
        else:
            outputtekst += bogstav
            i += 1
    return outputtekst
# Udvikling af logik:1 ends here
if inputchoice == "1":
    print(oversaet_til_roeversprog(inputtekst))
elif inputchoice == "2":
    print(oversaet_fra_roeversprog(inputtekst))
else:
    print("Ugyldigt valg")


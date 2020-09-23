# Skriv en rekursiv funksjon som beregner lengden på
# en streng. Du kan ikke bruke len () -funksjonen
# mens du beregner lengden på strengen.
# Du må stole på funksjonen du skriver.
# Sett denne funksjonen i et program som ber
# brukeren om å legge inn en streng og deretter skrive ut
# lengden på den strengen.


# for hvert rekursive kall, fjern et tegn fra strengen
# str[1:] spiser seg gjennom strengen fra høyre mot venstre
def calculate_length(str):
    if str == '':
        return 0
    return 1 + calculate_length(str[1:])


str = calculate_length("Dette er en streng med 31 tegn.")
for char in len(str):
    print(char, str)
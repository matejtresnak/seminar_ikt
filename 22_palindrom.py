import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def JePalindrom(vstup):
    vstup_reverse = vstup[::-1]
    for i in range(round(len(vstup)/2)):
        if vstup[i] != vstup_reverse[i]:
            return False
    return True

vstup = "kobyla má malý bok"
vstup = vstup.replace(" ","")
vstup = vstup.lower()
print(JePalindrom(strip_accents(vstup)))

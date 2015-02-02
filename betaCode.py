import betaCodeTables
# conversionFlow: betaCode > translit > Arabic

# Needed:
#   - table of conversion (betacode > translit; translit > Arabic)
#   - tagging Arabic words
#   - tagging Arabic text

# define replacement with dictionaries
def dictReplace(text, dic):
    for k, v in dic.items():
        text = text.replace(k, v)
        if len(v) > 1:
            vUpper = v[0].upper()+v[1:]
        else:
            vUpper = v.upper()
        text = text.replace(k.upper(), vUpper)
    return(text)

def dictReplaceRev(text, dic):
    for k, v in dic.items():
        text = text.replace(v, k)
        text = text.replace(v.upper(), k.upper())
    return(text)

def betacodeToTranslit(text):
    text = dictReplace(text, betaCodeTables.betacodeTranslit)
    return(text)

def translitToSearch(text):
    text = dictReplace(text, betaCodeTables.translitSearch)
    return(text)

def translitToArabic(text):
    pass


testString = "qul a`_u_du bi-l-Ll~ahi min al-^Say.t_ani al-ra^g_imi"

print(betacodeToTranslit(testString))
print(translitToSearch(betacodeToTranslit(testString)))



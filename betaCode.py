import re

# import conversion tables
import betaCodeTables

# conversionFlow: betaCode > translit > Arabic

# Needed:
#   - table of conversion (betacode > translit; translit > Arabic)
#   - tagging Arabic words
#   - tagging Arabic text

# COMPLEX RULES:
# vowel case endings add "_", i.e.:
#       f_i al-kit_abi_, but not:
#       f_i al-kit_abi.n
# attached prepositions/conjunctions must be separated with "-", i.e.:
#       bi-Llahi_
#       fa-_dahaba_
# tāʾ marbūṭaŧ: add + after tāʾ marbūṭaŧ, if the first word of idafa
#       `_amma:t+u Ba.gd_ada, but
#       al-`_amma:tu f_i Ba.gd_ada


# define replacement with dictionaries
def dictReplace(text, dic):
    for k, v in dic.items():
        k = k.strip()
        v = v.strip()
        text = text.replace(k, v)
        if len(v) > 1:
            vUpper = v[0].upper()+v[1:]
        else:
            vUpper = v.upper()
        text = text.replace(k.upper(), vUpper)
    return(text)

# conversion functions
def betacodeToTranslit(text):
    print("betacodeToTranslit()")
    text = dictReplace(text, betaCodeTables.betacodeTranslit)
    text = re.sub("\+|_", "", text)
    return(text)

def betacodeToSearch(text):
    print("betacodeToSearch()")
    text = dictReplace(text, betaCodeTables.betacodeTranslit)
    # fixing tāʾ marbūṭaŧs
    text = re.sub(r"ŧ\+", r"t", text)
    text = re.sub(r"ŧ", r"", text)
    text = dictReplace(text, betaCodeTables.translitSearch)
    text = re.sub("\w_", "", text)
    return(text)

def betacodeToLOC(text):
    print("betacodeToLOC()")
    text = dictReplace(text, betaCodeTables.betacodeTranslit)
    # fixing tāʾ marbūṭaŧs
    text = re.sub(r"ŧ\+", r"t", text)
    text = re.sub(r"ŧ", r"", text)
    text = dictReplace(text, betaCodeTables.translitLOC)
    text = re.sub(r"\w_", r"", text)
    return(text)

def betacodeToArabic(text):
    print("betacodeToArabic()")
    text = dictReplace(text, betaCodeTables.betacodeTranslit)
    text = re.sub('\+' , '', text)

    # complex combinations
    sun = "tṯdḏrzsšṣḍṭẓln"
    text = re.sub(r"\b[aA]l-([%s])" % sun, r"ﭐل-\1\1", text) # converts articles w/ sun letters
    text = re.sub(r"\b[aA]l-", r"ﭐلْ-", text) # converts articles
    text = re.sub(r"\bwa-a?l-", "وَﭐل-", text) # converts articles
    #text   = re.sub(r"n-", "", text) # converts articles

    text = re.sub("[Aa]llãh", " ﭐلـلّٰـه ".strip(), text) # Convert God's Name
    text = re.sub(r"li-[Ll]lãhi", " لِـلّٰـهِ ".strip(), text) # Convert God's Name
    text = re.sub(r"\bb\.", "بن", text) # Convert b. into ar bn

    text  = re.sub(",", "،", text) # Convert commas

    # fixes initial Alifs
    text = re.sub("\\b[Aa]", "أَ", text)
    text = re.sub("\\b[Ii]", "إِ", text)
    text = re.sub("\\b[Uu]", "أُ", text)
    text = re.sub("\\b[Āā]", "آ", text)
    text = re.sub("\\b[Īī]", "إِي", text)
    text = re.sub("\\b[Ūū]", "أُو", text)

    # gemminated consonants: replaces the second one with tašdīd
    cnsnnts = "btṯǧčḥḥḫdḏrzsšṣḍṭẓʿġfḳkglmnhwy"
    text = re.sub(r"([%s])\1" % cnsnnts, r"\1" + " ّ ".strip(), text)
    # two consonants into C-sukun-C
    text = re.sub(r"([%s])([%s])" % (cnsnnts,cnsnnts), r"\1%s\2" % " ْ ".strip(), text)
    # final consonant into C-sukun
    text = re.sub(r"([%s])(\s|$)" % (cnsnnts), r"\1%s\2" % " ْ ".strip(), text)
    # consonant + long vowel into C-shortV-longV
    text = re.sub(r"([%s])([Āā])" % (cnsnnts), r"\1%s\2" % " َ ".strip(), text)
    text = re.sub(r"([%s])([Īī])" % (cnsnnts), r"\1%s\2" % " ِ ".strip(), text)
    text = re.sub(r"([%s])([Ūū])" % (cnsnnts), r"\1%s\2" % " ُ ".strip(), text)

    # tanwins
    text = re.sub('aȵ' , ' ً '.strip(), text)
    text = re.sub('uȵ' , ' ٌ '.strip(), text)
    text = re.sub('iȵ' , ' ٍ '.strip(), text)


##
##    # arVlong  = "[ãáāĀīĪūŪ]"
##    nameAr   = re.sub(r"(ūw)", r"w", nameAr) # fixes long vowel+weak consonant combinations
##    nameAr   = re.sub(r"(īy)", r"y", nameAr) # fixes long vowel+weak consonant combinations 
##    nameAr   = re.sub(r"(%s)\1*" % arCtrans, r"\1", nameAr) # removes double letters: sukkariyyat > sukariyat
##    if re.search("ʾ", nameAr):
##      # medial: vowel + hamza + consonant (chair corresponds to preceeding vowel)
##      nameAr = re.sub(r"[āĀ]ʾi", r"ائ", nameAr)
##      nameAr = re.sub(r"[aA]ʾī", r"ئي", nameAr)
##      nameAr = re.sub(r"[āĀ]ʾī", r"ائي", nameAr)
##      nameAr = re.sub(r"[uU]ʾā", r"ؤا", nameAr)
##      
##      nameAr = re.sub(r"aʾa", r"أ", nameAr)
##      nameAr = re.sub(r"aʾi", r"ئ", nameAr)
##      nameAr = re.sub(r"aʾu", r"ؤ", nameAr)
##
##      nameAr = re.sub(r"iʾ[aiu]", r"ئ", nameAr)
##      
##      nameAr = re.sub(r"uʾ[au]", r"ؤ", nameAr)
##      nameAr = re.sub(r"uʾi", r"ئ", nameAr)
##      
##      nameAr = re.sub(r"[aA]ʾī", r"ئي", nameAr)
##      nameAr = re.sub(r"[āĀ]ʾī", r"ائي", nameAr)
##      nameAr = re.sub(r"[uU]ʾā", r"ؤا", nameAr)
##      
##      nameAr = re.sub(r"[uU]ʾ(%s)" % arCtrans, r"ؤ\1", nameAr)
##      nameAr = re.sub(r"[iI]ʾ(%s)" % arCtrans, r"ئ\1", nameAr)
##      nameAr = re.sub(r"[aA]ʾ(%s)" % arCtrans, r"أ\1", nameAr)
##
##      # madda: hamza followed by long a
##      nameAr = re.sub(r"ʾ[āĀ]", r"آ", nameAr)
##      
##      # final: hamza      
##      nameAr = re.sub(r"[uU]ʾ\b", r"ؤ", nameAr)
##      nameAr = re.sub(r"[iI]ʾ\b", r"ئ", nameAr)
##      nameAr = re.sub(r"[aA]ʾ\b", r"أ", nameAr)
##      
##      nameAr = re.sub(r"(%s)ʾ\b" % arVlong, r"\1ء", nameAr)
##
##      #arVowel  = "[áāĀaAiIīĪuUūŪ]"
##      #arVlong  = "[áāĀīĪūŪ]"
##      #arVshort = "[aAiIuU]"
##      #arCtrans = "[ʾʿbBčČdDḍḌḏḎġĠḥhHḤḫḪqQrRsSšŠṣṢtTṭṬṯṮŧwWzZẓẒ]"
##      #arHamza  = "ʾ"
##      #arAyn    = "ʿ"

    text = dictReplace(text, betaCodeTables.translitArabic)
    text = re.sub("-|_", "", text) # converts articles
    return(text)

testString = """
.kul huwa all~ahu_ a.hadu.n all~ahu_ al-.samadu_ lam yalid wa-lam y_ulad wa-lam yakun lahu kufu'a.n a.hadu.n

wa-.k_amat `_amma:t+u_ Ba.gd_ada_ li-yusallima al-_hal_ifa:ta_ al-Man.s_ura_ `al/a ruj_u`i-hi min al-K_ufa:ti_

al-.hamdu li-Ll~ahi


"""

print("betacode")
print(testString)

print(betacodeToTranslit(testString))
print(betacodeToSearch(testString))
print(betacodeToLOC(testString))
print(betacodeToArabic(testString))



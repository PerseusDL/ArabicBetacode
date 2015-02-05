import os, re
import betaCode, betaCodeTables

div = "############################################################\n"
sourceFolder = "./_HadithReader_Raw/"
targetFolder = "./_HadithReader_Processed/"

def processAllFiles():
    listOfFiles = os.listdir(sourceFolder)
    for file in listOfFiles:
        #print(file)
        #input(targetFolder+file[:-4]+"_Working.txt")
        if os.path.isfile(targetFolder+file[:-4]+"_Working.txt"):
            # regenerateFile
            print("\tRegenerating: %s" % file[:-4]+"_Working.txt")
            regenerateFile(file)
        else:
            # generateFile
            print("Generating: %s" % file[:-4]+"_Working.txt")
            generateFile(file)

def generateFile(file):
    with open(sourceFolder+file, "r", encoding="utf8") as f:
        hadith = f.read()
        hadithID = re.search(r"hadithID::(.*)\n", hadith).group(1).strip()
        hadithText = re.search(r"arHadithInit::(.*)\n", hadith).group(1).strip()
        
        # reformat optatives and other recognizeable elements
        
        # form the text
        hadithHeader = div + "## hadithID::     %s\n## Completed by:: ADDYOURNAME\n## Finished::     NO/YES\n\n" % hadithID
        arabicOriginal = div + "## ArabicInitial\n%s\n\n" % hadithText
        betaCodeAutoVar = betaCode.arabicToBetaCode(hadithText)
        betaCodeAuto = div + "## betaCodeAuto\n%s\n\n" % betaCodeAutoVar
        betaCodeManual = div + "## betaCodeManual\n%s\n\n" % betaCodeAutoVar
        betaCodeTranslit = div + "## betaCodeManual>Translit\n%s\n\n" % betaCode.betacodeToTranslit(betaCodeAutoVar)
        betaCodeArabic = div + "## betaCodeManual>Arabic\n%s\n\n" % betaCode.betacodeToArabic(betaCodeAutoVar)
        translationBetaCode = div + "## TranslationBetaCode\nType your translation on this line\n\n"
        translationTranslit = div + "## TranslationTranslit\nTranslation with transliterated names will appear here\n\n"

        newWorkingFile = hadithHeader + arabicOriginal + betaCodeAuto + betaCodeManual + betaCodeTranslit + betaCodeArabic + translationBetaCode + translationTranslit

        # save the text
        with open(targetFolder+file[:-4]+"_Working.txt", "w", encoding="utf8") as f:
            f.write(newWorkingFile)

            
def regenerateFile(file):
    with open(targetFolder+file[:-4]+"_Working.txt", "r", encoding="utf8") as f:
        hadith = f.read()

        hadith = re.split(div, hadith)

        # arabicOriginal
        arabicOriginal = re.sub("\n+", "\n", hadith[2])
        arabicOriginal = arabicOriginal.split("\n")[1]
        #input(arabicOriginal)
        #place to apply some additional conversions (salla allahu `alayhi wasallama > sl`m)

        # regenerate betaCodeAuto
        betaCodeAutoNew = betaCode.arabicToBetaCode(arabicOriginal)
        betaCodeAuto = re.sub("\n+", "\n", hadith[3])
        betaCodeAuto = betaCodeAuto.split("\n")
        betaCodeAuto[1] = betaCodeAutoNew
        hadith[3] = "\n".join(betaCodeAuto)

        # betaCodeManual
        betaCodeManual = re.sub("\n+", "\n", hadith[4])
        betaCodeManual = betaCodeManual.split("\n")[1]

        # regenerate betaCodeTranslit
        betaCodeTranslitNew = betaCode.betacodeToTranslit(betaCodeManual)
        betaCodeTranslit = re.sub("\n+", "\n", hadith[5])
        betaCodeTranslit = betaCodeTranslit.split("\n")
        betaCodeTranslit[1] = betaCodeTranslitNew
        hadith[5] = "\n".join(betaCodeTranslit)

        # regenerate betaCodeArabic
        betaCodeArabicNew = betaCode.betacodeToArabic(betaCodeManual)
        betaCodeArabic = re.sub("\n+", "\n", hadith[6])
        betaCodeArabic = betaCodeArabic.split("\n")
        betaCodeArabic[1] = betaCodeArabicNew
        hadith[6] = "\n".join(betaCodeArabic)

        # translationBetaCode
        translationBetaCode = re.sub("\n+", "\n", hadith[7])
        translationBetaCode = translationBetaCode.split("\n")[1]

        # regenerate translationTranslit
        translationTranslitNew = betaCode.betacodeToTranslit(translationBetaCode)
        translationTranslit = re.sub("\n+", "\n", hadith[8])
        translationTranslit = translationTranslit.split("\n")
        translationTranslit[1] = translationTranslitNew
        hadith[8] = "\n".join(translationTranslit)

        # collect the record back
        newWorking = ""
        for section in hadith[1:]:
            newWorking = newWorking + div + section + "\n\n"

        newWorking = re.sub("\n{3,}", "\n\n", newWorking)
        
        #input(newWorking)

        # save the text
        with open(targetFolder+file[:-4]+"_Working.txt", "w", encoding="utf8") as f:
            f.write(newWorking)
    

processAllFiles()

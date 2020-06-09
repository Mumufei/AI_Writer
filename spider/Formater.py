import os
import re

# Step 1: Get Corpus From Folders
#corpusPath = "../NewCorpus/new-FF14-Corpus-en.txt"      # ATTENTION: if zh needed, replace "en" as "zh"
corpusPath = "./少女前线"
dataPathes = []     # It Could be Removed Later
# dialogueText = open(corpusPath).read()
dialogueText = ""
for dirPath, dirNameList, fileNameList in os.walk(corpusPath):
     for name in fileNameList:
         fileName = "%s/%s" % (dirPath, name)
         file = open(fileName, encoding='UTF-8')
         tempText = file.read().replace("\n", " | ").replace(" |  |  | ", "\n").replace("\n | ", "\n").replace(" |  | ", " | ")
         # tempText.replace("\n\n", ';').replace('\n', "")
         dialogueText = "%s%s\n" % (dialogueText, tempText)
         dataPathes.append(fileName)
         file.close()

# Step 2.5: Find Every Kind of Placeholders, Analyzing~
# Type 1: "<>" Type, Delete All
# placeholderList = re.findall('<.*?>', dialogueText)
# TypeList = []
# for placeholder in placeholderList:
#     if placeholder not in TypeList:
#         print(placeholder)
#         TypeList.append(placeholder)
#         dialogueText.replace(placeholder, "")
# TypeList.clear()
# placeholderList.clear()
# Type 2: "()" Type
# placeholderList = re.findall(' &lt;.*?&gt;', dialogueText)
# for placeholder in placeholderList:
#     if placeholder not in TypeList:
#         TypeList.append(placeholder)
#         # dialogueText.replace(placeholder, '')
#         print(placeholder)
# Step 4: Join These Corpus into One *.txt
filehandle = open("Girlsfrontline.txt", "w", encoding='UTF-8')
filehandle.write(dialogueText)
filehandle.close()
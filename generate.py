from utils import askUser, clearTerminal, printHeading
from os import path, mkdir

CONST_DEFAULT_TYPST_FILE = """
#import "../../templates/sammanfattning1.typ": *

#show: sammanfattningStyles.with(lang: "sv") 


// ----------------- First Page -----------------
#show: makeSammanfattningCover.with(
  docTitle: [Matematik Specialisering],
  authors: ("Oscar Kristensson",),
  cover: image("figures/MaSpecBakgrund.svg"),
)
"""


def generatePage():
    clearTerminal()
    printHeading("Generate project")
    
    CONFIG_FILE_NAME = "typ_proj_config.json"


    if path.exists(CONFIG_FILE_NAME):
        print("Failed to generate project, the config file already exists")
        return
    

    documentPath = askUser(
"""What is the path to the document? 
For example: "sammanfattningAvMatematikSpecialisering". 
Do not include the file extension.
""")

    fontPath = askUser(
"""What is the path to the fonts? 
For example: "C:/Storage/Typst/fonts" (default).
To use the default, press enter 
""")
    
    if fontPath == "":
        fontPath = "C:/Storage/Typst/fonts"

    
    outputDocumentName = askUser(
"""What is the document name? 
For example: "Sammanfattning av Matematik Specialisering".
Do not include the file extension.
""")
    
    rootPath = askUser(
"""What is the path to the root? 
For example: "../../"
Default: ""
To use the default, press enter 
""")
    
    if rootPath == "":
        rootPath = ""



    string = "{" + f"""
        "documentPath": "{documentPath}",
        "fonts": "{fontPath}",
        "name": "{outputDocumentName}",
        "root": "{rootPath}"
    """ + "}"


    createFolderStructure = askUser("Create folder structure (Y/n)")

    if createFolderStructure == "Y":
        mkdir("figures")
        

    defaultFile = askUser("Create default file (Y/n)")
    

    if defaultFile == "Y":
        DEFAULT_FILE = documentPath + ".typ"
        if path.exists(DEFAULT_FILE):
            print("Could not create the default file")
        else:
            with open(DEFAULT_FILE, "w") as f:
                f.write(CONST_DEFAULT_TYPST_FILE)
        
        


    with open(CONFIG_FILE_NAME, "w") as f:
        f.write(string)


    input("Finished configuration. Press enter to continue")

    clearTerminal()
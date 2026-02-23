from utils import clearTerminal, printHeading, compileTypstDocToPDF, actionList, safeLoad
import json
import os
import shutil

global data

def loadProjectInfo():
    global data
    configPath = os.getcwd().replace("\\", "/") + "/typ_proj_config.json"
    print(configPath)
    if not os.path.exists(configPath): 
        print("Path does not exist")
        return False
    

    with open(configPath, "r") as f:
        data = json.load(f)

    return True


def compile():
    if (not loadProjectInfo()):
        print("Could not load the project")
        return
    
    clearTerminal()
    printHeading("Compile")
    print("Compiling document")


    if not "documentPath" in data:
        print("the parameter documentPath is required")
        return

    relativeDocumentPath = data["documentPath"]
    fontPath = data["fonts"]
    ignoreSystemFonts = fontPath != ""

    if not ignoreSystemFonts:
        fontPath = None

    root = safeLoad(data, "root", "")
    outputName = safeLoad(data, "name", relativeDocumentPath)

    docPath = os.getcwd() + "/" + relativeDocumentPath




    compileTypstDocToPDF(docPath + ".typ", ignoreSystemFonts, fontPath, root)

    
    shutil.move(docPath+".pdf", os.getcwd() + "/" + outputName + ".pdf")


    



    



def mainPage():
    loadProjectInfo()
    clearTerminal()
    printHeading("TypMan")

    actionList([
        {
            "name": "Compile",
            "func": compile
        },
    ])




    # clearTerminal()
    
    


if __name__ == "__main__":
    mainPage()
import subprocess
import os


def printHeading(heading):
    # Calculate the number of dashes needed on each side
    total_length = 50  # total width of the line
    dash_length = (total_length - len(heading) - 2) // 2  # subtract 2 for spaces
    line = '-' * dash_length + f' {heading} ' + '-' * dash_length
    
    # If the title length makes the line short by 1 character (odd), add 1 more dash at the end
    if len(line) < total_length:
        line += '-'
    
    print(line)

def compileTypstDocToPDF(documentLocation,  ignoreSysFonts = True, fontPath = "fonts", root = "docs"):
    print("WorkingDir:", os.getcwd())
    print("Input:", documentLocation)



    command = ["typst", "compile", str(documentLocation)] # , "--features", "html"

    if ignoreSysFonts:
        command.append("--ignore-system-fonts")



    # Note: Add error handling for FileNotFound errors
    if fontPath is not None:
        command.append("--font-path")
        command.append(str(fontPath))


    if root is not None:
        command.append("--root")
        command.append(str(root))



    print("Running command: ", " ".join(command))
    subprocess.run(command)


def actionList(actions = []):
    for i, action in enumerate(actions):
        print(f"{i + 1}: {action["name"]}")


    while True:
        rv = input("\n\nSelect the action, pressing enter exits: ")

        if rv == "":
            return None
        
        try:
            actionIndex = int(rv) - 1


        
        except:
            print("Failed to convert action to index, try again")
            continue

        return actions[actionIndex]["func"]()

    
    

        


def clearTerminal():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux / macOS
    else:
        os.system('clear')


def safeLoad(dict: dict, key: str, catchValue):
    if not key in dict:
        return catchValue
    
    return dict[key]


import glob, os
from posixpath import dirname

def loweredgames(f):
    loweredgamesquestion = input("Do you want to lower the games row on the main screen? [y/N]: ")
    if loweredgamesquestion == "y":
        with open("loweredgames.css", "r") as r:
            f.write(r.read())

def themepicker():
    themechoice = input("Which styling do you want? ")
    if os.path.exists(themechoice):
        return themechoice
    else:
        print("Invalid choice")
        themepicker()

def foldercreator(dirName):
    try:
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        foldercreator(dirName)

def borderradius(f):
    borderradiusquestion = input("Do you want to turn border radius OFF? [y/N]: ")
    if borderradiusquestion == "y":
        f.write('border-radius: 0px !important;\n')

def boxshadow(f):
    bordershadowquestion = input("Do you want to turn box shadow OFF? [y/N]: ")
    if bordershadowquestion == "y":
        f.write('box-shadow: none !important;\n')
        f.write('-webkit-box-shadow: none !important;\n')

def texticoncolour(f):
    textcolour = input("Colour for Text and Icons (WIP). Enter 'default' for default colours: ")
    if textcolour != "default":
            f.write('color: #' + textcolour + ' !important;\n')


print("Warning! Eat every option, the upper case Y or N is the default option!")
themename = input("Enter your theme name: ")
themefile = themename + ".css"
print("\n")
os.chdir("./templates")
for file in glob.glob("*.css"):
    print(file)
themestyle = "templates/" + themepicker()
os.chdir('..')
print("\n")
print("Colour inputs are all hex-codes WITHOUT A HASTAG. For making good colour combinations, go to https://coolors.co/")
backgroundlight = input("Colour for Light Background: ")
backgroundregular = input("Colour for Regular Background: ")
backgrounddark = input("Colour for Dark Background: ")
borderlight = input("Colour for Light Border: ")
borderdark = input("Colour for Dark Border: ")
accent = input("Colour for accents: ")
print("For the list of fonts included as standard on the Steam Deck, go to the DeckFonts.txt on the Github page")
fontfamily = input("Enter the exact name of the font you want here: ")

foldercreator(themename)

with open(themename + "/theme.json", 'w') as t:
    t.write("\n")
    t.write("{\n")
    t.write('"name": "' + themename + '",\n')
    t.write('"version": "1.0",\n')
    t.write('"inject": {\n')
    t.write('"' + themefile + '": [\n')
    t.write('"SP", "MainMenu", "QuickAccess"\n')
    t.write(']\n')
    t.write('}\n')
    t.write('}\n')
    

with open(themename + "/" + themefile, 'w') as f:
    f.write(':root {\n')
    f.write('--BackgroundLight: #' + backgroundlight + ' !important;\n')
    f.write('--BackgroundRegular: #' + backgroundregular + ' !important;\n')
    f.write('--BackgroundDark: #' + backgrounddark + ' !important;\n')
    f.write('--BorderLight: #' + borderlight + ' !important;\n')
    f.write('--BorderDark: #' + borderdark + ' !important;\n')
    f.write('--Accent: #' + accent + ' !important;\n')
    f.write('}\n')
    f.write('* {\n')
    f.write('font-family: "' + fontfamily + '" !important;\n')
    texticoncolour(f)
    borderradius(f)
    boxshadow(f)
    f.write('}\n')
    with open(themestyle, "r") as r:
        f.write(r.read())
    loweredgames(f)
exit()

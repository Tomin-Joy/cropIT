from PIL import Image
import re
import glob



class SizeError(Exception):
    pass
def sizeValidate(input):
    pattern = re.compile(r"[0-9]+x[0-9]+")
    return pattern.match(input)

def help():
    print("""commands present:
    -h or --help : displays this menu
    -r <input> <size> <output_name>: resize image to custom size
        eg:
            -r img.png 400x600 result_name.png

    -c <input> <output format> : change format of the image 
        eg: 
            -c img.png jpg
    -ca <input format> <output format> : change all images in one format to other
        eg:
            -ca png jpg
    -q or --quit : exit
    """ )

def resizer(cmd):
    arg=cmd.split(">>>")
    try:
        if len(arg)<4:
            raise IndexError
        image = Image.open(arg[1])
        if not sizeValidate(arg[2]):
            raise SizeError
        size=arg[2].split("x")
        image = image.resize((int(size[0]),int(size[1])))
        image.save(arg[3])
        print("done")
    except FileNotFoundError:
        print("Invalid path or file")
    except IndexError:
        print("Argument missing")
    except SizeError:
        print("Invalid size")
def formatAll(cmd):
    arg=cmd.split(" ")
    try:
        if len(arg)<3:
            raise IndexError
        for img in glob.glob(f"*.{arg[1]}"):
            try:
                image = Image.open(img)
                image = image.convert("RGB")
                image.save(img.replace(arg[1],arg[2]))
                print("done")
            except FileNotFoundError:
                print("Invalid path or file")
            except IndexError:
                print("Argument missing")
            except ValueError:
                print("Invalid Extension")
    except IndexError:
        print("Argument missing")
    

def formater(cmd):
    arg=cmd.split(" ")
    try:
        if len(arg)<3:
            raise IndexError
        name = arg[1].split(".")
        image = Image.open(arg[1])
        image = image.convert("RGB")
        image.save(f"{name[0]}.{arg[2]}")
        print("done")
    except FileNotFoundError:
        print("Invalid path or file")
    except IndexError:
        print("Argument missing")
    except ValueError:
        print("Invalid Extension")

print("Welcome \nType -h or --help\n ")
while(1):
    cmd = input("  ")
    arg=cmd.split(" ")
    if arg[0]=="-h" or arg[0] == "--help":
        help()
    elif arg[0]=="-q" or arg[0] =="--quit":
        print("see you again")
        break
    elif arg[0]=="-r":
        resizer(cmd)
    elif arg[0]=="-ca":
        formatAll(cmd)
    elif arg[0]=="-c":
        formater(cmd)
    else:
        print("invalid command")

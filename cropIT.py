from PIL import Image
import re



class SizeError(Exception):
    pass
def sizeValidate(input):
    pattern = re.compile(r"[0-9]+\\*[0-9]+")
    return pattern.match(input)

def help():
    print("""commands present:
    -h or --help : displays this menu
    -r <input> <size> <output_name>: resize image to custom size
        eg:
            -r img.png 400*600 result_name.png

    -c <input> <output format> : change format of the image 
        eg: 
            -c img.png jpg
    -q or --quit : exit
    """ )

def resize(cmd):
    arg=cmd.split(" ")
    try:
        if len(arg)<4:
            raise IndexError
        image = Image.open(arg[1])
        if not sizeValidate(arg[2]):
            raise SizeError
        size=arg[2].split("*")
        image = image.resize((int(size[0]),int(size[1])))
        image.save(arg[3])
        print("done")
    except FileNotFoundError:
        print("Invalid path or file")
    except IndexError:
        print("Argument missing")
    except SizeError:
        print("Invalid size")
    
def format(cmd):
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
    
    if cmd=="-h" or cmd == "--help":
        help()
    elif cmd=="-q" or cmd =="--quit":
        print("see you again")
        break
    elif cmd[0:2]=="-r":
        resize(cmd)
    elif cmd[0:2]=="-c":
        format(cmd)
    else:
        print("invalid command")
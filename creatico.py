import base64
with open("baohui.py","a") as f:
    f.write('class Gif(object):\n')
    f.write('\tdef __init__(self):\n')
    f.write("\t\tself.img='")
with open("baohui.ico","rb") as i:
    b64str = base64.b64encode(i.read())
    with open("baohui.py","ab+") as f:
        f.write(b64str)
with open("baohui.py","a") as f:
    f.write("'")

import os
import sys
import cv2
import qrcode
import numpy as np
import matplotlib.pyplot as plt

READ_PATH = "Files"
SAVE_PATH = "Codes"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def run():

    args_1: tuple = ("--data", "-d")
    args_2: tuple = ("--version", "-v")
    args_3: tuple = ("--box-size", "-bxs")
    args_4: tuple = ("--border", '-b')
    args_5: tuple = ("--background", "-bg")
    args_6: tuple = ("--foreground", "-fg")
    args_7: tuple = ("--save", "-s")

    data: str = None
    version: int = 1
    box_size: int = 10
    border: int = 4
    background: tuple = [255, 255, 255]
    foreground: tuple = [0, 0, 0]
    save: bool = False
    save_name: str = None

    if args_1[0] in sys.argv: data = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: data = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: version = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: version = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv: box_size = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: box_size = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if args_4[0] in sys.argv: border= int(sys.argv[sys.argv.index(args_4[0]) + 1])
    if args_4[1] in sys.argv: border = int(sys.argv[sys.argv.index(args_4[1]) + 1])

    if args_5[0] in sys.argv:
        color = (sys.argv[sys.argv.index(args_5[0]) + 1] + ",").split(",")
        for i in range(3): 
            if len(color) == 4: background[i] = int(color[2-i])
            else: background[i] = int(color[0])
    if args_5[1] in sys.argv:
        color = (sys.argv[sys.argv.index(args_5[1]) + 1] + ",").split(",")
        for i in range(3): 
            if len(color) == 4: background[i] = int(color[2-i])
            else: background[i] = int(color[0])
    
    if args_6[0] in sys.argv:
        color = (sys.argv[sys.argv.index(args_6[1]) + 1] + ",").split(",")
        for i in range(3): 
            if len(color) == 4: foreground[i] = int(color[2-i])
            else: foreground[i] = int(color[0])
    if args_6[1] in sys.argv:
        color = (sys.argv[sys.argv.index(args_6[1]) + 1] + ",").split(",")
        for i in range(3): 
            if len(color) == 4: foreground[i] = int(color[2-i])
            else: foreground[i] = int(color[0])
    
    if args_7[0] in sys.argv:
        save = True
        save_name = sys.argv[sys.argv.index(args_7[0]) + 1] 
    if args_7[1] in sys.argv: 
        save = True
        save_name = sys.argv[sys.argv.index(args_7[1]) + 1]

    assert data is not None, "Enter data using --data | -d"
    assert version >= 1 and version <= 40, "Supported Versions are 1 to 40"

    if data[-3:] == "txt":
        fp = open(os.path.join(READ_PATH, data), "r")
        data = fp.read()
        fp.close()
        assert len(data) < 2000, "Data is too long to encode"
        
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(data, optimize=0)
    qr.make(fit=True)
    image = qr.make_image(fill_color=tuple(foreground), back_color=tuple(background))

    if not save:
        plt.figure()
        plt.imshow(image)
        plt.show()
    else:
        assert save_name is not None, "Enter a name for the save file"
        cv2.imwrite(os.path.join(SAVE_PATH, save_name + ".jpg"), np.array(image))

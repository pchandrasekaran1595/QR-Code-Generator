import os
import sys
import cv2
import qrcode
import numpy as np
import matplotlib.pyplot as plt

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH  = os.path.join(BASE_PATH, "input")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

if not os.path.exists(OUTPUT_PATH): os.makedirs(OUTPUT_PATH)


def breaker(num: int = 50, char: str = "*") -> None:
    print("\n" + num*char + "\n")


def show_image(image, cmap: str = "gnuplot2", title: str=None) -> None:
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    if title: plt.title(title)
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def main():
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
    background: list = [255, 255, 255]
    foreground: list = [0, 0, 0]
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
        with open(os.path.join(INPUT_PATH, data), "r") as fp:
            data = fp.read()
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
        cv2.imwrite(os.path.join(OUTPUT_PATH, save_name + ".jpg"), np.array(image))


if __name__ == "__main__":
    sys.exit(main() or 0)
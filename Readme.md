## QR Code Generator

1. Install Python
2. Run `pip install virtualenv`
3. Run `make-env.bat` or `make-env-3.9.bat`
4. Input Path &nbsp;--> `input`
5. Output Path --> `output`

<br>

[*qrcode* Library](https://pypi.org/project/qrcode/)

<br>

### **CLI Arguments**

<br>

<pre>
1. --data | -d        : A Link or a text file placed in Read Path
2. --version | -v     :
3. --box-size | -bxs  :
4. --border | -b      :
5. --background | -bg : Background Color (Default: (255, 255, 255)) [Expects 'number' or 'number,number,number']
6. --foreground | -fg : Foreground Color (Default: (0, 0, 0)) [Expects 'number' or 'number,number,number']
7. --save | -s        : Saves the Code (Expects 'filename')
</pre>
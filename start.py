import glob
from zipfile import ZipFile

files = glob.glob('./*.zip')

for n1 in range(0, 10):
    for n2 in range(0, 10):
        for n3 in range(0, 10):
            for n4 in range(0, 10):
                guess = ''.join(map(str, [n1, n2, n3, n4]))
                for n in range(len(files)):
                    zip_file = files[n]
                    if zip_file is not None:
                        password = None
                        with ZipFile(zip_file) as zf:
                            try:
                                zf.setpassword(bytes(guess, 'utf-8'))
                                if zf.testzip() is None:
                                    print("File: %s  Password: %s" % (zip_file, guess))
                                    password = guess
                                    files[n] = None
                            except:
                                pass

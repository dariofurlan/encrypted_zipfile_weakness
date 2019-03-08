import glob
from zipfile import ZipFile

files = glob.glob('./*.zip')

for n1 in range(0, 10):
    for n2 in range(0, 10):
        for n3 in range(0, 10):
            for n4 in range(0, 10):
                guess = ''.join(map(str, [n1, n2, n3, n4]))
                for zip_file in files:
                    password = None
                    with ZipFile(zip_file) as zf:
                        try:
                            zf.extractall(pwd=bytes(guess, 'utf-8'))
                        except:
                            pass
                            # print("Tried Unsuccessfully: %s" % guess)
                        else:
                            print("File: %s  Password: %s" % (zip_file, guess))
                            password = guess
                            break
                    if password is not None:
                        ZipFile(zip_file).extractall(pwd=bytes(password, 'utf-8'))

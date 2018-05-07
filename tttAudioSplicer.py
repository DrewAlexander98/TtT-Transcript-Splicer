def main():
    

def open_file(filename):
    if os.path.isfile(filename):
        inFile = open(filename, 'r')
        return inFile
    else:
        print("Cannot locate file {0}".format(filename))
        return None

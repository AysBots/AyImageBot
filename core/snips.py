import os


def all_permit(filename):
    os.system(f"chmod 777 ./{filename}")

def searchdata(text, filename):
    with open(filename, 'a') as f:
        f.write(str(text)+"\n")
        f.close()

try:
    open("C:\\non_esiste.txt")
except OSError as e:
    raise e
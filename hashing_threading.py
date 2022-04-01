from hashlib import sha1
import random
import string
import threading

def lowercase_word():
    word = ''
    random_word_length = random.randint(1, 5)
    while len(word) != random_word_length:
        word += random.choice(string.ascii_lowercase)
    return word

def hash_word_to_file():
    file1 = open("rainbowtabble.txt", "a")
    while True:
        c = lowercase_word()
        file1.write("%s\t\t>\t%s\n" %(c, sha1(c.encode('ASCII')).hexdigest()))

thread1 = threading.Thread(target=hash_word_to_file)
thread1.start()
thread2 = threading.Thread(target=hash_word_to_file)
thread2.start()
thread3 = threading.Thread(target=hash_word_to_file)
thread3.start()
thread4 = threading.Thread(target=hash_word_to_file)
thread4.start()

# binary files:
    # store data in bytes, can be text, images, pdf, video, audio
    # no delimiter
    # no translation required

# text files"
    # ascii or unicode
    # line ends with EOL character
    # default file mode


f = open("day.txt")
print("read :", f.read())
f.seek(0)
print("readlines :", f.readlines())
f.seek(0)
print("readline :", f.readline())


# seek() takes 2 arguments:
    # off-set:
        # defines how many positions to move
        # negative off-set is only alloweed in binary mode
    # reference:
        # it can be 0 (for beginning of file), default
        # 1 for current position
        # 2 for end of file


# f.tell()          # to get the position at which the reader index is at currently








# using context manager

with open('day.txt', 'r') as f1: # automatically closes the file when block ends or error is thrown
    optional_number_of_characters_to_read = 10
    print(f.read(optional_number_of_characters_to_read))
    # or 
    for line  in f:
        print(line)
    



print(f1.closed())   # returns True; though f1 is still accessible, the reading, writting operation is not alowed on it.



# to read images and other formats, we must open files in binary mode i.e, rb, wb, etc.

# access modes:
    # r reading only (default)
    # rb 
    # r+ reading and writing, pointer at the beginning
    # rb+ 
    # w writing only. Overwrite or create
    # wb
    # w+ reading and writing, pointer at the end
    # wb+
    # a appending or create
    # ab
    # a+ append and read
    # ab+
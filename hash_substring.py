# python3
B = 13
Q = 256


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text1 = input()
    if("I" in text1):
        pattern = input()
        text = input()
        return (pattern.rstrip(), text.rstrip())
    
    if("F" in text1):
        name = "tests/06"
        with open(name) as file:
            pattern = file.readline()
            text = file.readline()
            return (pattern.rstrip(), text.rstrip())
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q

    len_of_pattern = len(pattern)
    len_of_text = len(text)
    result = ""
    multiplier = 1
    hash_for_pattern = 0
    hash_fot_text = 0
    for i in range(1, len_of_pattern):
        multiplier = (multiplier * B)%Q

    for i in range(len_of_pattern):
        hash_for_pattern = (B * hash_for_pattern + ord(pattern[i]))%Q

    for i in range(len_of_text):
        hash_fot_text = (B * hash_fot_text + ord(text[i]))%Q

    for i in range(1+len_of_text-len_of_pattern):
        if hash_for_pattern==hash_fot_text:
            for j in range(len_of_pattern):
                if (text[i+j]!=pattern[j]):
                    break;
            j=j+1
            if j==len_of_pattern:
                result = result+str(i)+" "


        if(i<len_of_text-len_of_pattern):
            hash_fot_text = (B*(hash_fot_text-ord(text[i])*multiplier) + ord(text[i+len_of_pattern]))%Q
            if hash_fot_text<0:
                hash_fot_text = hash_fot_text + Q
    # and return an iterable variable
    return result.rstrip();


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


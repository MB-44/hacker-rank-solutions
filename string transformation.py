
import math
import os
import random
import re
import sys

def transformSentence(sentence):
    output = []
    sentence = sentence.split()

    for word in sentence:
        if len(word) == 1:
            output.append(word)
            continue
        else: 
            temp = word[0]
            for i in range(1,len(word)):
                if ord(word[i].lower()) == ord(word[i-1].lower()):
                    temp += word[i]
                elif ord(word[i].lower()) > ord(word[i-1].lower()):
                    temp += word[i].upper()
                else: 
                    temp += word[i].lower()
            output.append(temp)
    
    return " ".join([word for word in output])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
    print(result)

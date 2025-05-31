def caesarCipherEncryptor(string,key):
    newLetters=[]
    newKey=key%26
    alphabet =list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabet))
    return "".join(newLetters)

def getNewLetter(letter,key,alphabet):
    newLetterCode=alphabet.index(letter)+key
    return alphabet[newLetterCode] if newLetterCode <=25 else alphabet[newLetterCode-26]



print(caesarCipherEncryptor("abc", 2))      # Expected: "cde"
print(caesarCipherEncryptor("xyz", 3))      # Expected: "abc"
print(caesarCipherEncryptor("hello", 5))    # Expected: "mjqqt"
print(caesarCipherEncryptor("abc", 52))     # Expected: "abc"
print(caesarCipherEncryptor("abc", 27))     # Expected: "bcd"
print(caesarCipherEncryptor("z", 1))        # Expected: "a"
print(caesarCipherEncryptor("z", 25))       # Expected: "y"
print(caesarCipherEncryptor("a", 26))       # Expected: "a"

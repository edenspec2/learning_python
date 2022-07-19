import function_based as fb

def counting_vowels(word):
    try:
        type(word)==str
        vowels=['a','e','o','u','i']
        letter_count=0
        for letters in word.lower():
            if letters in vowels:
                letter_count=letter_count+1
        return letter_count
    except:
        return print ('invalid')

if __name__=='__main__':
    num=counting_vowels('hiAii')
    print(num)
    var=fb.text_to_matrix('1.txt')
    print(var)


import string

def get_value(name):
    '''
    return the value of given name
    '''
    letter_value = {}
    namevalue = 0
    value = 0
    for i in range(26):
        letter_value[chr(i+97)] = i+1
    
    for letter in name:
        if letter in letter_value.keys():
            value = letter_value[letter]
        namevalue += value
    return namevalue

# print(get_value('angela'))

def load_namelist(file_name):
    '''
    load the txt file, get all the names to name_list
    '''
    fp = open(file_name, 'r') 
    fullname_list = []
    name_list = []
    for line in fp:
        line = line.lower()
        line = line.strip("\n")
        line = line.split()
        fullname_list.append(line)
    
    for name in fullname_list:
        name.pop()
        name_list.append("".join(name))

    return name_list


def who_has_highest_value(file_name):
    name_list = load_namelist(file_name)
    Max = 0
    for name in name_list:
        value = get_value(name)
        if value > Max:
            Max = value
    return name + str(Max)


def get_words_with_same_value(file_name):
    '''
    return a list of matched words
    '''
    fd = open(file_name, 'r')
    for word in fd:
        if get_value(word) == get_value("Shirley"):
            return word
        else:
            return None


def main():
    file_name = 'roster.txt'
    print("The most valuable name of our class is: " + who_has_highest_value(file_name))
    print("The positive words that have the same value as my first name are: "+ str(get_words_with_same_value('positive-words.txt')))



if __name__ == '__main__':
    main()

with open('log.txt','r') as f:
    data=f.read()
    space_character=data.find(' ')
    new_line=data.find('\n')
    print(space_character)
    print(new_line)
    data_name=data[0:space_character]
    print(data_name)
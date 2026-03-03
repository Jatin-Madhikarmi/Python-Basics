with open('log.txt','r') as f:
    start=0
    msg=dict()
    data=f.read()
    space_character=data.find(' ')
    new_line=data.find('\n')
    assert new_line == start
    msg[None]=data[new_line+1:]
    print(space_character)
    print(new_line)
    data_name=data[0:space_character]
    print(msg)
    print(data_name)
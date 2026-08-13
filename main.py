def read_code_file(target_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        text = f.read()
    text2 = text.split('\n')
    ret = []
    for i in text2:
        if i == '':
            continue
        temp = []
        for j in i:
            temp.append(j)
        ret.append(temp)
    return ret

# test
if __name__ == '__main__':
    print(read_code_file('test_code.txt'))

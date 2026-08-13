def read_code_file(target_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        text = f.read()
    return [list(i) for i in text.split('\n') if i]

# test
if __name__ == '__main__':
    print(read_code_file('test_code.txt'))

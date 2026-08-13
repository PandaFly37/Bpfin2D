def read_code_file(target_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        text = f.read()
    rows = [list(i) for i in text.splitlines() if i]
    if not rows:
        return []
    max_len = max(len(row) for row in rows)
    return [row + [' '] * (max_len - len(row)) for row in rows]

# test
if __name__ == '__main__':
    print(read_code_file('test_code.txt'))

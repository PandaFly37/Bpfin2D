def read_code_file(target_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        text = f.read()
    rows = [list(i) for i in text.splitlines() if i]
    if not rows:
        return []
    max_len = max(len(row) for row in rows)
    return [row + [' '] * (max_len - len(row)) for row in rows]

def run_code(code):
    fx2ip = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    ipx = ipy = m0 = m1 = m2 = mc = 0
    data = []
    while True:
        # check
        if ipx < 0 or ipy < 0 or ipx >= len(code) or ipy >= len(code[0]):
            break
        m_max = max(m0, m1, m2)
        while m_max >= len(data):
            data.append(0)
        # set op
        op = code[ipx][ipy]
        # do
        if op == '<': fx = 'L'
        elif op == '>': fx = 'R'
        elif op == '^': fx = 'U'
        elif op == 'v': fx = 'D'
        elif op == '[':
            if fx == 'U': fx = 'L'
            elif fx == 'D': fx = 'R'
            elif fx == 'L': fx = 'D'
            elif fx == 'R': fx = 'U'
        elif op == ']':
            if fx == 'U': fx = 'R'
            elif fx == 'D': fx = 'L'
            elif fx == 'L': fx = 'U'
            elif fx == 'R': fx = 'D'
        elif op == '-':
            if fx == 'U': fx = 'D'
            elif fx == 'D': fx = 'U'
        elif op == '|':
            if fx == 'L': fx = 'R'
            elif fx == 'R': fx = 'L'
        elif op == '+':
            pass
        elif op == '/':
            if data[m1] == data[m2]:
                if fx == 'U': fx = 'R'
                elif fx == 'D': fx = 'L'
                elif fx == 'L': fx = 'U'
                elif fx == 'R': fx = 'D'
        elif op == '\\':
            if data[m1] == data[m2]:
                if fx == 'U': fx = 'L'
                elif fx == 'D': fx = 'R'
                elif fx == 'L': fx = 'D'
                elif fx == 'R': fx = 'U'
        elif op == '0': mc = 0
        elif op == '1': mc = 1
        elif op == '2': mc = 2
        elif op == 'L':
            if mc == 0: m0 = max(m0 - 1, 0)
            elif mc == 1: m1 = max(m1 - 1, 0)
            elif mc == 2: m2 = max(m2 - 1, 0)
        elif op == 'R':
            if mc == 0: m0 += 1
            if mc == 1: m1 += 1
            if mc == 2: m2 += 1
        elif op == 'A': data[m0] = data[m1] + data[m2]
        elif op == 'S': data[m0] = data[m1] - data[m2]
        elif op == 'M': data[m0] = data[m1] * data[m2]
        elif op == 'C': data[m0] = data[m1]
        elif op == '~': data[m0] = ~data[m1]
        elif op == '^': data[m0] = data[m1] ^ data[m2]
        elif op == '&': data[m0] = data[m1] & data[m2]
        elif op == 'I': pass
        elif op == 'O':
            print(chr(data[m2]), end='')
        elif op == '.': break
        else: pass
        print(ipx,ipy,fx,op) # 测试
        # move
        ipx += fx2ip[fx][0]
        ipy += fx2ip[fx][1]
    return

# test
if __name__ == '__main__':
    code = read_code_file('test_code.txt')
    run_code(code)

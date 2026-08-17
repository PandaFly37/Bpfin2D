import sys


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
    ipx = ipy = mc = 0
    m = [0, 0, 0]
    fx = 'U'
    data = []
    while True:
        # check
        if ipx < 0 or ipy < 0 or ipx >= len(code) or ipy >= len(code[0]):
            break
        m_max = max(m)
        while m_max >= len(data):
            data.append(0)
        # set op
        op = code[ipx][ipy]
        # test output
        print(f'ipx:{ipx} ipy:{ipy} fx:{fx} op:{op} mc:{mc} m0:{m[0]}({data[m[0]]}) m1:{m[1]}({data[m[1]]}) m2:{m[2]}({data[m[2]]})')
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
            if data[m[1]] == data[m[2]]:
                if fx == 'U': fx = 'R'
                elif fx == 'D': fx = 'L'
                elif fx == 'L': fx = 'U'
                elif fx == 'R': fx = 'D'
        elif op == '\\':
            if data[m[1]] == data[m[2]]:
                if fx == 'U': fx = 'L'
                elif fx == 'D': fx = 'R'
                elif fx == 'L': fx = 'D'
                elif fx == 'R': fx = 'U'
        elif op == '0': mc = 0
        elif op == '1': mc = 1
        elif op == '2': mc = 2
        elif op == 'L':
            m[mc] = max(m[mc] - 1, 0)
        elif op == 'R':
            m[mc] += 1
        elif op == 'A': data[m[0]] = data[m[1]] + data[m[2]]
        elif op == 'S': data[m[0]] = data[m[1]] - data[m[2]]
        elif op == 'M': data[m[0]] = data[m[1]] * data[m[2]]
        elif op == 'C': data[m[0]] = data[m[1]]
        elif op == '~': data[m[0]] = ~data[m[1]]
        elif op == '^': data[m[0]] = data[m[1]] ^ data[m[2]]
        elif op == '&': data[m[0]] = data[m[1]] & data[m[2]]
        elif op == 'I': pass
        elif op == 'O':
            print(chr(data[m[2]]), end='')
        elif op == '.': break
        else: pass
        # move
        ipx += fx2ip[fx][0]
        ipy += fx2ip[fx][1]
    return

# test
if __name__ == '__main__':
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = 'test_code.txt'
    try:
        code = read_code_file(target_file)
    except FileNotFoundError:
        print(f"File not found: {target_file}")
        sys.exit(1)
    run_code(code)

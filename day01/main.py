def main():
    p = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read()
            d = [int(i) for i in data.split()]
            for j in d:
                for k in d:
                    if (j + k == 2020):
                        p = j * k
                        break
                    for l in d:
                        if (j + k + l == 2020):
                            p2 = j * k * l
                            break
    finally:
        fin.close()
        print(f'Part1 {p}')
        print(f'Part2 {p2}')


if __name__ == '__main__':
    main()

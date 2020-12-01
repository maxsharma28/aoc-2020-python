def main():
    p = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read()
            d = [int(i) for i in data.split()]
    finally:
        fin.close()
        print(f'Part1 {p}')
        print(f'Part2 {p2}')
if __name__ == '__main__':
    main()

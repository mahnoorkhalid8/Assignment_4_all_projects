def odd_num(res: int):
    remainder = res % 2
    return remainder == 1

def main():
    for i in range(20):
        if odd_num(i):
            print("ODD")

        else:
            print("EVEN")

if __name__ == "__main__":
    main()
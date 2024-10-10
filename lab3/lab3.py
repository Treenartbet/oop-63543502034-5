def pattern_1(rows):
    print("Pattern 1:")
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def pattern_2(rows):
    print("\nPattern 2:")
    for i in range(rows):
        for j in range(rows - i):
            print("*", end=" ")
        print()

def pattern_3(rows):
    print("\nPattern 3:")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)


def pattern_4(rows):
    print("\nPattern 4:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)

def pattern_5(rows):
    print("\nPattern 5:")
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("*" * (i + 1))

# รับค่าจำนวนแถว
rows = int(input("Enter number of rows: "))

# เรียกใช้ฟังก์ชันเพื่อพิมพ์รูปแบบต่างๆ
pattern_1(rows)
pattern_2(rows)
pattern_3(rows)
pattern_4(rows)
pattern_5(rows)

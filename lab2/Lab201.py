# รับค่าจำนวนแถว
rows = int(input("Enter number of rows: "))

# กำหนดจำนวนคอลัมน์เท่ากับจำนวนแถว
cols = rows

# Pattern 1: ดาวหรือช่องว่างตามเงื่อนไข
print("Pattern 1:")
for i in range(rows):
    for j in range(cols):
        if j <= i:  # พิมพ์เฉพาะเมื่อคอลัมน์ไม่เกินแถว
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # ขึ้นบรรทัดใหม่

# Pattern 2: ดาวตามจำนวนที่กำหนดด้านซ้าย
print("\nPattern 2:")
for i in range(rows):
    for j in range(cols - i):
        print("*", end=" ")
    print()  # ขึ้นบรรทัดใหม่

# Pattern 3: พิมพ์ดาวตามจำนวนที่กำหนดในแต่ละแถว
print("\nPattern 3:")
for i in range(rows, 0, -1):
    for _ in range(i - 1):
        print(" ", end="")
    for j in range(rows - i + 1):
        if j < rows - i:
            print("* ", end="")
        else:
            print("*", end="")
    print()

# Pattern 4: พิมพ์ดาวตามจำนวนที่กำหนดและวาดตามจำนวนแถว
print("\nPattern 4:")
for i in range(rows, 0, -1):
    for _ in range(rows - i):
        print(" ", end="")
    for j in range(i):
        if j < i - 1:
            print("* ", end="")
        else:
            print("*", end="")
    print()

# Pattern 5: พิมพ์ดาวตามจำนวนที่กำหนดและวาดตามจำนวนแถว
print("\nPattern 5:")
for i in range(rows):
    for j in range(rows):
        if j < rows - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()

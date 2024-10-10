def print_spaces(count):
    if count > 0:
        print(" ", end="")
        print_spaces(count - 1)

def print_stars(count):
    if count > 0:
        print("*", end=" ")
        print_stars(count - 1)

def print_pattern_1(rows, current_row=1):
    if current_row <= rows:
        print_spaces(rows - current_row)
        print_stars(current_row)
        print()
        print_pattern_1(rows, current_row + 1)

def print_pattern_2(rows, current_row=1):
    if current_row <= rows:
        print_stars(rows - current_row + 1)
        print()
        print_pattern_2(rows, current_row + 1)

def print_pattern_3(rows, current_row=1):
    if current_row <= rows:
        print_spaces(current_row - 1)
        print_stars(rows - current_row + 1)
        print()
        print_pattern_3(rows, current_row + 1)

def print_pattern_4(rows, current_row=1):
    if current_row <= rows:
        print_stars(current_row)
        print()
        print_pattern_4(rows, current_row + 1)

def print_pattern_5(rows, current_row=1):
    if current_row <= rows:
        print_spaces(rows - current_row)
        print_stars(current_row)
        print()
        print_pattern_5(rows, current_row + 1)

# รับค่าจำนวนแถว
rows = int(input("Enter number of rows: "))

print("\nPattern 1:")
print_pattern_1(rows)

print("\nPattern 2:")
print_pattern_2(rows)

print("\nPattern 3:")
print_pattern_3(rows)

print("\nPattern 4:")
print_pattern_4(rows)

print("\nPattern 5:")
print_pattern_5(rows)

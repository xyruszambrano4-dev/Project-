while True:
    n = int(input("Enter the TableSize (or type 0 to exit): "))
    if n == 0:
        break

    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)

    for row in table:
        print(row)

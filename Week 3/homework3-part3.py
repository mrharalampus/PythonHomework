data = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
]

for row in data:
    year = row[0]
    total = sum(row[1:])
    print(year, "Total sales:", total)

for row in data:
    year = row[0]
    avg = sum(row[1:]) / 4
    print(year, "Average sales:", avg)

max_sales = -1
min_sales = 999
max_year = max_q = 0
min_year = min_q = 0

for row in data:
    year = row[0]

    for i in range(1, 5):
        sales = row[i]

        if sales > max_sales:
            max_sales = sales
            max_year = year
            max_q = i

        if sales < min_sales:
            min_sales = sales
            min_year = year
            min_q = i

print("Max sales:", max_sales, "Year:", max_year, "Quarter:", max_q)
print("Min sales:", min_sales, "Year:", min_year, "Quarter:", min_q)
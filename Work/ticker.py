import csv

from follow import follow


def select_columns(rows, indicies):
    for row in rows:
        yield [row[index] for index in indicies]


def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows


if __name__ == "__main__":
    lines = follow("Data/stocklog.csv")
    rows = parse_stock_data(lines)
    rows = select_columns(rows, [0, 1, 4])
    for row in rows:
        print(row)

import xlsxwriter


def write(data, filename):
    workbook = xlsxwriter.Workbook(f'{filename}.xlsx')

    worksheet = workbook.add_worksheet("data")

    # Start from the first cell. Rows and
    # columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for id_, fname, lname, phone, city, age in data:
        worksheet.write(row, col, id_)
        worksheet.write(row, col + 1, fname)
        worksheet.write(row, col + 2, lname)
        worksheet.write(row, col + 3, phone)
        worksheet.write(row, col + 4, city)
        worksheet.write(row, col + 5, age)
        row += 1

    workbook.close()



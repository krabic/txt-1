import glob

from openpyxl import Workbook
import os

fldr = r"C:/Users/admin/Documents/парсинг/"
files = glob.glob(os.path.join(fldr, "geo_logins*.txt"))


def save(line_to_save):
    wb = Workbook()
    ws = wb.active
    for line in line_to_save:
        ws.append([line])
    wb.save("login_exel.xlsx")
    wb.close()


all_lines = []
for file in files:
    with open(file, 'r') as current_file:
        lines = current_file.readlines()  # take all lines of the file

        for line in lines:
            all_lines.append(line)
save(all_lines)

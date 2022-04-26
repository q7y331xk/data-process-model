from config import EXCEL_READ_TABLE
from rds.rds import read
from excel.excel import write_excel

sellings = read(EXCEL_READ_TABLE)
write_excel(sellings)
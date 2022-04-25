from config import PROCESSED_RDS_TABLE
from rds.rds import read
from excel.excel import write_excel

sellings = read(PROCESSED_RDS_TABLE)
write_excel(sellings)
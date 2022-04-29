from time import sleep
from config import EXCEL_KEYWORDS_PATH, EXISTS_RDS_TABLE, PROCESSED_RDS_TABLE, RDS_SKIP_ID
from process.process import process_data
from rds.rds import create_table_if_exists_drop, read, write
from excel.excel import read_model


print("==================================================")
print(f"read data from {EXISTS_RDS_TABLE}")
print(f"write data to {PROCESSED_RDS_TABLE}")
print(f"skip_id {RDS_SKIP_ID} ( 0 means there is no skip )")
print("sleep(0)")
print("==================================================")
# sleep(5)
print("1/5 read model from excel... ", end="")
models = read_model(EXCEL_KEYWORDS_PATH)
print("done")
print("2/5 read sellings... ", end="")
sellings_exist = read(EXISTS_RDS_TABLE)
print("done")
print("3/5 create new table... ", end="")
create_table_if_exists_drop(PROCESSED_RDS_TABLE)
print('done')
print('4/5 process data... ', end="")
sellings_processed = process_data(sellings_exist, models, RDS_SKIP_ID)
print('4/5 process data... done')
print('5/5 write processed data... ')
write(PROCESSED_RDS_TABLE, sellings_processed)
print('all complete!')
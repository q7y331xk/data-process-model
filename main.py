from config import EXISTS_RDS_TABLE, PROCESSED_RDS_TABLE
from process.process import process_data
from rds.rds import create_table_if_exists_drop, read
from excel.excel import read_model

models = read_model()
sellings_exist = read(EXISTS_RDS_TABLE)
create_table_if_exists_drop(PROCESSED_RDS_TABLE)
process_data(PROCESSED_RDS_TABLE, sellings_exist, models)
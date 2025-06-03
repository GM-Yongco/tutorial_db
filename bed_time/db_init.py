# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

import sqlite3
import textwrap
from datetime import datetime, timezone

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	print("-" * 50)
	print(section_name)
	print("-" * 50)

# ========================================================================
# FUNCTIONS 
# ========================================================================

DB_FILE:str = "sleep_log.db"
def execute_SQL(SQL_command:str) -> bool:
	is_executed_just_fine = False

	try:
		this_connection:sqlite3.Connection = sqlite3.connect(DB_FILE)
		this_cursor:sqlite3.Cursor = this_connection.cursor()
		this_cursor.execute(textwrap.dedent(SQL_command))
		this_connection.commit()
		this_connection.close()
		is_executed_just_fine = True
	except Exception as e:
		print(e)

	return is_executed_just_fine

def sql_value(val) -> str:
	if val == -1 or val == "NULL":
		return "NULL"
	else:
		return f'"{val}"'

# ========================================================================

def init_table_sleep_log()->None:
	CREATE_table_sleep_log = """
	CREATE TABLE IF NOT EXISTS sleep_log (
		time_stamp TEXT,
		
		hour_sleep_start INT,
		hour_sleep_end INT,

		id INTEGER PRIMARY KEY AUTOINCREMENT
	);
	"""
	execution_status = "NOT OK"
	if execute_SQL(SQL_command=CREATE_table_sleep_log):
		execution_status = "OK"
	print(f"{execution_status:8}init_table_sleep_log")

# ========================================================================

def CREATE_sleep_log(
	hour_sleep_start:int = -1, 
	hour_sleep_end:int = -1):

	time_now:str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

	INSERT_sleep_log = f"""
	INSERT INTO sleep_log (
		time_stamp, hour_sleep_start, hour_sleep_end
	) VALUES (
		{sql_value(time_now)},
		{sql_value(hour_sleep_start)},
		{sql_value(hour_sleep_end)}
	);
	"""
	execute_SQL(INSERT_sleep_log)

# ========================================================================

def READ_sleep_log():
	SQL_command = "SELECT * FROM sleep_log"

	this_connection:sqlite3.Connection = sqlite3.connect(DB_FILE)
	this_cursor:sqlite3.Cursor = this_connection.cursor()
	this_cursor.execute(textwrap.dedent(SQL_command))
	rows:list = this_cursor.fetchall()

	for row in rows:
		print(row)

	# Clean up
	this_connection.close()	

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	init_table_sleep_log()
	
	section("END")
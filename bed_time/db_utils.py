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
def SQL_execute(SQL_command:str) -> bool:
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

def SQL_fetch(SQL_command:str) -> bool:
	ret_val = 0

	try:
		this_connection:sqlite3.Connection = sqlite3.connect(DB_FILE)
		this_cursor:sqlite3.Cursor = this_connection.cursor()
		this_cursor.execute(textwrap.dedent(SQL_command))
		ret_val:list = this_cursor.fetchall()
		this_connection.close()
	except Exception as e:
		print(e)

	return ret_val

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
	# 24 hour format btw
	execution_status = "NOT OK"
	if SQL_execute(SQL_command=CREATE_table_sleep_log):
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
	SQL_execute(INSERT_sleep_log)

# ========================================================================

def READ_sleep_log():
	SQL_command = "SELECT * FROM sleep_log"
	rows:list = SQL_fetch(SQL_command)
	for row in rows:
		print(row)

def READ_last_2():
	SQL_command = """
	SELECT * FROM sleep_log
	ORDER BY id DESC
	LIMIT 2;
	"""
	rows:list = SQL_fetch(SQL_command)

	for row in rows:
		print(row)

	section()
	message:str = f"you slept at {rows[0][1]:02} the other day"
	message += f"\nyou slept at {rows[1][1]:02} yesterday"

	if (rows[0][1] > 0 and rows[0][1] <12) or (rows[1][1] > 0 and rows[1][1] <12) :
		message += "\nyou didnt sleep early in both days, no sleep late tonight"
		pass
	else:
		message += "\nyou slept early the past 2 days so you get to play league late :DDD"
	print(message)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	init_table_sleep_log()
	
	section("END")
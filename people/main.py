# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: 
# ========================================================================
# HEADERS
# ========================================================================

import sqlite3
import textwrap


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

def execute_SQL(SQL_command:str, DB_name = "people.db") -> bool:
	is_executed_just_fine = False

	try:
		this_connection:sqlite3.Connection = sqlite3.connect(DB_name)
		this_cursor:sqlite3.Cursor = this_connection.cursor()
		this_cursor.execute(textwrap.dedent(SQL_command))
		this_connection.commit()
		this_connection.close()
		is_executed_just_fine = True
	except Exception as e:
		print(e)

	return is_executed_just_fine

# ========================================================================

def init_table_people()->None:
	CREATE_table_people = """
	CREATE TABLE IF NOT EXISTS people (
		name_first TEXT,
		name_last TEXT,
		name_between TEXT,
		name_preferred TEXT,

		unique_description TEXT NOT NULL,
		people_id INTEGER PRIMARY KEY AUTOINCREMENT
	);
	"""
	execution_status = "NOT OK"
	if execute_SQL(SQL_command=CREATE_table_people):
		execution_status = "OK"
	print(f"{execution_status:8}init_table_people")

def init_table_birthdays()->None:
	CREATE_table_birthdays = """
	CREATE TABLE IF NOT EXISTS birthdays(
		year INTEGER,
		month INTEGER,
		date INTEGER,

		birthdays_id INTEGER PRIMARY KEY AUTOINCREMENT,
		people_id INTEGER,
		FOREIGN KEY (people_id) REFERENCES people(people_id)
	);
	"""
	execution_status = "NOT OK"
	if execute_SQL(SQL_command=CREATE_table_birthdays):
		execution_status = "OK"
	print(f"{execution_status:8}init_table_birthdays")
		

def init_tables():
	init_table_people()
	init_table_birthdays()

# ========================================================================

def CREATE_people(
	name_first:str = "NULL", 
	name_last:str = "NULL", 
	name_between:str = "NULL", 
	name_preferred:str = "NULL",
	unique_description:str = "NULL"):

	def sql_value(val):
		return "NULL" if val == "NULL" else f'"{val}"'

	INSERT_person = f"""
	INSERT INTO people (
		name_first, name_last, name_between, name_preferred, unique_description
	) VALUES (
		{sql_value(name_first)},
		{sql_value(name_last)},
		{sql_value(name_between)},
		{sql_value(name_preferred)},
		{sql_value(unique_description)}
	);
	"""
	execute_SQL(INSERT_person)

def UPDATE_people(
	people_id:int, 
	name_first:str = "NULL", 
	name_last:str = "NULL", 
	name_between:str = "NULL", 
	name_preferred:str = "NULL",
	unique_description:str = "NULL"):

	# checks if the person exists
	conn = sqlite3.connect('people.db')
	cursor = conn.cursor()
	cursor.execute("SELECT 1 FROM people WHERE people_id = ? LIMIT 1", (people_id,))
	result = cursor.fetchone()

	if not result:
		print(f"{'NOT OK':8}people_id does not exist.")
	else:
		updates:dict = {}
		if name_first != "NULL": updates["name_first"] = name_first
		if name_last != "NULL": updates["name_last"] = name_last
		if name_between != "NULL": updates["name_between"] = name_between
		if name_preferred != "NULL": updates["name_preferred"] = name_preferred
		if unique_description != "NULL": updates["unique_description"] = unique_description

		update_list:list = []
		for key, value in updates.items():
			update_list.append(f'{key} = "{value}"')

		if update_list:
			update_sql = ", ".join(update_list)

			UPDATE_person = f"""
			UPDATE people SET
				{update_sql}
			WHERE people_id = {people_id};
			"""
			execute_SQL(UPDATE_person)
	conn.close()

def dummy_data()->None:
	CREATE_people(unique_description= "my bitch sister whom I love and look up to")
	CREATE_people(unique_description= "test 2")
	CREATE_people(unique_description= "test 3")
	CREATE_people(unique_description= "test 4")
	CREATE_people(unique_description= "test 5")

	print("create_people done")

	UPDATE_people(
		people_id = 1, 
		name_first = "Gabrielle", 
		name_last = "Yongco", 
		name_between = "Zaci Memarion", 
		name_preferred = "Shobe/TiaMei"
	)
	UPDATE_people(2, name_first="two")
	UPDATE_people(3, name_first="three")
	UPDATE_people(4, name_first="four")
	UPDATE_people(5, name_first="five")

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	init_tables()
	dummy_data()
	
	section("END")
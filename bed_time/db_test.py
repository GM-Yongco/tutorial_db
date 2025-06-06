# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: 
# ========================================================================
# HEADERS
# ========================================================================

from db_utils import *
# ========================================================================
# FUNCTIONS 
# ========================================================================

def test():
	pass

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	init_table_sleep_log()
	CREATE_sleep_log(5, 11)
	# READ_sleep_log()
	READ_last_2()
	
	section("END")
import sqlite3

con = sqlite3.connect("suggestion.db")

cur = con.cursor()

# cur.execute("CREATE TABLE suggestion (\
#             weatherId int, \
#             plantId int, \
#             suggest_en varchar(255), \
#             suggest_akan varchar(255), \
#             suggest_dagbani varchar(255)\
#             )")
# cur.execute("""INSERT INTO suggestion VALUES 
#             (1, 1, 'suggestion test', 'suggestion test', 'suggestion test'),
#             (2, 2, 'suggestion test2', 'suggestion test2', 'suggestion test2'),
#             (3, 3, 'suggestion test3', 'suggestion test3', 'suggestion test3')""")

# con.commit()

def query_suggestion(weather:int, plant:int, language:int) -> str:
    res = cur.execute(f"SELECT suggest_en FROM suggestion WHERE weatherId={weather} and plantId={plant}")
    return res.fetchone()

# print(query_suggestion(1,1,1))
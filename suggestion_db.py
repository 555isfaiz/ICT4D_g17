import sqlite3



def query_suggestion(weather:int, plant:int, language:int) -> str:

    con = sqlite3.connect("suggestion.db")

    cur = con.cursor()

    # 5xx is rain, 3xx is drizzle
    # so 1 is rain, 2 is other(sun)
    if language == 1:
        column = "suggest_en"
    else:
        column = "suggest_fr"
    res = cur.execute(f"SELECT {column} FROM suggestion WHERE weatherId={weather} and plantId={plant}")
    return res.fetchone()[0]

print(query_suggestion(1,1,1))
print(query_suggestion(1,2,1))
print(query_suggestion(1,3,1))
print(query_suggestion(2,1,1))
print(query_suggestion(2,2,1))
print(query_suggestion(2,3,1))
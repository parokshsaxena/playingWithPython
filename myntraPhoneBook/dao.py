import rethinkdb as r

tableName = "directory"

def getConn():
	conn = r.connect(host = "localhost",
			port = 28015,
			db = "hackramp",
			auth_key = ""
			)
	return conn	
def initializeDB():
	conn = init()
	r.table("directory").insert({
		"id" : 1,
		"name" : "paroksh saxena",
		"phoneNum" : "8884190588",
		"emailId" : "paroksh.saxena@myntra.com"
	}).run(conn)

def getAllDocs():
	conn = getConn()
	for doc in r.table(tableName).run(conn):
    		print doc

def filterSearch(name):
    conn = getConn()
    docs = r.table(tableName).filter(
        r.row["name"].match("(?i)" + name)
    ).run(conn)
    result = []

    for doc in docs:
        result.append(doc)

    return result

#initializeDB()
#getAllDocs()
#filterSearch("paro")
#filterSearch("paroksh")
#filterSearch("proks")



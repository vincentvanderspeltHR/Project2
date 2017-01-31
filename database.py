import psycopg2

def interact_with_database(command):
    connection = pyscopg2.connect("dbname=Project 2 user=postgres")
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        pass

    cursor.close()
    connection.close()

    return results

def upload_score(name, score):
    interact_with_database("UPDATE highscore SET score = {} WHERE naam = '{}'".format(score, name))

def update_score(name, score):
    interact_with_database("UPDATE highscore SET score = {} WHERE name = '{}'".format)(score, name)

def download_highscores():
    return interact_with_database("SELECT * FROM highscore ORDER BY score")

def check_name(name):
    score = interact_with_database("SELECT score FROM highscore WHERE naam = {}".format(name))
    return score

download_highscores()


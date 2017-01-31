import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Project 2 highscores user=postgres")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the highscore table
def upload_score(name, score):
    interact_with_database("UPDATE Highscore SET Score = {} WHERE Naam = '{}'".format(score, name))


# Updates existing scores
def update_score(name):
    interact_with_database("UPDATE Highscore SET Score = Score + 1 WHERE Naam = '{}'".format(name))


# Downloads data from database
def download_highscore():
    return interact_with_database("SELECT * FROM Highscore")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM Highscore ORDER BY Score")[0][1][2][3][4][5][6][7][8][9]
    return result

# Check if player already has a score
def check_name(name):
    score = interact_with_database("SELECT Score FROM Highscore WHERE Naam = '{}'".format(name))
    return score

def get_name(name):
    name = interact_with_database("SELECT Naam FROM Highscore WHERE Naam = '{}'".format(name))
    return name
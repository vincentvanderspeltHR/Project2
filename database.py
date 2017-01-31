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
    result = interact_with_database("SELECT * FROM Highscore ORDER BY Score")
    return result

# Check if player already has a score
def check_name(name):
    score = interact_with_database("SELECT score FROM highscore where naam = '{}'".format(name))
    return score
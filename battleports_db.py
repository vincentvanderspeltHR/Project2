import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Project2 user=postgres password=HoI700XD port=6666")
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
def new_score(name, score):
    interact_with_database("INSERT INTO Highscore VALUES('{}', {})".format(name, score))


# Updates existing scores
def upload_score(name, score):
    interact_with_database("UPDATE Highscore SET Score = {} WHERE Naam = '{}'".format(score, name))


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM Highscore ORDER BY Score")
    return result

# Check if player already has a score
def check_name(name):
    score = interact_with_database("SELECT Score FROM Highscore WHERE Naam = '{}'".format(name))
    return score

def clear_save():
    interact_with_database("DELETE FROM game")
    interact_with_database("DELETE FROM player")
    interact_with_database("DELETE FROM boat")


def save_game(currentplayer , available_boats , setup_counter , special_deck , normal_deck , discard_pile):
    interact_with_database("INSERT INTO game VALUES('{}', '{}', {}, '{}', '{}', '{}')".format(currentplayer , available_boats , setup_counter , special_deck , normal_deck , discard_pile))

def save_player(name , score , boatlist , currentboat , cards_in_hand , pick_cards , trap_cards , destroyed_boats , emp_buff , attack_amount , sabotage_buff):
    interact_with_database("INSERT INTO player VALUES('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {})".format(name , score , boatlist , currentboat , cards_in_hand , pick_cards , trap_cards , destroyed_boats , emp_buff , attack_amount , sabotage_buff))

def save_boat(x, y, new_x, new_y, switch_x, length,
                               steps, original_stance,
                               new_stance, hp,
                               currenthp, range_buff,
                               horizontal_attackingrange,
                               vertical_attackingrange,
                               vertical_defendingrange,
                               damage_buff, movement,
                               original_attack_amount,
                               attack_amount, EMP,
                               special_card):
    interact_with_database("INSERT INTO boat VALUES({}, {}, {}, {}, {}, {}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(x, y, new_x, new_y, switch_x, length,
                               steps, original_stance,
                               new_stance, hp,
                               currenthp, range_buff,
                               horizontal_attackingrange,
                               vertical_attackingrange,
                               vertical_defendingrange,
                               damage_buff, movement,
                               original_attack_amount,
                               attack_amount, EMP,
                               special_card))
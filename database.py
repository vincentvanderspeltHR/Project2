import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Project2 password=3252AVKollen user=postgres")
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

def new_score(name, score):
    interact_with_database("INSERT INTO highscore VALUES('{}', {})".format(name, score))

# Downloads data from database
def download_top_score():
    scores = interact_with_database("SELECT * FROM highscore ORDER BY score DESC")
    return scores


# Check if player already has a score
def check_name(name):
    score = interact_with_database("SELECT Score FROM Highscore WHERE Naam = '{}'".format(name))
    return score

# Clears old save
def clear_save():
    interact_with_database("DELETE FROM game")
    interact_with_database("DELETE FROM player")
    interact_with_database("DELETE FROM boat")


# Save data
def save_game(currentplayer , playerlist , available_boats , setup_counter , special_deck , normal_deck , discard_pile):
    interact_with_database("INSERT INTO game VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(currentplayer , playerlist , available_boats , setup_counter , special_deck , normal_deck , discard_pile))

def save_player(naam , score , boatlist , currentboat , cards_in_hand , pick_cards , trap_cards , destroyed_boats , emp_buff , attack_amount , sabotage_buff):
    interact_with_database("INSERT INTO player VALUES('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {})".format(naam , score , boatlist , currentboat , cards_in_hand , pick_cards , trap_cards , destroyed_boats , emp_buff , attack_amount , sabotage_buff))

def save_boat(x , y , new_x , new_y , switch_x , boat_length , steps , original_stance , new_stance , hp , currenthp , range_buff , horizontal_attackingrange , vertical_attackingrange , vertical_defendingrange , damage_buff , movement , original_attack_amount , attack_amount , emp , special_card):
    interact_with_database("INSERT INTO boat VALUES({}, {}, {}, {}, {}, {}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(x , y , new_x , new_y , switch_x , boat_length , steps , original_stance , new_stance , hp , currenthp , range_buff , horizontal_attackingrange , vertical_attackingrange , vertical_defendingrange , damage_buff , movement , original_attack_amount , attack_amount , emp , special_card))

def load_game():
    game_data = interact_with_database("SELECT * FROM game")
    return game_data

def load_players():
    player_data = interact_with_database("SELECT * FROM player")
    return player_data

def load_boats():
    boat_data = interact_with_database("SELECT * FROM boat")
    return boat_data
import models
import exceptions as exception
import settings as constant

def get_player_name():
    while True:
        name = input("Enter username: ").strip(' ')
        if len(name) > 1:
            break
    return name

def play():
    bot, player, turn = models.Enemy(), models.Player(name = get_player_name()), 0
    try:
        while player.health_poitns != 0:
            if turn % 2 == 0:
                try:
                    player.attack(bot)
                    turn += 1
                except exception.EnemyDown:
                    print(f"Enemy of {bot.level}th level is defeated")
                    constant.STARTING_LVL += 1
                    bot = models.Enemy(level = constant.STARTING_LVL)
                    player.score += constant.SCORE_FOR_AN_ENEMY
            else:
                try:
                    player.defence(bot)
                    turn -= 1
                except exception.GameOver:
                    print(f"Game over. Your score = {player.score}")
                    with open('score.txt', 'a') as file:
                        file.write(f"{player.name}, {player.score}\n")
    except KeyboardInterrupt:
        print("\nGame over")

play()

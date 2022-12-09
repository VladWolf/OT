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
    name = get_player_name()
    bot = models.Enemy()
    player = models.Player(name)
    try:
        while player.health_poitns != 0:
                try:
                    player.attack(bot)
                    player.defence(bot)
                except exception.EnemyDown:
                    print(f"Enemy of {bot.level}th level is defeated")
                    bot = models.Enemy()
                    player.score += constant.SCORE_FOR_AN_ENEMY
                except exception.GameOver:
                    print(f"Game over. Your score = {player.score}")
                    with open('score.txt', 'a') as file:
                        file.write(f"{player.name}, {player.score}\n")
    except KeyboardInterrupt:
        print("\nGame over")

play()

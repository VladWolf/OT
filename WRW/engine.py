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
    while player.health_poitns != 0:
            try:
                player.attack(bot)
                player.defence(bot)
            except exception.EnemyDownError as enemy_down:
                print(enemy_down)
                bot = models.Enemy.level_up(bot)
                player.score += constant.SCORE_FOR_AN_ENEMY
            except exception.GameOverError as game_over:
                print(game_over)

if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print("\nGame over")

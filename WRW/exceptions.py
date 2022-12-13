class EnemyDownError(Exception):
    def __init__(self, level):
        self.level = level
    
    def __str__(self):
        return f"Enemy of {self.level}th level is defeated"


class GameOverError(Exception):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        with open('score.txt', 'a') as file:
            file.write(f"{self.name}, {self.score}\n")
        return f"Game over. Your score = {self.score}"

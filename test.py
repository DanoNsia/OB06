class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if not isinstance(other, Hero):
            raise ValueError("The target must be an instance of Hero class")

        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = 0  # 0 - игрок, 1 - компьютер
        print("Начало игры!")

        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0

            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            print("-" * 20)

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

def main():
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютер"

    game = Game(player_name, computer_name)
    game.start()

if __name__ == "__main__":
    main()
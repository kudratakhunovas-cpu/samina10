from game import start_game

if __name__ == "__main__":
    start_game()
from scenes import start_room, left_path, right_path

def start_game():
    life = 5

    while life > 0:
        choice, life = start_room(life)

        if choice == "left":
            life = left_path(life)

        elif choice == "right":
            result, life = right_path(life)

            if result == "exit":
                break

        if life <= 0:
            print("\nУ тебя больше нет жизней. Конец игры!")
            return
def start_room(life):
    print(f"\nУ тебя осталось жизней: {life}")
    print("Вы просыпаетесь в тёмном помещении.")
    print("1) Осмотреть комнату 2) Пойти налево 3) Пойти направо")

    choice = input("Что ты выберешь? (1/2/3): ")

    if choice == "1":
        print("Вы нашли записку и проход...")
        print("1) Пойти к проходу 2) Прочитать записку")
        c = input("Выбор: ")

        if c == "1":
            print("Минотавр убил вас!")
            life -= 1
            return None, life

        else:
            print("Записка: 'Не смотри назад...' — но минотавр поймал вас!")
            life -= 1
            return None, life

    elif choice == "2":
        return "left", life

    elif choice == "3":
        return "right", life

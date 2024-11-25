import json
import random

# JSON
def load_data_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def main():
    # Загружаем данные
    json_file = "questions.json"
    data = load_data_from_json(json_file)
    words_easy = data[0]["questions"][0]
    words_medium = data[0]["questions"][1]
    words_hard = data[0]["questions"][2]
    levels = data[1]["levels"]


    level_choice = input("Выберите уровень сложности (легкий, средний, тяжелый): ").strip().lower()
    if level_choice in ["легкий", "easy"]:
        words = words_easy
    elif level_choice in ["средний", "medium"]:
        words = words_medium
    elif level_choice in ["тяжелый", "hard"]:
        words = words_hard
    else:
        print("Уровень сложности не распознан, выбран легкий уровень.")
        words = words_easy

    answers = {}

    print("\nНачнем игру! Переведите следующие слова:")
    for word, translation in random.sample(list(words.items()), len(words)):
        hint = f"{len(translation)} букв, начинается на '{translation[0]}'"
        print(f"Слово: {word} ({hint})")

        user_answer = input("Ваш перевод: ").strip().lower()
        if user_answer == translation.lower():
            print(f"Верно! {word.capitalize()} — это {translation}.")
            answers[word] = True
        else:
            print(f"Неверно. {word.capitalize()} — это {translation}.")
            answers[word] = False


    correct_words = [word for word, correct in answers.items() if correct]
    incorrect_words = [word for word, correct in answers.items() if not correct]

    print("\nРезультаты:")
    print("Правильно отвечены слова:", ", ".join(correct_words) if correct_words else "нет")
    print("Неправильно отвечены слова:", ", ".join(incorrect_words) if incorrect_words else "нет")

    # Итог
    score = len(correct_words)
    rank = levels.get(str(score), "Неизвестный ранг")
    print(f"\nВаш ранг: {rank}")

if __name__ == "__main__":
    main()

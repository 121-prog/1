import json
import os
from datetime import datetime


def load_books():
    """Загрузка книг из JSON-файла"""
    if not os.path.exists("books.json"):
        return []
    with open("books.json", "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_books(books):
    """Сохранение книг в JSON-файл"""
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def add_book(books):
    """Добавление новой книги"""
    print("\n--- Добавление книги ---")
    
    author = input("Введите автора: ").strip()
    title = input("Введите название: ").strip()
    
    # Проверка на дубликаты
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Ошибка: такая книга уже существует!")
            return
    
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5!")
        except ValueError:
            print("Пожалуйста, введите число!")
    
    date_read = input("Введите дату прочтения (ДД.ММ.ГГГГ) или оставьте пустым для текущей даты: ").strip()
    if not date_read:
        date_read = datetime.now().strftime("%d.%m.%Y")
    
    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read
    }
    
    books.append(book)
    save_books(books)
    print(f'Книга "{title}" добавлена!')


def show_all_books(books):
    """Показать все книги"""
    print("\n--- Список всех книг ---")
    if not books:
        print("Список книг пуст.")
        return
    
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']} (оценка: {book['rating']}, дата: {book['date_read']})")


def show_average_rating(books):
    """Показать среднюю оценку"""
    print("\n--- Средняя оценка ---")
    if not books:
        print("Нет книг для расчета.")
        return
    
    avg_rating = sum(book["rating"] for book in books) / len(books)
    print(f"Средняя оценка: {avg_rating:.2f}")


def show_author_stats(books):
    """Статистика по авторам"""
    print("\n--- Статистика по авторам ---")
    if not books:
        print("Нет книг для статистики.")
        return
    
    authors = {}
    for book in books:
        author = book["author"]
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1
    
    for author, count in sorted(authors.items()):
        print(f"{author}: {count} кн.")


def delete_book(books):
    """Удалить книгу"""
    print("\n--- Удаление книги ---")
    if not books:
        print("Список книг пуст.")
        return
    
    show_all_books(books)
    
    while True:
        try:
            choice = int(input("\nВведите номер книги для удаления (0 для отмены): "))
            if choice == 0:
                print("Удаление отменено.")
                return
            elif 1 <= choice <= len(books):
                removed_book = books.pop(choice - 1)
                save_books(books)
                print(f'Книга "{removed_book["title"]}" удалена!')
                return
            else:
                print(f"Пожалуйста, введите число от 1 до {len(books)}!")
        except ValueError:
            print("Пожалуйста, введите число!")


def main():
    """Главная функция приложения"""
    books = load_books()
    
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("\nВыберите действие (1-6): ").strip()
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_all_books(books)
        elif choice == "3":
            show_average_rating(books)
        elif choice == "4":
            show_author_stats(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")


if __name__ == "__main__":
    main()

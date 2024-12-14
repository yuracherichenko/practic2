import datetime
import json
import random
import os

_DOWNLOAD_PATH = "Download/"
_ARTICLES_FILE = "articles.json"


class Article:
    def __init__(self, name):
        self.name = name
        self.likes = random.randint(0, 100)
        self.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        """Возвращает словарь для сериализации в JSON"""
        return {
            "name": self.name,
            "likes": self.likes,
            "created_at": self.created_at,
        }


def ensure_download_path():
    """Проверяет существование папки для загрузок, если нет — создает"""
    if not os.path.exists(_DOWNLOAD_PATH):
        os.makedirs(_DOWNLOAD_PATH)
        print(f"Папка {_DOWNLOAD_PATH} создана.")


def save_article_to_file(article: Article):
    """Сохраняет статью в общий JSON-файл"""
    path = os.path.join(_DOWNLOAD_PATH, _ARTICLES_FILE)
    
    # Загружаем существующий список статей, если файл уже есть
    articles = []
    if os.path.exists(path):
        with open(path, 'r') as f:
            articles = json.load(f)
    
    # Добавляем новую статью и сохраняем обратно
    articles.append(article.to_dict())
    with open(path, 'w') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)
    print(f"Статья '{article.name}' сохранена в файл: {path}")


def get_article():
    """Создает случайную статью"""
    return Article(f"Article {random.randint(1000, 9999)}")


def do_work():
    """Генерирует статью и сохраняет ее в общий файл"""
    article = get_article()
    save_article_to_file(article)


def read_all_articles():
    """Читает и выводит все статьи из общего JSON-файла"""
    path = os.path.join(_DOWNLOAD_PATH, _ARTICLES_FILE)
    if not os.path.exists(path):
        print("Файл с данными статей не найден.")
        return
    
    with open(path, 'r') as f:
        articles = json.load(f)
    
    print("\nВсе статьи из общего файла:")
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['name']} - {article['likes']} лайков (Создано: {article['created_at']})")


if __name__ == "__main__":
    # Подготовка папки для сохранения
    ensure_download_path()

    # Запрос количества статей от пользователя
    try:
        count = int(input("Введите количество статей для генерации: "))
        if count <= 0:
            raise ValueError("Число должно быть больше 0.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        count = 10  # Используется значение по умолчанию

    # Генерация статей
    for _ in range(count):
        do_work()

    print("\nВсе статьи успешно сохранены!")
    
    # Чтение и вывод всех статей
    read_all_articles()

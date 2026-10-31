class Language:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Construction:
    def __init__(self, id, name, element_count, language_id):
        self.id = id
        self.name = name
        self.element_count = element_count
        self.language_id = language_id

class LanguageConstruction:
    def __init__(self, construction_id, language_id):
        self.construction_id = construction_id
        self.language_id = language_id

languages = [
    Language(1, "Язык Python"),
    Language(2, "Язык C++"),
    Language(3, "Java"),
]

constructions = [
    Construction(1, "Арифметическое выражение", 3, 1),
    Construction(2, "Анонимная функция", 4, 1),
    Construction(3, "Цикл for", 6, 1),
    Construction(4, "Условный оператор", 4, 2),
    Construction(5, "Объявление класса", 6, 3),
]

language_constructions = [
    LanguageConstruction(1, 1),
    LanguageConstruction(1, 2),
    LanguageConstruction(2, 1),
    LanguageConstruction(2, 2),
    LanguageConstruction(5, 3),
]

def main():
    print("Задание 1")

    for language in languages:
        if "язык" in language.name.lower().split():
            names = []

            for construction in constructions:
                if construction.language_id == language.id:
                    names.append(construction.name)

            print(f"{language.name}: {', '.join(names)}")

    print("\nЗадание 2")

    result = []
    for language in languages:
        total_elements = 0
        amount = 0

        for construction in constructions:
            if construction.language_id == language.id:
                total_elements += construction.element_count
                amount += 1

        if amount > 0:
            average = round(total_elements / amount, 2)
            result.append((language.name, average))

    result.sort(key=lambda item: item[1])

    for name, average in result:
        print(f"{name}: {average:.2f} элементов")

    print("\nЗадание 3")

    for construction in constructions:
        if construction.name.lower().startswith("а"):
            names = []

            for link in language_constructions:
                if link.construction_id == construction.id:
                    for language in languages:
                        if language.id == link.language_id:
                            names.append(language.name)

            print(f"{construction.name}: {', '.join(names)}")

if __name__ == "__main__":
    main()

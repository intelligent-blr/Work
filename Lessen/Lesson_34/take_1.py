# ----------- ПРИМЕР 1 ----------
import re

text = """
Путешественник: Привет! Я путешественник из 2478 года. В какой год я попал?

Собеседник: Вы в 2024 году. Как вы здесь оказались?

Путешественник: Машина времени сбилась. Что у вас происходит?

Собеседник: Мы на пороге 202598 года. Климат меняется, технологии развиваются.

Путешественник: Интересно. В 2478 году мы уже колонизировали Марс и другие планеты. Что у вас в 2050?

Собеседник: В 2050 мы полностью перешли на возобновляемую энергию. А в 2200?

Путешественник: В 2200 году был первый контакт с внеземными цивилизациями. А что в 1800 году?

Собеседник: В 1800 году произошла промышленная революция. Что в 3000?

Путешественник: В 3000 году человечество стало межгалактической цивилизацией.

"""
# years = []
# for ch in list("?!.,:;"):
#     text = text.replace(ch, '')
#     text = text.lower()

# for word in text.split():
#     if word.isdigit():
#         years.append(word)
# print(years)

# ----------- ПРИМЕР 1 ----------
# pattern = r"20.."      # .. - любые два символа
# pattern = r"20\d\d"    # 2 цифры после 20
# pattern = r"20\d{4}"   # {4} - говорит что после 20 должно идти 4 цифры
# pattern = r"\d"
# pattern = r"\d{4}"
# pattern = r"\d{4}\sгод"
# result = re.findall(pattern, text)
# print(result)

# ----------- ПРИМЕР 2 ----------
# Получим все слова длины 3
# pattern = r"\b\w{3}\b"    #\b указывает что есть начало слова и конец слова и 3 буквы или цифры
# result = re.findall(pattern, text)
# print(result)


# ----------- ПРИМЕР 3 ----------
# pattern = r"\b\w{3,}\b"        # w{3,} - цифры или буквы 3 и более символов
# text = "Hello, how are you?"
# #
# result = re.findall(pattern, text)
# print(result)  # ['how', 'are', ‘you’]



# ----------- ПРИМЕР 4 ----------
# pattern = r"\b[Ttj]\w{2,}\b"            # [] - можно указать конкретные цифры или буквы в поиске
# text = "The quick brown fox jumps over the lazy dog. ttoday is a sunny day."

# result = re.findall(pattern, text)
# print(result)  # ['The', 'Today']


# ----------- ПРИМЕР 5 ----------
# слова длиной от 2 до 4 букв
# pattern = r"\b\w{2,4}\b"
# text = "A cat is happy"
# result = re.findall(pattern, text)
# print(result)  # ['cat', 'is']


# ----------- ПРИМЕР 6 ----------
# слова, заканчивающиеся на d
# pattern = r"\w*d\b"
# text = "I had a red card and a gold medal."
# print(re.findall(pattern, text)) # ['had', 'red', 'gold']



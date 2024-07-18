import re
from django import template


register = template.Library()

@register.filter()
def censor(text):

    if not isinstance(text, str):
        raise ValueError("Принимаем только строки")
    # Список нецензурных слов
    profanity_list = ['мурлыка', 'Редис', 'куча']
    # Заменяем каждое нецензурное слово на '*'
    for word in profanity_list:
        text = re.sub(r'\b{}\b'.format(word),word[0] + '*' * (len(word)-1), text, flags=re.IGNORECASE)
    return text
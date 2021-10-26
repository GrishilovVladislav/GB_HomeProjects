from random import randint
nouns = ["автомобиль", "лес", "огонь", "город", "дом", "я"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью","когда-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "угрюмый"]

def get_jokes(num):
  for i in range (0, num):
    print (nouns[randint(0,len(nouns)-1)],adverbs[randint(0,len(adverbs)-1)],adjectives[randint(0,len(adjectives)-1)])

get_jokes(10)
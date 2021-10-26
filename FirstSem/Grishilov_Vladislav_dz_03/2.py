def num_translate_adv(num):

  if num.istitle():
    return (eng_to_rus[num.lower()].capitalize())
  else: 
    return (eng_to_rus[num])

eng_to_rus = {
  'zero':'нуль', 
  'one':'один',
  'two':'два',
  'three':'три',
  'four':'четыре',
  'five':'пять',
  'six':'шесть',
  'seven':'семь',
  'eight':'восемь',
  'nine':'девять',
  'ten':'десять',
  '': 'None'
}
while True:
  word = input ('Enter your word: ')
  if word.lower() in eng_to_rus:
    print (num_translate_adv(word))
  else:
    print ('None')
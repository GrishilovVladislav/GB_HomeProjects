def num_translate(num):
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
  if word in eng_to_rus:
    print (num_translate(word))
  else:
    print ('None')
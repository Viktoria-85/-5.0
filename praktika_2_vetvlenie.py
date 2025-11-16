
rate_as_str = input("оцените работу оператора от 1 до 5:")
rate = int(rate_as_str)
if(rate<1):
    rate = 1
    print(rate)

    if(rate>5):
        rate = 5
        print(rate)

        print(rate)

feedbeck = ""

if rate == 1:
    feedbeck = input("расскажите, что нам улучшить?")

elif rate == 2:
        feedbeck = input("расскажите, что вас смутило?")
elif rate == 3:
      feedbeck = input("что вас смутило?")
elif rate == 4:
       feedbeck == input("спасибо за хорошую оценку")
else:
    if rate == 5:
         feedbeck == input("спасибо за высокую оценку!")





print((feedbeck))

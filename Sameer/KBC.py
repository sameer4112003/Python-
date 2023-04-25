questions = [
  [
    "Which language was used to make instagram ?", "Python","Java","C/C++","None",1
  ],
  [
    "Which language was used to make Facebook ?", "Python","Java","C/C++","None",2
  ],
  [
    "Which language was used to make Snapchat ?", "Python","Java","C/C++","None",3
  ],
  [
    "Which language was used to make Tiktok ?", "Python","Java","C/C++","None",4
  ],
  [
    "Which language was used to make YT ?", "Python","Java","C/C++","None",1
  ],
  [
    "Which language was used to make Linkedin ?", "Python","Java","C/C++","None",2
  ],
  [
    "Which language was used to make Twitter ?", "Python","Java","C/C++","None",3
  ],
  [
    "Which language was used to make Amazon ?", "Python","Java","C/C++","None",4
  ],
  [
    "Which language was used to make quikr ?", "Python","Java","C/C++","None",1
  ],
  [
    "Which language was used to make boat ?", "Python","Java","C/C++","None",2
  ],
  [
    "Which language was used to make lenkskart ?", "Python","Java","C/C++","None",3
  ],
  [
    "Which language was used to make emcure ?", "Python","Java","C/C++","None",4
  ],
  [
    "Which language was used to make sugar ?", "Python","Java","C/C++","None",1
  ],
  [
    "Which language was used to make cardekho ?", "Python","Java","C/C++","None",2
  ],
  [
    "Which language was used to make mamaearth ?", "Python","Java","C/C++","None",3
  ],
  [
    "Which language was used to make bharatpay ?", "Python","Java","C/C++","None",4
  ],
]

levels = [1000 , 2000, 3000, 4000, 10000,
         100000,200000,300000,400000,1000000,
         2000000,3000000,4000000,10000000]
money = 0
for i in range(0,len(questions)):
  question = questions[i]
  print(f"The price money for this question is {levels[i]}")
  print(f"a. {question[1]}         b. {question[2]}")
  print(f"c. {question[3]}         d. {question[4]}")
  Reply = int(input("Enter your answer : "))
  if(Reply==question[-1]):1
    print(f"Congrats, you've won Rs.{levels[i]}
    if(i==5):
      money = 10000
    elif(i==10):
      money = 1000000
    elif(i==15):
      money=10000000
  else:
    print("Wrong answer")
    break

print(f" The final money you've won is {money}")

    
  
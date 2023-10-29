from questions import questions

questionsAnswers = [
    "What is the best weather in bahrain ? \n (a) Cold\n (b) Hot \n (c) Rain \n",
    "What is the best weather in UK ? \n (a) Cold\n (b) Hot \n (c) Rain \n",
    "What is the best weather KSA ? \n (a) Cold\n (b) Hot \n (c) Rain \n",
    "What is the best weather  UEA ? \n (a) Cold\n (b) Hot \n (c) Rain \n"
]

qList = [
    questions(questionsAnswers[0],"c"),
    questions(questionsAnswers[1],"b"),
    questions(questionsAnswers[2],"a"),
    questions(questionsAnswers[3],"a")
]


def runn (ques):
    score =0
    for quess in ques:
        answer = input(quess.question)
        if answer == quess.answer:
            score+=1
    print("\n Your score is "+ str(score)+ "/" + str(len(questionsAnswers)))  

runn(qList)



import random

phrasal_verbs = [
    {"english": "ask out", "portuguese": "convidar para sair"},
    {"english": "bring up", "portuguese": "mencionar"},
    {"english": "call back", "portuguese": "ligar de volta"},
    {"english": "call off", "portuguese": "cancelar"},
    {"english": "call up", "portuguese": "ligar para alguém"},
    {"english": "check out", "portuguese": "conferir"},
    {"english": "come back", "portuguese": "voltar"},
    {"english": "come in", "portuguese": "entrar"},
    {"english": "come over", "portuguese": "visitar"},
    {"english": "come up", "portuguese": "surgir"},
    {"english": "cut off", "portuguese": "interromper"},
    {"english": "do over", "portuguese": "fazer de novo"},
    {"english": "drop off", "portuguese": "deixar, largar"},
    {"english": "figure out", "portuguese": "compreender"},
    {"english": "find out", "portuguese": "descobrir"},
    {"english": "get along", "portuguese": "dar-se bem"},
    {"english": "get away", "portuguese": "escapar"},
    {"english": "get back", "portuguese": "voltar"},
    {"english": "get up", "portuguese": "levantar-se"},
    {"english": "give away", "portuguese": "dar, doar"},
    {"english": "give in", "portuguese": "desistir"},
    {"english": "give back", "portuguese": "devolver"},
    {"english": "give up", "portuguese": "desistir"},
    {"english": "go away", "portuguese": "ir embora"},
    {"english": "go back", "portuguese": "voltar"},
    {"english": "go on", "portuguese": "continuar"},
    {"english": "go out", "portuguese": "sair"},
    {"english": "grow up", "portuguese": "crescer"},
    {"english": "hang out", "portuguese": "sair"},
    {"english": "hang up", "portuguese": "desligar"},
    {"english": "hold on", "portuguese": "aguardar"},
    {"english": "keep on", "portuguese": "continuar"},
    {"english": "let down", "portuguese": "decepcionar"},
    {"english": "look after", "portuguese": "cuidar de"},
    {"english": "look for", "portuguese": "procurar"},
    {"english": "look forward to", "portuguese": "ansiar por"},
    {"english": "look out", "portuguese": "ter cuidado"},
    {"english": "look up", "portuguese": "pesquisar"},
    {"english": "make out", "portuguese": "entender"},
    {"english": "make up", "portuguese": "inventar"},
    {"english": "pick up", "portuguese": "buscar"},
    {"english": "put away", "portuguese": "guardar"},
    {"english": "put off", "portuguese": "adiar"},
    {"english": "put on", "portuguese": "vestir"},
    {"english": "put out", "portuguese": "apagar"},
    {"english": "put up with", "portuguese": "tolerar"},
    {"english": "run into", "portuguese": "encontrar por acaso"},
    {"english": "run over", "portuguese": "revisar rapidamente"},
    {"english": "run out of", "portuguese": "ficar sem"},
    {"english": "set up", "portuguese": "configurar, montar"},
    {"english": "set off", "portuguese": "partir"},
    {"english": "show up", "portuguese": "aparecer"},
    {"english": "shut up", "portuguese": "calar-se"},
    {"english": "take after", "portuguese": "puxar a alguém"},
    {"english": "take away", "portuguese": "levar embora"},
    {"english": "take back", "portuguese": "devolver"},
    {"english": "take off", "portuguese": "decolar"},
    {"english": "take out", "portuguese": "tirar"},
    {"english": "take over", "portuguese": "assumir o controle"},
    {"english": "take up", "portuguese": "começar um hobby"},
    {"english": "throw away", "portuguese": "jogar fora"},
    {"english": "try on", "portuguese": "experimentar roupa"},
    {"english": "turn on", "portuguese": "ligar"},
    {"english": "wake up", "portuguese": "acordar"},
    {"english": "warm up", "portuguese": "aquecer"},
    {"english": "watch out", "portuguese": "prestar atenção"},
    {"english": "write down", "portuguese": "anotar"},
    {"english": "break down", "portuguese": "quebrar"},
    {"english": "break up", "portuguese": "terminar um relacionamento"},
    {"english": "bring back", "portuguese": "trazer de volta"},
    {"english": "bring in", "portuguese": "trazer, introduzir"},
    {"english": "bring out", "portuguese": "revelar"},
    {"english": "bring over", "portuguese": "trazer alguém"},
    {"english": "bring together", "portuguese": "juntar"},
    {"english": "bring up", "portuguese": "mencionar"},
    {"english": "carry on", "portuguese": "continuar"},
    {"english": "carry out", "portuguese": "realizar"},
    {"english": "come across", "portuguese": "encontrar por acaso"},
    {"english": "come along", "portuguese": "acompanhar"},
    {"english": "come apart", "portuguese": "desmanchar"},
    {"english": "come down", "portuguese": "descer"},
    {"english": "come off", "portuguese": "desprender-se"},
    {"english": "come out", "portuguese": "revelar"},
    {"english": "come over", "portuguese": "visitar"},
    {"english": "come through", "portuguese": "passar por"},
    {"english": "come up with", "portuguese": "sugerir"},
    {"english": "cut back", "portuguese": "reduzir"},
    {"english": "cut down", "portuguese": "reduzir"},
    {"english": "cut in", "portuguese": "interromper"},
    {"english": "cut out", "portuguese": "excluir"},
    {"english": "drop by", "portuguese": "dar uma passada"},
    {"english": "drop out", "portuguese": "abandonar"},
    {"english": "fall apart", "portuguese": "desmoronar"},
    {"english": "fall down", "portuguese": "cair"},
    {"english": "fall for", "portuguese": "apaixonar-se"},
    {"english": "fall off", "portuguese": "cair de"},
    {"english": "fall out", "portuguese": "cair"},
    {"english": "fall over", "portuguese": "tropeçar e cair"},
]

def quiz_user(phrasal_verbs, limit=10):
    random.shuffle(phrasal_verbs)
    
    # Limit the number of questions to 'limit' or the length of the list if smaller
    questions = phrasal_verbs[:limit]
    
    score = 0

    for verb in questions:
        print(f"How do you say '{verb['english']}' in Portuguese?")
        user_answer = input("Your answer:\n").strip().lower()
        if user_answer == verb['portuguese'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{verb['portuguese']}'.")
            print("Don't worry, keep practicing and you'll get better!")

    print(f"Your final score is: {score}/{len(questions)}")
    print("Well done! You are improving your vocabulary, keep going!!!")

def main():
    print("Welcome to the English Learning App - Most Common Phrasal Verbs")
    
    while True:
        input("Press enter to start the quiz\n")
        quiz_user(phrasal_verbs)
        
        # Ask user if they want to retake the quiz
        retry = input("Do you want to take the quiz again? (yes/no):\n").strip().lower()
        while retry not in ['yes', 'no']:
            retry = input("Please write 'yes' or 'no':\n ").strip().lower()
        if retry != 'yes':
            break
    
    print("Thank you for playing! Have a great day!")

# Call the function to start the app
main()
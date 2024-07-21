from random import choice, randint

def get_response(user_input: str)-> str :
    lowered: str= user_input.lower()
    if lowered=='':
        return "Well, wouldn't you like to talk to me?"
    elif 'hello' in lowered:
        return "Hello There!"
    elif 'how are you?' in lowered:
        return " Good haha what about you?"
    elif 'bye' in lowered: 
        return 'see you again!'
    elif  "roll a dice" in lowered:
        return f'You rolled:{randint(1,6)}'
    else:
        return choice(['could you explain that further?',
                       'i do not follow..',
                       'what are you saying?'])
    
     
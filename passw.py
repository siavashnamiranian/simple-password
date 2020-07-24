#simple password

import random

def passw(pass_lenght,strenght):
    weak = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    medium = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t','u','v',
              'w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    strong = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t','u','v',
              'w','x','y','z','1','2','3','4','5','6','7','8',
              '9','0','/','#','-','_','%','&','@','$']
    if strenght=="weak":
        p =  "".join(random.sample(weak,pass_lenght ))
        return p
    elif strenght=="average":
        pass_lenght_average=pass_lenght
        p =  "".join(random.sample(medium,pass_lenght_average))
        return p
    elif strenght=="hard":
        pass_lenght_hard=pass_lenght
        p =  "".join(random.sample(strong,pass_lenght_hard))
        return p
    else:
        print(" wrong_input ")

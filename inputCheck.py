class InputCheck:
    def __init__(self):
        """Setts accepted verbs and directions"""
        self.verbs = ['jump','look','open','close','take','drop','attack','walk','go', 'inventory']

        north = ['n','north']
        south = ['s','south']
        east = ['e','east']
        west = ['w','west']
        self.directions = [north, south, east, west]


 
    def check_verb(self, user_input):
        """Takes user input and try to analyse it.
        Checks if user typed in a verb thats in list
        or a direction
        Returns -> verb/direction(singel letter)"""
        
        user_input = user_input.lower()
        for verb in self.verbs:
            #Check if any verb is in user input
            #return return the verb 
            if verb in user_input:
                #If the verb is 'walk' or 'go' check the direction to go
                if verb in ('walk','go'):
                    return(self.what_direction(user_input))
                else:
                    print (verb)
                    return verb

        for direction in self.directions:
            #If there where no verbs in user input check if there is 
            #directions ex 'n' or 'north'
            if direction[0] == user_input or direction[1] == user_input:
                return direction[0]

        print("Sorry I did not understand that -.-")

 
    def what_direction(self, user_input):
        """Check what direction the user wants to go"""
        for direction in self.directions:
            if direction[1] in user_input: 
                return direction[0]

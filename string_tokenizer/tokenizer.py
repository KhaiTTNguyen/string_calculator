import re

class TagManipulator:
    def __init__(self):
        self.tokens = []

    def parse_string(self, expr):
        # regex = ",\\ *"
        
        # tempResult = re.split(regex, exp)

        # if len(tempResult) > 0:
        #     for tag in tempResult:
        #         self.tokens.append(tag)

        #     result = self.tokenise( self.tokens )

        return expr
       

    def parse_string(self, expr, regex): 
        result = [] 
        tempResult = re.split( regex, expr ) 
        if( len(tempResult[0]) > 0 ): 
            result = tempResult 
        
        return result
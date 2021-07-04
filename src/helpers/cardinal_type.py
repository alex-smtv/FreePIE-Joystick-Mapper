class CardinalType:

    N  = 4500 * 0 
    NE = 4500 * 1
    E  = 4500 * 2
    SE = 4500 * 3
    S  = 4500 * 4
    SW = 4500 * 5
    W  = 4500 * 6
    NW = 4500 * 7

    ALLOWED_VALUES = {
        "N"  : N ,
        "NE" : NE,
        "E"  : E ,
        "SE" : SE,
        "S"  : S ,
        "SW" : SW,
        "W"  : W ,
        "NW" : NW,
    }

    @staticmethod
    def is_value_allowed(value):
        if type(value) is not str and type(value) is not int:
            return False
        
        if type(value) is str:
            value = value.upper()

        found = False
        
        for allowed_value in CardinalType.ALLOWED_VALUES:
            if type(value) is str:
                found = (value == allowed_value)
            
            elif type(value) is int:
                found = (value == CardinalType.ALLOWED_VALUES[allowed_value])
            
            if found:
                break

        return found
    
    @staticmethod
    def retrieve_value_from(cardinal):
        if CardinalType.is_value_allowed(cardinal):
            
            if type(cardinal) is str:
                return CardinalType.ALLOWED_VALUES[cardinal.upper()]
            elif type(cardinal) is int:
                return cardinal
            else:
                raise RuntimeError("CardinalType edge case: the value {} could not be retrieved.".format(cardinal))

        else:
            raise ValueError("The cardinal {} could not be validated.".format(cardinal))
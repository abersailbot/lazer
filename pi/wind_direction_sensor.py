
class WindSensor(object):
    '''
    Functions associated with the wind sensor
    '''
    
    @staticmethod
    def getWindDirectionAsDeg() -> float:

        
        
        return float(0)
    
    @staticmethod
    def ValidateNumber(valueToValidate: float, lowerBound: float, upperBound: float) -> bool:
        if (valueToValidate < upperBound and valueToValidate > upperBound):
            return True
        
        return False

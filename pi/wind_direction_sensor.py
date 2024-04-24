
class WindSensor(object):
    '''
    Functions associated with the wind sensor
    '''
    
    @staticmethod
    def getWindDirectionAsDeg() -> float:

        #Create table of values of resistance and angle of wind_direction_sensor and return that value
        
        return float(0)
    
    @staticmethod
    def ValidateNumber(valueToValidate: float, lowerBound: float, upperBound: float) -> bool:
        if (valueToValidate < upperBound and valueToValidate > lowerBound):
            return True
        
        return False

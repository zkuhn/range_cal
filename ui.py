
class TextUI(object):
    
    def __init__(self):
        pass
    
    def ask_sensor_fixture_assignment(self):
        
        
        input_correct = False
        sensor_id, fixture_id = "", ""
        while not input_correct:
            print("please enter sensor id/serial num:")
            sensor_id = input()
            print("please enter the fixture number you placed the sensor in:")
            fixture_id = input()
            
            print("You've entered: ")
            print("serial_number/sensor_id = {}".format(sensor_id))
            print("fixture_id = {}".format(fixture_id))
            print("Is this correct? ?(Y/n)")        
            correct = input()
            
            if (correct == "") or (correct.lower() == "y"):
                input_correct = True
            
        return sensor_id, fixture_id    
        
        
    def ask_done(self):
        print("Are you done entering sensor/fixture pairs?(Y/n)")
        correct = input()
        return  (correct == "") or (correct.lower() == "y")
    
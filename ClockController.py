from Displays import LCDDisplay
from Button import *
from Clock import *
from Counters import *

class ClockController:
    """ our implementation of the clock controller
        4 butons for setting month, date, hour, min, LCD display to show the time
    """

    def __init__(self):
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                            Button(11, 'red', buttonhandler=self),
                            Button(12, 'yellow', buttonhandler=self),
                            Button(13, 'blue', buttonhandler=self)]

    def _getdaysinmonth(self, month):
        # create a dictionary for how many days are in each month
        monthdays = {
            1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
        }
        return monthdays.get(month)                    
        
    def showTime(self):
            """ show the time on the display """

            (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
            self._display.showText(f"{'tick tock'}\n{month:02}/{date:02}\n{hour:02} : {minute:02} : {sec:02}")   
            

    def buttonPressed(self, name):
        if name == 'yellow':
            # get the current hour
            hour = self._clock.getHour() 
            if hour == 23:
                self._clock.setHour(0)
            else:
            # set the hour to 1 + the current hour
                self._clock.setHour(hour + 1)

        if name == 'blue' :
            # get the current minute
            minute = self._clock.getminute()
            if minute == 59:
                self._clock.setminute(0)
            # set the minute to 1 + the current minute
            else:
                self._clock.setminute(minute + 1)

        if name == 'white':
            month = self._clock.getmonth()
            if month == 12:
                self._clock.setmonth(1)
            else:    
                self._clock.setmonth(month + 1)

        
        if name == 'red':
            month, date = self._clock.getmonth(), self._clock.getdate()
            if date == self._getdaysinmonth(month):
                self._clock.setdate(1)
            else:    
                self._clock.setdate(date + 1)    


        

    def buttonReleased(self, name):
        pass              
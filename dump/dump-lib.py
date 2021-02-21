# Author: Christopher Herzog
# Purpose: Dump Library to integrate into applications

#import logger
import os

class dump:

    # configure dump, allow defaults to be overwritten
    
    # get configuration information
    def dumper_loc(self, location=None):
        if location is None:
            raise Exception("Location cannot be None.")
        elif location != None:
            # Test Run, not a valid location. For Testing purposes.
            if location == 'Test' or location == 'test':
                return(self.location)

            #check if location is directory
            if os.path.exists(location) is False:
                raise Exception("Not a valid directory location.")
            else:
                return(self.location)
    
    def backup_dev(self, name=None):
        if name is None:
            raise Exception("Backup evice Name cannot be None.")
        else:
            return(self.name)

    def input_dev(self, name=None):
        if name is None:
            raise Exception("Input device Name cannot be None.")
        else:
            return(self.name)

    def backup_mntpnt(self, location='/mnt/'):
        #check if location is directory

        return(self.location)
    
    def input_mntpnt(self, location='/mnt/'):
        return(self.location)

    # locate backup device < not configurable >

    # verify USB devices < not configurable >

    # make udev rules < not configurable > 

    # mount backup device < not configurable >

    # perform backup < not configurable >

    # unmount backup < not configurable >


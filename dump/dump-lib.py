# Author: Christopher Herzog
# Purpose: Dump Library to integrate into applications

#import logger


class dump:
    
    import os

    # configure dump, allow defaults to be overwritten
    def dumper_loc(self, location=None):

        dumper_loc_location = str(location)

        if dumper_loc_location is None:
            raise Exception("Location cannot be None.")
        elif dumper_loc_location != None:
            # Test Run, not a valid location. For Testing purposes.
            if dumper_loc_location == 'Test' or dumper_loc_location == 'test':
                return(dumper_loc_location)

            #check if location is directory
            if os.path.exists(dumper_loc_location) is False:
                raise Exception("Not a valid directory location.")
            else:
                return(dumper_loc_location)

    def backup_dev(self, name=None):

        backup_dev_name = str(name)

        if backup_dev_name is None:
            raise Exception("Backup device Name cannot be None.")
        else:
            return(backup_dev_name)

    def input_dev(self, name=None):

        input_dev_name = str(name)

        if input_dev_name is None:
            raise Exception("Input device Name cannot be None.")
        else:
            return(input_dev_name)

    def backup_mntpnt(self, location='/mnt/'):

        backup_mntpnt_location = str(location)

        if backup_mntpnt_location is None:
            raise Exception("Backup Location cannot be None.")
        elif backup_mntpnt_location != None:
            # Test Run, not a valid location. For Testing purposes.
            if backup_mntpnt_location == 'Test' or backup_mntpnt_location == 'test':
                return(backup_mntpnt_location)

            #check if location is directory
            if os.path.exists(backup_mntpnt_location) is False:
                raise Exception("Not a valid directory location.")
            else:
                return(backup_mntpnt_location)

    def input_mntpnt(self, location='/mnt/'):

        input_mntpnt_location = str(location)

        if input_mntpnt_location is None:
            raise Exception("Input Location cannot be None.")
        elif input_mntpnt_location != None:
            # Test Run, not a valid location. For Testing purposes.
            if input_mntpnt_location == 'Test' or input_mntpnt_location == 'test':
                return(input_mntpnt_location)

            #check if location is directory
            if os.path.exists(input_mntpnt_location) is False:
                raise Exception("Not a valid directory location.")
            else:
                return(input_mntpnt_location)

    # locate backup device < not configurable >

    # verify USB devices < not configurable >

    # make udev rules < not configurable >

    # mount backup device < not configurable >

    # perform backup < not configurable >

    # unmount backup < not configurable >




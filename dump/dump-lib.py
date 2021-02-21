# Author: Christopher Herzog
# Purpose: Dump Library to integrate into applications

#import logger
import os

class dump:

    def dump_config(self, dumper_loc_location=None, backup_dev_name=None, input_dev_name=None,
                    backup_mntpnt_location='/mnt/', input_mntpnt_location='/mnt/', ):

        # configure dump, allow defaults to be overwritten
        def dumper_loc(self):

            dumper_loc_location = str(dumper_loc_location)

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

        def backup_dev(self):

            backup_dev_name = str(backup_dev_name)

            if backup_dev_name is None:
                raise Exception("Backup device Name cannot be None.")
            else:
                return(backup_dev_name)

        def input_dev(self):

            input_dev_name = str(input_dev_name)

            if input_dev_name is None:
                raise Exception("Input device Name cannot be None.")
            else:
                return(input_dev_name)

        def backup_mntpnt(self):

            backup_mntpnt_location = str(backup_mntpnt_location)

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

        def input_mntpnt(self):

            input_mntpnt_location = str(input_mntpnt_location)

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


    def dump_start(self, *args):
        import configparser
        import subprocess
        import usb
        import logger
        import pyudev
        import sys
        import re

        #Define default value for Debug
        for item in args:
            if item.lower() == 'true':
                debug = True
            else:
                debug = False

        def find_backup(self):

            #Find all USB Devices
            connected_usb = usb.core.find(find_all=True)
            
            #Check if no devices are connected
            if connected_usb == None:
                raise ValueError('No Devices Found.')

            #Loop through connected devices and append to array
            device_list = {}

            for device in connected_usb:
                usb_device = usb.util.get_string(device, device.iManufacturer)
                usb_device = str(usb_device)
                usb_device_vendorID = hex(device.idVendor)
                usb_device_productID = hex(device.idProduct)
                device_list[usb_device] = usb_device_vendorID, usb_device_productID

                if debug:
                    print('connected_usb: ', connected_usb, 'usb_device: ', usb_device, '\nusb_device_vendorID: ', usb_device_vendorID,
                        '\nusb_device_productID: ', usb_device_productID, '\ndevice_list[usb_device]: ', device_list[usb_device])
                else:
                    raise("Invalid argument value for dump_start(True|False).")

            return device_list

        def verify_usb(self, usb_device_list, backup_dev_name, input_dev_name):
            backup_device = backup_device.lower()
            input_device = input_device.lower()
            
            usb_list = {}
            for device, value in usb_device_list.items():
                print(usb_device_list[device][1])
                if backup_device in device.lower():
                    print('found the backup device')
                    backup_usb_device_vendor = usb_device_list[device][0]
                    backup_usb_device_product = usb_device_list[device][1]
                    #usb_list[device] = backup_usb_device_product
                    
                if input_device in device.lower():
                    print('found the input device')
                    input_usb_device_vendor = usb_device_list[device][0]
                    input_usb_device_product = usb_device_list[device][1]

            if debug:
                print('backup_device: ', backup_device, '\ninput_device: ', input_device, '\nbackup_usb_device_vendorID: ', backup_usb_device_vendor,
                '\nbackup_usb_device_productID: ', backup_usb_device_product, '\ninput_usb_device_vendorID: ', input_usb_device_vendor,
                '\ninput_usb_device_productID: ', input_usb_device_product)
    
            return backup_usb_device_vendor, input_usb_device_vendor, backup_usb_device_product, input_usb_device_product

    # make udev rules < not configurable >

    # mount backup device < not configurable >

    # perform backup < not configurable >

    # unmount backup < not configurable >




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
        '''
            args: [0]debug(True|False), [1]auto_unmount(True|False)
        '''
        
        import configparser
        import subprocess
        import usb
        import logger
        import pyudev
        import sys
        import re

        # Define default value for Debug
        if args[0].lower() == 'true':
            debug = True
        else:
            debug = False

        # Define value to auto unmount
        if args[1].lower() == 'true':
            unmount = True
        else:
            unmount = False

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
                    raise Exception("Invalid argument value for dump_start(True|False).")

            return device_list

        def verify_usb(self, usb_device_list, backup_dev_name, input_dev_name):
            
            backup_device = backup_device.lower()
            input_device = input_device.lower()
            
            usb_list = {}
            for device, value in usb_device_list.items():
                print(usb_device_list[device][1])
                if backup_device in device.lower():
                    if debug:
                        print('found the backup device')
                    backup_usb_device_vendor = usb_device_list[device][0]
                    backup_usb_device_product = usb_device_list[device][1]
                    #usb_list[device] = backup_usb_device_product
                    
                if input_device in device.lower():
                    if debug:
                        print('found the input device')
                    input_usb_device_vendor = usb_device_list[device][0]
                    input_usb_device_product = usb_device_list[device][1]

            if debug:
                print('backup_device: ', backup_device, '\ninput_device: ', input_device, '\nbackup_usb_device_vendorID: ', backup_usb_device_vendor,
                '\nbackup_usb_device_productID: ', backup_usb_device_product, '\ninput_usb_device_vendorID: ', input_usb_device_vendor,
                '\ninput_usb_device_productID: ', input_usb_device_product)
    
            return backup_usb_device_vendor, input_usb_device_vendor, backup_usb_device_product, input_usb_device_product

        def make_udev_rules(self, backup_vendorID, input_vendorID, backup_productID, input_productID, dumper_loc):
           
            udev_file_source = open('/etc/udev/rules.d/10.autobackup_source.rules', 'w+')
            udev_file_backup = open('/etc/udev/rules.d/11.autobackup_backup.rules', 'w+')
            
            #strip first two characters of hex
            backup_vendorID = backup_vendorID.strip('0x')
            backup_productID = backup_productID.strip('0x')
            input_vendorID = input_vendorID.strip('0x')
            input_productID = input_productID.strip('0x')
            
            write_str_source = """ACTION="add", ATTRS{idVendor}=""" + '''"''' + input_vendorID + '''", ATTRS{idProduct}="''' + input_productID + '''",''' + """ RUN+="/usr/bin/sudo /usr/bin/python3 """ + dumper_loc + '''"'''

            udev_file_source.write(str(write_str_source))

            udev_file_source.close()

            write_str_backup = """ACTION="add", ATTRS{idVendor}=""" + '''"''' + backup_vendorID + '''", ATTRS{idProduct}="''' + backup_productID + '''",''' + """ RUN+="/usr/bin/sudo /usr/bin/python3 """ + dumper_loc + '''"'''

            udev_file_backup.write(str(write_str_backup))

            udev_file_backup.close()

            #reload udev rules
            subprocess.run('udevadm control --reload', shell=True)

            if debug:
                print('udev_file_source: ', udev_file_source, '\nudev_file_backup: ', udev_file_backup,
                    '\nbackup_vendorID: ', backup_vendorID, '\nbackup_productID: ', backup_productID,
                    '\ninput_vendor_id: ', input_vendorID, '\ninput_productID: ', input_productID,
                    '\nudev source rule: ', write_str_source, '\nudev backup rule: ', udev_file_backup)

        def mount_usb(self, dbl, dil, mbl, mil, backup_name, input_name):
            
            check_path_backup = (mbl + 'backup')
            check_path_input = (mil + 'source')

            if os.path.exists(check_path_backup):
                if debug:
                    print('check_path_backup: path already exists.')
                pass
            else:
                #make dir for mount point
                makedir_backup = ('mkdir ' + mbl + 'backup')
                os.system(makedir_backup)

            #make mount point for backup usb
            backup_command = ('sudo mount -t auto ' + dbl + ' ' + mbl + 'backup')
            
            os.system(backup_command)
            
            if os.path.exists(check_path_input):
                if debug:
                    print('check_path_input: path already exists.')
                pass
            else:
                #make dir for mount point
                makedir_input = ('mkdir ' + mil + 'source')
                os.system(makedir_input)

            
            #make mount point for input usb
            input_command = ('sudo mount -t auto ' + dil + ' ' + mil + 'source')

            os.system(input_command)

            if debug:
                print('Make Backup Mount Point Directory: ', makedir_backup,
                    '\nMake Input Mount Point Directory: ', makedir_input)

        # TODO: change the variables to the global configuration variables
        def run_autobackup(self, dev_backup_loc, dev_input_loc, mnt_backup_loc, mnt_input_loc, backup_name, input_name):

            INPUT_SOURCE = (mnt_input_loc + 'source')
            INPUT_DEVICE = (dev_input_loc)
            BACKUP_SOURCE = (mnt_backup_loc + 'backup')
            BACKUP_DEVICE = (dev_backup_loc)
            
            command = ('''rsync -a {0} {1} ''').format(INPUT_SOURCE, BACKUP_SOURCE)

            result = subprocess.run(command, shell=True)
        
        if unmount:
            def unmount_drives():

                print('unmounting drives...')
                command = ('''umount /mnt/*''')

                subprocess.run(command, shell=True)

                print('Safe to remove drives')
        
    def umount(self):

        print('unmounting drives...')
        command = ('''umount /mnt/*''')

        subprocess.run(command, shell=True)

        print('Safe to remove drives')




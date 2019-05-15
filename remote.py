import sys
from wakeonlan import send_magic_packet
from pywebostv.discovery import discover
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl, InputControl

# Send a wake on lan broadcast to your TV.
# This will ensure the TV is on, before trying to connect.
send_magic_packet('<TV MAC ADDRESSES>')

# The 'store' gets populated during the registration process. If it is empty, a registration prompt
# will show up on the TV. You can pass any dictionary-like interface instead.
store = {}


client = WebOSClient("<TV IP>")
client.connect()
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("\nPlease accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("\nRegistration successful!")
        # print(store)

media = MediaControl(client)
system = SystemControl(client)
inp = InputControl(client)


def volume_set():
    print('\nWhat volume level do you want? [0-100]')
    try:
        volume_level = int(input('> '))
        if -1 < volume_level < 101:  # Check if range of 1-100
            media.set_volume(volume_level)
        else:
            print('Not a valid range, please use a range of 1-100.')
    except ValueError:
        print('That\'s not a valid number.')


def volume_mute():
    print('\nWould you like to mute or unmute?')
    mute_val = input('> ')

    if mute_val == 'mute':
        media.mute(True)
    elif mute_val == 'unmute':
        media.mute(False)
    else:
        print('That is not a valid value. Please type "mute" or "unmute".')


def volume_info():
    volume = media.get_volume()
    print('\nCurrent volume level is ', volume['volume'])
    print('Mute: ', volume['muted'])


def up_volume_lvl():
    media.volume_up()
    print('\nVolume increased by 1')


def down_volume_lvl():
    media.volume_down()
    print('\nVolume decreased by 1')


def sys_info():
    # Return Sysetem info in a dictionary
    system_info = system.info()
    print('\nProduct Name: ' + system_info['product_name'])
    print('Model Name: ' + system_info['model_name'])
    print('Software Version: ',
          system_info['major_ver'] + '.' + system_info['minor_ver'])
    print('MAC Address: ' + system_info['device_id'])
    print('Country: ' + system_info['country'])
    print('Language: ' + system_info['language_code'])


def kb_input():
    print('\nType your text below:')
    user_input = input('> ')
    inp.type(user_input)


def unknown_command():
    print('That\'s not a valid command.')


menu = {
    "0": sys.exit(),
    "1": volume_set,
    "2": volume_mute,
    "3": system.power_off,
    "4": volume_info,
    "5": up_volume_lvl,
    "6": down_volume_lvl,
    "7": sys_info,
    "8": kb_input
}


while True:
    # Ask the user what they would like to do after connecting
    print('\n\nWhat would you like to do? Choose only the number.\n')
    print('[0]Exit the program')
    print('[1]Set the volume level\n[2]Mute or unmute the volume\n[3]Turn off')
    print('[4]Current volume level\n[5]Volume up 1\n[6]Volume down 1')
    print('[7]System info\n[8]Keyboard Input (On-screen keyboard needs to be displayed)')
    choice = input('> ')
    menu.get(choice, unknown_command)()

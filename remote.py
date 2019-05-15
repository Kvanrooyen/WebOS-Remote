from wakeonlan import send_magic_packet
from pywebostv.discovery import discover
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl, InputControl, SourceControl

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
src_control = SourceControl(client)


def volume_set():
    print('\nWhat volume level do you want? [0-100]')
    volume_level = int(input('> '))
    media.set_volume(volume_level)


def volume_mute():
    print('\nWould you like to mute or unmute?')
    mute_val = input('> ')

    if mute_val == 'mute':
        media.mute(True)
    elif mute_val == 'unmute':
        media.mute(False)


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
    print('Product Name: ' + system_info['product_name'])
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


run_again = True

# Call this function after user makes a decision.
# This lets them run the program again if they want.


while run_again != False:
    # Ask the user what they would like to do after connecting
    print('\n\nWhat would you like to do? Choose only the number.\n')
    print('[0]Exit the program')
    print('[1]Set the volume level\n[2]Mute or unmute the volume\n[3]Turn off')
    print('[4]Current volume level\n[5]Volume up 1\n[6]Volume down 1')
    print('[7]System info\n[8]Keyboard Input (On-screen keyboard needs to be displayed)\n')
    choice = int(input('> '))

    if choice == 0:
        run_again = False
    elif choice == 1:
        volume_set()
    elif choice == 2:
        volume_mute()
    elif choice == 3:
        system.power_off()
    elif choice == 4:
        volume_info()
    elif choice == 5:
        up_volume_lvl()
    elif choice == 6:
        down_volume_lvl()
    elif choice == 7:
        sys_info()
    elif choice == 8:
        kb_input()

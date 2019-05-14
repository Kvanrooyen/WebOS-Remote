import sys
from pywebostv.discovery import discover
from pywebostv.connection import WebOSClient
from pywebostv.controls import MediaControl, SystemControl

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
    print('\nCurrent volume level is ' + volume['volume'])


def up_volume_lvl():
    media.volume_up()
    print('\nVolume increased by 1')


def down_volume_lvl():
    media.volume_down()
    print('\nVolume decreased by 1')


run_again = True

# Call this function after user makes a decision.
# This lets them run the program again if they want.


def rerun():
    print('\nWould you like to run the program again? [Y/N]')
    run_again_choice = input('> ')

    if run_again_choice == 'y':
        run_again = True
    elif run_again_choice == 'Y':
        run_again = True
    elif run_again_choice == 'n':
        sys.exit()
    elif run_again_choice == 'N':
        sys.exit()


while run_again != False:
    # Ask the user what they would like to do after connecting
    print('What would you like to adjust? Choose only the number.\n')
    print('[1]Set the volume level\n[2]Mute or unmute the volume\n[3]Turn off\n')
    print('[4]Current volume level\n[5]Volume up 1\n[6]Volume down 1\n')
    choice = int(input('> '))

    if choice == 1:
        volume_set()
        rerun()
    elif choice == 2:
        volume_mute()
        rerun()
    elif choice == 3:
        system.power_off()
        # After TV has turned off you can't reconnect. You need to create a Wake on LAN function, to connect again.
    elif choice == 4:
        volume_info()
        rerun()
    elif choice == 5:
        up_volume_lvl()
        rerun()
    elif choice == 6:
        down_volume_lvl()
        rerun()

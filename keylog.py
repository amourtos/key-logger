"""
Keylogger - A malicious program used for recording keystrokes
"""

__author__ = "Alex Mourtos"

import sys
import time
import signal
import os
import argparse
import logging
from datetime import datetime
# from pynput.keyboard import listener

# +++ Setting up logger +++
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('keylog.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()


# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')
# logger = logging.getLogger(__name__)
# stream_handler = logging.StreamHandler()


# +++ ------------------------------------------------------------------- +++
# functions to set banners and timers for uptime
def start_banner():
    file = __file__.split("/")[-1]
    start_time = datetime.now()
    start_banner = (
        "\n" +
        "-" * 80 +
        f"\n\tRunning {file}" +
        f"\n\tStarted on {start_time.isoformat()}\n" +
        "-" * 80
    )
    print(start_banner)
    logger.info(start_banner)
    return start_time


def end_banner(start_time):
    file = __file__.split("/")[-1]
    up_time = datetime.now() - start_time
    end_banner = (
        "\n" +
        "-" * 80 +
        f"\n\tStopping {file}" +
        f"\n\tUptime was {up_time}\n" +
        "-" * 80
    )
    print(end_banner)
    logger.info(end_banner)
    return

# +++ ------------------------------------------------------------------- +++


exit_flag = False


# def writefile(key):
#     key_data = str(key)
#     key_data = key_data.replace("'", "'")
#     with open("log.text", 'a') as f:
#         f.write(key_data)


def signal_handler(sig_num, frame):
    global exit_flag
    print('Received ' + signal.Signals(sig_num).name)
    if sig_num == 2:
        print("User is terminating program.")
        exit_flag = True
    if sig_num == 15:
        exit_flag = True
    if sig_num == 9:
        exit_flag = True


def main(args):
    print(f"my PID: {os.getpid()}")
    start = start_banner()
    # start_banner()
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while not exit_flag:
        time.sleep(1.0)
        try:
            print("main function running... log being created")
        except KeyboardInterrupt:
            print("user is killing program.")
        except Exception as e:
            logger.error(f"something went wrong: {e}")

    end_banner(start)
    return


if __name__ == '__main__':
    main(sys.argv[1:])

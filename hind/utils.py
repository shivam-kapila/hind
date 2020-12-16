import time


def safely_import_config():
    """
        Safely import config.py. If config.py is not found, wait 2 seconds and try again.
    """

    while True:
        try:
            from hind import config
            break
        except ImportError:
            print("Cannot import config.py. Waiting and retrying...")
            time.sleep(2)

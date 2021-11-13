from gitea_auto_update.update import updater
import fire
import sys


def main():
    """Main func"""
    if not sys.version_info[0] == 3:
        sys.exit("Sorry, Python 2 is not supported. Please update to Python 3.")
    fire.Fire(updater)


if __name__ == '__main__':
    main()
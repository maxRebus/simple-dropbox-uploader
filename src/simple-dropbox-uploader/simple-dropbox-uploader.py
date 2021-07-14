import argparse
import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

ENVVAR = 'SIMPLEDBUPLOAD_TOKEN'

def backup(filestream, dropbox_pathname):
    with filestream as f:
        try:
            dbx.files_upload(f.read(), dropbox_pathname, mode=WriteMode('add'))
        except ApiError as err:

            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Dropbox uploader')
    parser.add_argument('-n', '--dropboxpathname', help='Name to upload', required=True)
    parser.add_argument('-t', '--dropboxtoken', help='Token', required=False)
    args = vars(parser.parse_args())

    if 'dropboxtoken' in args:
        TOKEN = args['dropboxtoken']
    elif f'{ENVVAR}' in os.environ:
        TOKEN = os.environ[f'{ENVVAR}']
    else:
        sys.exit(f"ERROR: Cannot find token. You must set {ENVVAR} enviroment variable or pass -t TOKEN by command line.")

    with dropbox.Dropbox(TOKEN) as dbx:
        try:
            dbx.users_get_current_account()
        except AuthError:
            sys.exit("ERROR: Invalid access token; try re-generating an "
                "access token from the app console on the web.")

        backup(sys.stdin.buffer, args['dropboxpathname'])

        print("Done!")
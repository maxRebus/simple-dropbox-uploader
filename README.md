Simple Dropbox Uploader
===

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

20-rows dropbox uploader. Take from `stdin` and put to DropBox using API v2. 


> #### :warning: I write **Simple Dropbox Uploader** mainly for my purposes, having found nothing like it. Not tested. If you are looking for a better project try [Dropbox Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)


## Setup
```
export SIMPLEDBUPLOAD_TOKEN=YouDropboxSecretToken
```

## Examples

### Load text file
```
echo 'Ciao!' >> ciao.txt
cat ciao.txt | python3 app.py -n /ciao.txt
```

### Backup text file with datetime information
```
echo 'Ciao!' >> ciao.txt
cat ciao.txt | python3 app.py -n /ciao.backup.$(date +%F_%R)
```
Simple Dropbox Uploader
===

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

20-rows dropbox uploader. Take from `stdin` and put to DropBox using API v2. 


> #### :warning: I write **Simple Dropbox Uploader** mainly for my purposes, having found nothing like it. Not tested. If you are looking for a better project try [Dropbox Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)


## Install
```
docker pull massimorebuglio/simple-dropbox-uploader
export SDU_DROPBOX_TOKEN=YourSecretToken
```

## Examples

### Upload text file
```
echo 'Ciao!' >> ciao.txt
cat ciao.txt | sudo docker run massimorebuglio/simple-dropbox-uploader -n /ciao_on_dropbox.txt --dropboxtoken $SDU_DROPBOX_TOKEN
```

### Backup text file with datetime information
```
echo 'Ciao!' >> ciao.txt
cat ciao.txt | sudo docker run massimorebuglio/simple-dropbox-uploader -n /ciao.backup.$(date +%F_%R) --dropboxtoken $SDU_DROPBOX_TOKEN 
```

### Backup mongodb running in a docker container
```
sudo docker exec MONGO_CONTAINER_NAME sh -c 'mongodump --authenticationDatabase admin -u MONGO_USERNAME -p MONGO_PASSWORD --archive' | sudo docker run massimorebuglio/simple-dropbox-uploader -n /ciao.backup.$(date +%F_%R) --dropboxtoken $SDU_DROPBOX_TOKEN 
```










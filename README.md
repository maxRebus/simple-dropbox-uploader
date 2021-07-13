# Useless API

Dummy project to test CI/CD docker pipeline.

## Usage

* Edit `app.py` and push to main.
* Check pipeline: https://github.com/ai4muse/useless_api/actions

### Troubleshoot

#### Refresh dependency

Windows:
   ```
   pip list --format=freeze > requirements.txt
   wsl find requirements.txt -type f -exec sed -i 's/.post20210125/ /g' {} \;
   ```

Linux:
   ```
   pip list --format=freeze > requirements.txt
   find requirements.txt -type f -exec sed -i 's/.post20210125/ /g' {} \;
   ```
   
Note: `wsl find... / find...` tricky fix a bad self-generated dependency of _setuptools_. 
"# simple-dropbox-uploader" 

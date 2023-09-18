## Introduction

myapitest is a flask REST API that takes a given file path or directory as a GET requests and generates a JSON blob response listing the contents of a given path directory or file.

## Requirements
- Python3
- Flask
- pip
- Docker

See the requirements.txt file for more details on required python dependencies.

## Getting Started

myapitest when download has the following structure:

- tests/ - contains configuration and test scripts such as - - test_app.py which send a GET request to expected URL and port
- tet2/test.backup - containts a text file to read from to run a test and ensure API is running 
- requirements.txt - lists all the required pythong files 
- run_app.sh - is a bash script to run or execute the app locally 

Install or ensure you have python3-flask
download or clone the git repo 
execute the run bash shell script 

```
./run_app.sh
```

in another terminal you can execute:

```
curl http://localhost:5000/tests/test2/test.backup
```

This should return a json response containing the content message:
```
{"content":"hello it works"
```

You can also run it in a docker container by executing docker run 

## Testing 

There is a test_app.py script that can be used to test the app works, it checks for a specified expected JSON response. If received an OK the app should be running as expected.

## Security considerations

This app can be a security risk as it reads from a file system. A lot of security aspects should apply such as how to run it safely in a contained environment for testing purposes. Keep in mind that when running locally you are exposing your local file system to be read via GET requests.

# TO-DO

- The POST, PUT, DELETE commands are not validated at this time.  Best to create an authentication and authorization control in order to allow permissions to execute this HTTP methods.

- Consider environment hardening considerations during deployment 






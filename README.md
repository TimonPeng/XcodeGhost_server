# XcodeGhost_server

[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](https://github.com/Carthage/Carthage)


**XcodeGhost_server** is the server program of XcodeGhost.

You can use it to receive encrypted information and send some commands to the iPhone that vulnerable.

## Depends

* **web.py** `sudo pip install web.py`
* **pyDes**  `sudo pip install pyDes`

## Usage

### Start Server
```
sudo python server.py 80
```

**Windows** don't need `sudo`

### Domain Forward

You need forward `init.icloud-analysis.com` to your IP.
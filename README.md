This uses symlinks to gain read access to a website's files if the website does not check before extracting.
Based of the Whitehacks 2023 challenge Zippy

## How to use?

### Installation

```sh
git clone https://github.com/seanLimWeiRen/unzipVuln.git
cd unzipVuln
chmod +x unzipvuln.py
```

### Using the tool
```sh
./unzipvuln.py FILE_LOCATION
```

The tool will place the zip file in the current directory as `evil.zip`

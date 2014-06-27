# mkpasswd

Python script and module for generating random passwords. Based on the most
fundamental features from Don Libes' expect script. This script is compatible 
with both Python 2 ans Python 3.

# Usage

The simplest usage is just

    mkpasswd.py

but additional options are available via

    mkpasswd.py -h

You can also use the script as a Python module with

    ```python
    from mkpasswd import mkpasswd
    password = mkpasswd()
    ```
    

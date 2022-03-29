# reverse-shell

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Size](https://img.shields.io/github/repo-size/medpaf/reverse-shell)

This is a reverse shell written in Python used to to target a machine and gain remote shell access.

It consists of two distinct scripts:
- ***reverse-shell-server.py***: script with open listener port on which it receives the connection, by which command execution can be achieved.
- ***reverse-shell-client.py***: script in which the target machine (client) communicates back to the attacking machine (server).
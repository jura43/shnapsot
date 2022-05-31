# Shnapsot

##### Shnapsot is real-time chat application made in Flask with emphasis on secure exchange of messages

## Introduction

This project is part of Applied cryptography course. Goal of this project was to create end-to-end encryption and authentication of messages in real-time chat application.
Even though project didn't require me to create any sort of GUI I decided to make the app using python web framework Flask as I wanted to learn more about web development.

## About the chat
After creating account and logging in you will be redirected to index page(currently empty). To see online users go to the /online page. Upon loading of online users page javascript will generate Elliptic-curve Diffie-Hellman key pair using P-256 curve with Web Crypto API. After selecting user with which you want to chat it will export end send your public key to the other client. Other side will get exclamation mark next to your name which indicates that you selected him to chat with. After the other side selects your name script will generate derived key on his side and send his public key to you to generate derived key. Then you can start chatting. Derived key is generate using AES-GCM algorithm which offers encryption and message authentication by performing encrypt-then-MAC. Due lack of time there isn't any logic in case third person selects your name to chat with you. In that case chat with current user will not function anymore. For implementing key exchange and sending messages I use Socket.io.

## How to run it

To run it you have to have following:
- Python interpreter
- Python modules specified in requirements.txt
- MySQL database

To install required modules you can run following command after cloning the repo

     $ pip install -f requirements.txt
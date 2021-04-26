# QR Code Based Vending Machine

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This repository contains Backend, User WebApp, Admin Dashboard and Python Firmware for Raspberry Pi

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on you raspberry pi.

### Prerequisites

Turn on your Raspberry Pi, copy Firmware folder to the destkop of your Raspberry Pi and execute the following commands

```
- sudo apt update
- sudo apt upgrade

```

### Installing

Installing the Firmware to your Raspberry Pi

This assumes that you have already copied Firmware folder from this repository to the desktop of your Raspberry Pi
Open the terminal and execute the following commands

```
- cd ~/Desktop/Firmware
- python3 mainHandle.py
```


## Usage <a name = "usage"></a>

- Run the Raspberry Pi Firmware
- Scan the QRCode or open this link on your device
- http://vend-frontend.production.wrapdrive.tech/#/dashboard
- Click VEND button to vend the product

- For vend reports open the admin panel
- http://vend-admin.production.wrapdrive.tech/#/main

```
Default email address: admin@admin.com
Default password: admin
```

## WebApp Links

- Client App http://vend-frontend.production.wrapdrive.tech/#/dashboard
- Admin Dashboard http://vend-admin.production.wrapdrive.tech/#/

## Circuit Diagram
Servo is connected to GPIO3 of Raspberry Pi

![circuit diagram](Circuit_bb.png)

## QRCode

![circuit diagram](qrLarge.png)
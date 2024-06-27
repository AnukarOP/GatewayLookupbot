# - Gateway Lookup Bot 🚀

Welcome to the **Gateway Lookup Bot** repository! This bot provides users with detailed information about various websites, including payment gateway detection and site security features. It offers different functionalities and commands for users with varying access levels, such as free users, premium users, and VIPs.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The **Gateway Lookup Bot** leverages the [Telethon](https://github.com/LonamiWebs/Telethon) library to interact with the Telegram API and provide insightful details about websites, including detected payment gateways and security features like Captcha and Cloudflare protection.

## Features
- **Website Lookup:** Detects payment gateways and security features.
- **User Credit System:** Manages user credits for accessing bot functionalities.
- **Admin Commands:** Broadcast messages, approve users, and check registration stats.
- **VIP and Premium Plans:** Special commands and higher limits for VIP and Premium users.

## Installation
Follow these steps to set up the bot locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AnukarOP/GatewayLookupbot
    cd GatewayLookupbot
    ```

2. **Install dependencies:**
    ```bash
    pip install <LIB_HERE>
    ```

3. **Configure environment variables:**
    Edit the 'main.py` file in the root directory and add the necessary environment variables:
    ```main.py
    API_ID # Get this from my.telegram.org
    API_HASH # Get this from my.telegram.org
    BOT_TOKEN # Get this from @BotFather 
    ADMIN_ID # Admin Chatid Comma-separated admin IDs
    VIP_IDS # VIP Users Chatid Comma-separated VIP IDs
    ```

## Usage
To start the bot, run the following command:
```bash
python3 main.py
```

## Commands

### User Commands
- **`/start`**: Welcome message and registration prompt.
- **`/register`**: Register the user to start using the bot.
- **`/refresh`**: Refresh user credits.
- **`/info`**: Get user account details including plan and credits.
- **`/codes`**: Display generated codes (VIP only).
- **`/create <number>`**: Generate redeem codes (VIP only).
- **`/redeem <code>`**: Redeem a code for credits.
- **`/bh <site_url>`**: Perform a site lookup to detect payment gateways and security features.

### Admin Commands
- **`/broadcast <message>`**: Broadcast a message to all registered users.
- **`/approve <user_id>`**: Approve a user to the Premium plan.
- **`/stats`**: Display the number of registered users.

### VIP Commands
- **`/bh <site_url>`**: Access site lookup functionality without credit deduction.
- **`/create <number>`**: Generate multiple redeem codes.

## Contributing
We welcome contributions! Please follow these steps to contribute:

1. Fork the repository. 🌿
2. Star this Repository. ⭐
3. Follow me for more Open-source codes. ✅
4. Nothing... 😁

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


![](https://visitor-badge.laobi.icu/badge?page_id=AnukarOP.readme)
---

# Sex Positions Data & Automation

Welcome to the Sex Positions Data & Automation repository! This project encompasses several components to gather, manage, and disseminate information about sex positions. It includes a web scraper, an API for accessing position data, a JSON data exporter, and a Telegram bot for automated updates.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Components](#components)
  - [Web Scraper](#web-scraper)
  - [API](#api)
  - [JSON Data Exporter](#json-data-exporter)
  - [Telegram Bot](#telegram-bot)
- [Configuration](#configuration)
- [License](#license)
- [Contact](#contact)

## Features

- **Web Scraper:** Scrapes detailed information about sex positions from a specified website.
- **API:** Provides a RESTful interface to query data about sex positions.
- **JSON Data Exporter:** Dumps position data into a JSON file for offline use.
- **Telegram Bot:** Automatically posts updates about sex positions to a Telegram channel.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/TraxDinosaur/SexPositions/
cd SexPositions
pip install -r requirements.txt
```

## Components

### Web Scraper

The web scraper, implemented in `funcs.py`, retrieves detailed information about sex positions. It extracts:

- Position number
- Name
- Description
- Image URL
- Similar positions
- Safety tips

### API

The FastAPI application, defined in `api.py`, allows users to access position data through a RESTful interface:

- **Home Endpoint:** `GET /`
  - Returns a welcome message and instructions.
- **Positions Endpoint:** `GET /positions/{position}`
  - Retrieves data for a specific position based on the position number.

To run the API server, set `RUN_API` to `True` in `main.py` and execute:

```bash
python main.py
```

### JSON Data Exporter

The `jsonDump.py` script exports data about sex positions to a `positions.json` file. This is useful for offline data access or backups.

To dump the data, set `DUMP_TO_JSON` to `True` in `main.py` and run:

```bash
python main.py
```

### Telegram Bot

The Telegram bot, implemented in `tgBot.py`, posts position updates to a Telegram channel. To use it, configure `config.py` with your bot token and chat ID.

To start the bot, set `POST_TO_TG` to `True` in `main.py` and run:

```bash
python main.py
```

You can start posting by sending the `/photo` command to your bot in Telegram.

## Configuration

- **`config.py`**: This file contains configuration settings for the Telegram bot, including the bot token and chat ID.
- **`main.py`**: Manage which components to run by setting `RUN_API`, `DUMP_TO_JSON`, or `POST_TO_TG` to `True`.

## License

This project is licensed under the [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/). See the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub Profile:** [@TraxDinosaur](https://github.com/TraxDinosaur)
- **Contact Email:** [acciotraxdinosaur@duck.com](mailto:acciotraxdinosaur@duck.com)
- **Contact Site:** [traxdinosaur.github.io](https://traxdinosaur.github.io)

For any inquiries or contributions, feel free to reach out!

# NightBot Giveaway Assistant

NightBot Giveaway Assistant is a Python-based tool designed for live streamers to create interactive giveaway announcements and winner popups using the YouTube API and Chrome DevTools Protocol.

## Features

- **Interactive GUI:** User-friendly GUI for selecting winners.
- **Custom Winner Announcements:** Dynamically announce winners in the YouTube live chat.
- **Visual Popups:** Generate on-screen popups with custom animations to display winner details.
- **Configurable & Extendable:** Flexible configurations for authorization and UI customization.

---

## Requirements

- **Python:** Version 3.8 or later.
- **Dependencies:** Listed in `requirements.txt`.
- **Chrome DevTools:** Ensure Chrome DevTools is enabled and accessible.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DNSINED/NGW_Changer.git
   cd NGW_Changer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your credentials:
   ```env
   CHANNEL_ID=your_channel_id
   AUTH_TOKEN=your_auth_token
   WS_AUTH=your_ws_auth_token
   ```

4. Run the script:
   ```bash
   python nightbot_giveaway.py
   ```

---

## Usage

1. **Launch the GUI**: The application will start with a graphical interface.
2. **Enter Winner Name**: Input the name of the giveaway winner.
3. **Announce Winner**: Click "Execute" to:
   - Send a congratulatory message to the YouTube live chat.
   - Display a popup with winner details.

---

## Development Notes
**Files and Directories**

 - main.py: Entry point to the application.

 - gui.py: Handles GUI-related functionality.

 - nightbot_api.py: Manages API interactions.

 - popup.py: Generates and handles popup animations.

 - .env: Environment variable file for sensitive data.

 - requirements.txt: Python dependencies.

---

### Environment Variables
Replace hardcoded credentials with environment variables for enhanced security. Use the `.env` file as shown in the installation steps.

---

## Contribution

Contributions are welcome! Please open an issue or submit a pull request to improve this tool.

### To Do:
- Add more configurable options.
- Improve popup animations.
- Add multi-platform support.

---

## Disclaimer
This tool is for educational and research purposes only. Ensure compliance with YouTube’s API usage policies and terms of service.
This tool aims to demonstrate that there are certain vulnerabilities and that you should not take seriously everything you see on the internet, also the script is not fully usable, there is another fully functional version, do not avoid contacting me if you need it for education and research purposes.

---

## License
[MIT License](LICENSE)

---

## Acknowledgements
Special thanks to:
- [NightBot API](https://api.nightbot.tv/) for chat integration.
- The Python community for supporting open-source development.


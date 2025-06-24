# 🎙️ Rumble AI Assistant

**Rumble** is a voice-activated personal assistant built in Python. It simplifies everyday tasks through natural voice commands—integrating speech recognition, web browsing, news updates, music playback, and Google-powered search for a seamless, hands-free experience.

---

## 🚀 Features

- **Wake Word Activation**: Say `"rumble"` to activate the assistant.
- **Web Browsing**: Open any website with voice commands like `open youtube` or `open bbc.co.uk`.
- **News Updates**: Get the latest headlines using `news` or `tell me the news` (powered by NewsAPI).
- **Music Playback**:
  - Play predefined songs from a local music dictionary (`play sapphire`).
  - If not found, it searches and plays the first YouTube result.
- **Google Search**: Any unrecognized command triggers a Google Custom Search, and Rumble reads out the most relevant result.
- **Audio Feedback**: Rumble uses text-to-speech to reply to your commands vocally.

---

## 🛠️ Built With

- `speech_recognition` – Captures and processes voice input.
- `gTTS` / `pyttsx3` – Converts text responses to speech.
- `pygame` – Handles local music playback.
- `webbrowser` – Opens websites and YouTube links.
- `pytube` – Manages YouTube streaming.
- `requests` – Handles API calls (news, search, etc.).

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ManthanN75/Rumble.git
cd Rumble

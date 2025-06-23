# 🎙️ Rumble AI Assistant

**Rumble** is a voice-activated personal assistant built in Python. It simplifies everyday tasks through natural voice commands, integrating speech recognition, web browsing, news updates, music playback, and Google-powered search to deliver a seamless hands-free experience.


## 🚀 Features

* **Wake Word Activation**: Say **"rumble"** to activate the assistant.
* **Web Browsing**: Open any website with voice commands like `open youtube` or `open bbc.co.uk`.
* **News Updates**: Get the latest U.S. headlines using the command `news` or `tell me the news`, powered by NewsAPI.
* **Music Playback**:

  * Play predefined songs from a local music library (`play sapphire`).
  * If not found, searches and opens the first YouTube result.
* **Google Search**: Any other unrecognized command triggers a Google Custom Search, and the assistant reads out a relevant result.
* **Audio Feedback**: Rumble uses text-to-speech to respond vocally to all commands.


## 🛠️ Built With

* `speech_recognition` – For capturing and understanding voice input.
* `gTTS` / `pyttsx3` – Text-to-speech conversion for feedback.
* `pygame` – For audio handling of local music files.
* `webbrowser` – For opening websites and YouTube videos.
* `pytube` – For YouTube content handling.
* `requests` – For API communication (news and search).


## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd rumble-ai-assistant
   ```

2. **Install the required dependencies:**

   ```bash
   pip install speechrecognition gtts pygame pytube requests pyttsx3
   ```

3. **API Configuration:**

   * Open `main.py` and replace:

     * `google_api_key` with your **Google Custom Search API Key**
     * `google_cx` with your **Search Engine ID**
   * Replace `newsapi` with your valid **NewsAPI Key**.

4. **Music Library:**

   * Ensure `music_library.py` contains a dictionary of `{ "song name": "YouTube link" }`.

5. **Run the assistant:**

   ```bash
   python main.py
   ```



## 🎤 Usage

* Rumble automatically calibrates your microphone at startup.
* Say **"rumble"** to activate.
* Then issue commands like:

  * `open google`
  * `play sapphire`
  * `news`
  * `search how to cook pasta`

Rumble will speak back the results and open websites where necessary.



## ⚠️ Limitations

* Requires **active internet connection** for web, search, and playback features.
* YouTube video selection depends on Google Search result accuracy.
* No offline music playback (plays via YouTube in browser).



## 🤝 Contributing

Want to make Rumble smarter?

* Fork the repo
* Create a new branch
* Submit a PR with improvements

All contributions are welcome—whether it’s adding new commands, improving accuracy, or optimizing code performance!





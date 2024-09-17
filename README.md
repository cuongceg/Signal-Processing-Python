# Audio Processing

This program records audio from the microphone, saves the audio data to a WAV file, and plots the audio signal.

## Requirements

- Python 3.x
- `virtualenv` (if not installed, you can install it using `pip install virtualenv`)

## Setup

### Step 1: Create and activate a virtual environment

#### On Windows
~~~sh
python -m venv venv
.\venv\Scripts\activate
~~~


#### On macOS and Linux
~~~sh
python3 -m venv venv
source venv/bin/activate
~~~



### Step 2: Install the required libraries

~~~sh
pip install -r requirements.txt
~~~

## Running the Program

After installing the required libraries, you can run the program using the command:

~~~sh
python audio_processing.py
~~~


The program will record audio for 5 seconds, save the data to a file named `sample_python_audio.wav`, and plot the audio signal in a file named `sample-signal-wave.png`.

## Notes

- Ensure that your microphone is working and connected to your computer.
- If you encounter issues with `pyaudio`, try reinstalling it using `pip install pyaudio` or refer to the `pyaudio` documentation for more details.

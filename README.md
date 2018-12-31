# Keep Calm on wHAT

A simple script for generating "Keep Calm" messages on [Inky WHAT display](https://shop.pimoroni.com/products/inky-what).

![Keep calm and carry on](default.png?raw=true)

## Installation

### Install dependencies
Follow the instruction in [Getting Started with Inky wHAT](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-what) page
or simply install `einky` and `pil` python packages:
```bash
sudo pip install einky
sudo pip install pil
```

### Download this code
Just clone this repo:
```
git clone https://github.com/roblan/keep-calm.git
```

### Download font
Script uses font stored in `font.tff` file inside it's main folder.
To download [Keep Calm font from dafont.com](https://www.dafont.com/keep-calm.font) type in terminal
```bash
cd ./keep-calm
wget https://dl.dafont.com/dl/?f=keep_calm -O font.zip
unzip ./font.zip
mv ./KeepCalm-Medium.ttf ./font.ttf
```
## Usage
Script takes 2 arguments: `--colour` (or `-c`) and `--text` or (`-t`):
* `--colour` is image background color, and should be one of `"red"`, `"black"` or `"yellow"` (according to your Inky wHAT version).
* `--text` should be list of 5 lines to display. It's set to `"Keep" "calm" "and" "carry" "on"` by default.

### Example usage
```bash
python ./keep-calm.py --colour "red" --text "I can't keep calm" "and carry on" "  I'm a programmer  " "I get 21 errors" "in a 20 line program"
```

![I can't keep calm and carry on I'm a programmer I get 21 errors in a 20 line program](example.png?raw=true)

## Know issues
Sometimes (on smaller font sizes usually) text is cropped. To fix this you can simply add spaces to both sides of cropped line (like in the example above).

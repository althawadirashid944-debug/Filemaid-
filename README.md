# Filemaid🧹-
An event-driven linux utility daemon that automatically organises your Downloads folder into structured categories note: still WIP (work in progress) you will need to use a terminal command for it to work [IF YOU SEE ANY FOLDERS SUCH AS BUILD OR LIB IGNORE THEM JUST DOWNLOAD AND USE THE Filemaid folder] 
-
-
-
-

FileMaid is a lightweight Linux file organizer that automatically sorts your Downloads folder using real-time filesystem events.

It runs quietly in the background and moves files into categorized folders based on file type.

---

## Features

- Real-time file detection (event-based, not polling)
- Automatically sorts downloads into folders
- Lightweight and fast
- Works in background like a daemon [full background intergration is a work in progress right now you just need terminal to run it] 
- Uses `watchdog` for filesystem events

---

##  How it works

When a file is downloaded into your Downloads folder, FileMaid:

1. Detects the file creation event
2. Waits until download is fully finished
3. Checks file extension
4. Moves it into the correct folder:

- images/
- videos/
- audio/
- documents/
- archives/
- code/
- apps/
- other/

---

##   Installation

### 1. Install pipx (recommended)

```bash
sudo pacman -S python-pipx
```
### 2. Use gitclone or download folder from here
Via gitclone
you then cd filemaid
once inside filemaids folder run: pipx install .
(THE DOT IS VERY IMPORTANT) 
### Requirements
Python 3.10+
watchdog
### Notes
FileMaid is event-based (no heavy CPU usage)
It only runs when file events happen
Designed for Linux systems (Hyprland, KDE, etc.) 
Also like I said before needs the terminal (full background intergration is a work in progress bear with me here)
### FINAL THING IS DISCLAIMER : Modifies the position of files in your downloads to organised folders please use wisely . 

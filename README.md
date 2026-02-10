# XOLtab - System Info CLI

## Introduction
XOLtab is a python based system information display script meant for linux but can be run on Windows or Mac (NOTE: the bellow commands are meant for linux based systems and may need to be changed depending on your OS). XOLtab is designed to be lightweight and snappy and is inspired by neofetch (RIP).

---

## Features

- Display OS-specific ASCII art
- Show detailed system info: CPU, GPU, Memory, Disk, Battery, Uptime, and more
- Colorful, bold output for readability
- Easy to install and run

---

## Installation

### Prerequisites

- Python 3.x installed
- Git installed

### Steps

1. Clone the repository:

```bash
https://github.com/AEROmicro/XOLtab
```

2. Navigate into the directory:

```bash
cd xoltab
```

3. Make the script executable:

```bash
chmod +x xoltab.py
```

4. Run the script directly:

```bash
./xoltab.py
```

### Optional: Make it globally accessible

To run `xoltab` from anywhere, you can:

- Move the script to a directory in your PATH, e.g., `~/.local/bin/`.
- Or, create an alias in your shell config.

Example:

```bash
mv xoltab.py ~/.local/bin/xoltab
chmod +x ~/.local/bin/xoltab
```

Now, you can run:

```bash
xoltab
```

### Install as an executable:
```bash
nano ~/.bashrc
```
or:
```bash
nano ~/.zshrc
```
and add something like this:
```bash
XOLtab(){
  sudo python3 /home/(yourusername)/Downloads/XOLtab.py
}
```
and then save:
```bash
source ~/.bashrc
```
or:
```bash
source ~/.zshrc
```
or wherever your script is installed
NOTE: you need sudo privleges if you want the device model to show

---

## Usage

Just run:

```bash
./xoltab.py
```

or, if you installed it globally:

```bash
xoltab
```

---

## License

This project is open-source. licened under GNU GPLv3
All spins of this project must retain this licence or legal action can pursue

---

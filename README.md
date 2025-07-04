# ZoolooS' Config Exporter for Space Engineers aka zce-se

## General info and Why

In-game ability to manage some world settings are very short, so I created a few tools for myself and decided to share it with anyone who may need it.<br>
Each world you play in Space Engineers has two files (`Sandbox_config.sbc`, `Sandbox.sbc`) with most of settings. This files actually just XML-files. They are lays in save-game folder. Path (on Windows) usually something like that:<br>
`c:\Users\<username>\AppData\Roaming\SpaceEngineers\Saves\<long_ID>\<save_name>\`<br>
You can change some settings through in-game UI, but manually you have some more variations.<br>
All mods info which you apply on world stored here too.

## zce-se can do

- Export modlist from Mods part SE sbc-files (`Sandbox_config.sbc`, `Sandbox.sbc`).
- For now that's all %).

## Prerequisites

- Installed `Python`. I think with 3.10+ all will work correct.
- Installed `lxml`:
  - https://github.com/lxml/lxml
  - https://pypi.org/project/lxml/
  - https://lxml.de/
- Project was build with `uv`, so you can use it too to make your live little bit easier.
  - https://docs.astral.sh/uv/

## How to use

Copy `Sandbox_config.sbc` or/and `Sandbox.sbc` files to `_in` folder (by default) near this script.<br>
Run script (main.py). Like `uv run main.py` or `python main.py` or whatever.<br>
Script will generate modlists (`Sandbox_config_out.txt` or/and `Sandbox_out.txt` files) in format (by default):

```txt
-:|: FriendlyName1 :|: ModId1
-:|: FriendlyName2 :|: ModId2
...
```

You can change some settings in `settings.py` file.

---
- Copyright © 2025 Ilya Popov aka ZoolooS. All rights reserved.
- Author: Ilya Popov aka ZoolooS
- Description: This file is the part of "ZoolooS' Config Exporter for Space Engineers" application
---

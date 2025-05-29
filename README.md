# ZoolooS' Config Exporter for Space Engineers aka zce-se

## zce-se can do

- Export modlist from Mods part SE sbc-files (`Sandbox_config.sbc`, `Sandbox.sbc`).
- For now that's all %).

## Prerequisites

- Installed `Python`. I think with 3.10+ all will work correct.
- Installed `lxml`.
- Project was build with `uv`, so you can use it too to make your live little bit easier.

## How to use

Copy `Sandbox_config.sbc` or/and `Sandbox.sbc` files to `_in` folder (by default) near this script.
Run script (main.py). Like `uv run main.py` or `python main.py` or whatever.
Script will generate modlists (`Sandbox_config_out.txt` or/and `Sandbox_out.txt` files) in format:

```txt
-:|: FriendlyName1 :|: ModId1
-:|: FriendlyName2 :|: ModId2
...
```

You can change some settings in settings.py file.

---
- Copyright © 2025 Ilya Popov aka ZoolooS. All rights reserved.
- Author: Ilya Popov aka ZoolooS
- Description: This file is the part of "ZoolooS' Config Exporter for Space Engineers" application
---

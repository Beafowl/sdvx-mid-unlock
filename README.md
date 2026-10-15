# SDVX song ID limit

spice2x patches for SOUND VOLTEX (`soundvoltex.dll`) that raise the music ID limit from **3072**, so
custom songs can use IDs above 3071. Without them, a `music_db.xml` with an ID of 3072 or more crashes
the game during boot. Patches here are meant to be used with [spice2x](https://spice2x.github.io/)
via the `Patches` menu.

### URL: `https://beafowl.github.io/sdvx-mid-unlock`

**Back up your original `soundvoltex.dll` and your save data before patching.** Use at your own
risk, see the [disclaimer](#disclaimer).

## Usage

<details>
<summary style="font-size: 16px">Method #1: Import from URL (easiest)</summary>

> *If the import does not work, update spice2x to the latest stable release from https://spice2x.github.io/.*

- Open `spicecfg.exe` (or run `spice64 --cfg`) and go to the `Patches` tab
- Click `Import from URL`, enter `https://beafowl.github.io/sdvx-mid-unlock` and click `Import`
- As long as your game version is [supported](SUPPORTED.md), the patches below show up in the list.
  Hover over a patch to see what it does
- Use the **unmodified** `soundvoltex.dll`: spice2x applies the patches in memory and checks the original bytes

spice2x keeps one imported list per game version, so importing this URL replaces patches imported
from another site for the same version.
</details>

<details>
<summary style="font-size: 16px">Method #2: Reading from JSON</summary>

- Open [SUPPORTED.md](SUPPORTED.md) and make sure your game version is supported
- Click the *Identifier* link for your version, then click *Download raw file* in the top right
- Create a folder named `patches` next to `spicecfg.exe` if there is none, and put the JSON file in it
- Open `spicecfg.exe` and go to the `Patches` tab
</details>

## Patches

### Song ID limit

Raises the limit to 65535, so music IDs `1 .. 65534` are usable. Keep ID 9001 free (the tutorial
uses it). The game's score tables grow with the limit and use about 360 MB of memory instead of
about 17 MB.

### Custom Songs folder

Gives all songs that carry `<tag id="100"/>` in `music_db.xml` a top-level folder **Custom Songs**
in the song select, with the sub-folders **ALL** and **LEVEL 1** to **LEVEL 20**, and hides them
from every other folder, including ALL and the stock level, grade and medal folders. The folder
takes the place of the contest category, whose contest folders are no longer listed. Add the tag
inside each custom song's `<music>` entry, e.g. after `</difficulty>`:

```xml
    </difficulty>
    <tag id="100"/>
  </music>
```

Selecting a custom song in the subscreen music search opens Custom Songs > ALL and jumps to it.
The patch also hides the folder the server adds for its current event, and makes the song select
reopen the folder you were in instead of the folder "recommended for beginners".

## Troubleshooting / FAQ

### "Import failed" when importing from URL

An import failed error with code 404 means your game version is not supported here. Check
[SUPPORTED.md](SUPPORTED.md).

### My game crashes when starting

Check that your `soundvoltex.dll` is unmodified (or restore it from your backup) and that no song in
`music_db.xml` uses an ID above 65534.

### Reporting problems

Please open an issue with your game version (`KFC-...` identifier), the patches you enabled and what
went wrong.

## Disclaimer

This is an unofficial, community-made tool, not affiliated with or endorsed by Konami. It modifies
game files and is provided "as is", without warranty of any kind. You use it entirely at your own
risk. The author is not liable for any loss or damage resulting from its use, including corrupted
game files, lost scores, play records, profiles or other save data (locally or on a server), and
crashes or other problems with the game or your system.

**Always keep backups** of `soundvoltex.dll`, your `data` folder and your server's save data before
patching.

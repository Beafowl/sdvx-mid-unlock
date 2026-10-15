# SDVX song ID limit

Every song in SOUND VOLTEX has a music ID. If a song has an ID over 3071, the game crashes while booting.

This repo provides spice2x patches that raise the music ID limit from 3072 to 65535 (basically unlimited).

### URL: `https://beafowl.github.io/sdvx-mid-unlock`

## Usage

<details>
<summary style="font-size: 16px">Method #1: Import from URL (easiest)</summary>

> _If the import does not work, update spice2x to the latest stable release from https://spice2x.github.io/._

- Open `spicecfg.exe` (or run `spice64 --cfg`) and go to the `Patches` tab
- Click `Import from URL`, enter `https://beafowl.github.io/sdvx-mid-unlock` and click `Import`
- As long as your game version is [supported](SUPPORTED.md), the patches below show up in the list.
  Hover over a patch to see what it does

</details>

<details>
<summary style="font-size: 16px">Method #2: Reading from JSON</summary>

- Open [SUPPORTED.md](SUPPORTED.md) and make sure your game version is supported
- Click the _Identifier_ link for your version, then click _Download raw file_ in the top right
- Create a folder named `patches` next to `spicecfg.exe` if there is none, and put the JSON file in it
- Open `spicecfg.exe` and go to the `Patches` tab
</details>

## Patches

### Increase song ID limit

As mentioned above, raises the limit to 65535, so music IDs `1 .. 65534` are usable.

### Custom Songs folder

The difficulty of custom songs can be quite far from what the game would suggest at a certain level, which
makes the level folders inaccurate when custom songs are included.

For that reason, a patch is included that moves all custom songs to a **Custom Songs** folder. They will be
removed from all other folders.

The folder will replace the Contest folder. Only songs that have an <tag id="100"/> in the music DB file will be moved.
The folder is further categorized into **ALL** and **LEVEL 1** to **LEVEL 20** folders.

To set all songs to a specified ID, use https://github.com/Beafowl/VoxCharger.

## Credits

The layout of this repository follows [sp2xpatcher](https://github.com/eamuse/sp2xpatcher).

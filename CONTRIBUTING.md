# Contributing

## Bug reports

Open an issue with the game version (`KFC-...` identifier), the patches you enabled, and what went
wrong (attach `log.txt` if the game crashed).

## Changes to the patch files

1. Fork the repository and make your changes.
2. Run `python checks.py` and fix anything it reports.
3. Submit a pull request.

Once a pull request is merged, the patches are available within minutes at
`https://beafowl.github.io/sdvx-mid-unlock`.

### JSON naming

Each game version has its own JSON file in `patches/`, named after its
[PE identifier](https://github.com/spice2x/spice2x.github.io/wiki/patches.json-specification#pe-identifier)
so that spice2x's *Import from URL* finds it. When adding a game version, also add it to
[SUPPORTED.md](SUPPORTED.md) in the existing format; `checks.py` fails otherwise.

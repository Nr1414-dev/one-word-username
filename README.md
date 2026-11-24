# One Word, One Username, One Reward

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Nr1414-dev/one-word-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Nr1414-dev/one-word-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the [make.fun](https://make.fun) bounty
["One Word, One Username, One Reward"](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

## The username

> rapid-orca-37

Our own make.fun handle, one word, 13 characters — inside the
30-character cap. A speedy orca: fast, memorable, and a handle its
owner happily wears.

## Run

```sh
python3 main.py
```

Writes the username to `/output/entry.txt` (UTF-8, no trailing newline,
13 characters). The program validates the text is 1–30 Unicode code
points and a single word before writing. Set `ENTRY_OUTPUT_DIR` to
write elsewhere.

## Verification

Deterministic output: running `main.py` twice to different directories
produces byte-identical `entry.txt` files (same SHA-256). The committed
`entry.txt` matches that hash as well.

## License

MIT — see [LICENSE](LICENSE).

# ZapFast, patched

[ZapFast](https://github.com/crmne/zapfast) for Windows x64 with a few patches on top. This isn't a separate app: every new ZapFast release is picked up, patched and published here automatically, so you get all of upstream's updates. Differences from upstream:

- **Read ticks always show**, even with your account's read receipts off.
- **Deleted messages stay.** Messages others delete for everyone are kept and marked *deleted*.
- **Screen privacy.** Covers chats, messages, media, names and avatars until hovered (Ctrl+Shift+H, off by default). By [paulo1403](https://github.com/paulo1403) ([crmne/zapfast#451](https://github.com/crmne/zapfast/pull/451)), via [ZapFaster](https://github.com/eternalwaitt/zap-faster).
- **Updates come from this repository**, so they keep these changes.

<p align="center">
  <img src="docs/ticks.png" width="49%" alt="Read ticks turn blue even with read receipts off">
  <img src="docs/deleted.png" width="49%" alt="A message deleted for everyone stays, marked deleted">
</p>
<p align="center">
  <img src="docs/privacy.png" width="49%" alt="Screen privacy covers the chat list until you hover a row">
  <img src="docs/updates.png" width="49%" alt="Each upstream release is patched and offered as an update">
</p>

Everything else is upstream ZapFast. The changes are in [`patches/`](patches).

**[Download the latest release](https://github.com/Goodly58/zapfast/releases/latest)** (`.msi`)

Unofficial build, not affiliated with ZapFast, WhatsApp or Meta. ZapFast © Carmine Paolino and contributors, [MIT](LICENSE).

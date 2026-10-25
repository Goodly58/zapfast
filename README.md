# ZapFast, patched

Windows builds of [ZapFast](https://github.com/crmne/zapfast) with one change:
**read ticks show even when your WhatsApp account has read receipts off.**

ZapFast 0.20.0 started greying out other people's read ticks in direct chats
whenever your account's read receipts are off
([crmne/zapfast#458](https://github.com/crmne/zapfast/pull/458)), to match the
phone. WhatsApp still delivers those receipts and ZapFast still stores them;
the change is display only. This build shows them again.

Turn off **Settings > Privacy > Send read receipts** in ZapFast as well, so
reading a chat here sends no blue ticks of your own.

## What is patched

| Patch | Change |
|---|---|
| [`0001-show-read-ticks.patch`](patches/0001-show-read-ticks.patch) | `display_delivery` returns the stored status unchanged |
| [`0002-update-from-this-fork.patch`](patches/0002-update-from-this-fork.patch) | The built-in updater checks this repository and trusts only [this repository's key](update-public-key.hex) |

Without the second patch, ZapFast's updater would install the next upstream
release and drop the first.

## How updates work

[`build.yml`](.github/workflows/build.yml) runs every six hours. When
upstream publishes a release this repository has not built, it checks out that
tag, applies `patches/`, builds the Windows x64 packages the way upstream's
release workflow does, signs the update manifest and publishes a release with
the same tag. ZapFast then offers it in the app as usual.

If upstream changes the patched code, `git apply` fails, GitHub emails the
failure, and the installed copy stays on the last patched version until the
patch is refreshed. To build a particular tag, run the workflow by hand with
that tag.

The private signing key is the `ZAPFAST_UPDATE_SIGNING_KEY` secret. An
optional `ZAPFAST_GIPHY_KEY` secret fills the GIF picker's key.

## Licence

ZapFast is © Carmine Paolino and contributors under the [MIT licence](LICENSE).
This is an unofficial build, not affiliated with ZapFast, WhatsApp or Meta.

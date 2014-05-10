<p style='text-colr:red'>This is OBSOLETE, switch to https://github.com/ywrac/btsync-api-python</p>

# python-btsync

BTSync APIをPythonから利用することができます。
APIを利用するためにはBitTorrent社からAPI Keyを取得する必要があります。

The `BTSync` class is a light wrapper around the [Bittorrent Sync API][1].
For now, this code assumes a btsync instance is running with a working API key.
(See the **Notes** section for more info on how to get this set up.)

[1]: http://www.bittorrent.com/sync/developers/api

## インストール　Installation
```bash
$ git clone https://github.com/jminardi/python-btsync.git
$ cd python-btsync
$ python setup.py install
```
*最新版の[BitTorrent Sync][0]が必要です。*
*You will also need a recent version of the [Bittorrent Sync Application][0]*
[0]: http://www.bittorrent.com/sync/downloads


## 使い方　Basic Use

```python
>>> # this code assumes a btsync instance is running
>>> from btsync import BTSync
>>> btsync = BTSync()
>>> btsync.get_folders()
[{u'dir': u'/Users/jack/sync/notes',
  u'error': 0,
  u'files': 13,
  u'indexing': 0,
  u'secret': u'NOPE',
  u'size': 70867,
  u'type': u'read_write'}]
```

## メソッド　Implemented Methods
すべてのメソッドが実装されているわけだはありません。
しかし`request()`メソッドを介して任意のメソッドを実行することができます。

At this time, not all API calls are implemented. However, you can still
make any API call manually using the `request()` method like so:

```python
btsync.request({'method': 'get_folder_peers', 'secret': '<yoursecret>'})
```

### 実装済みのメソッド一覧
* [x] Get folders
* [x] Add folder
* [x] Remove folder
* [x] Get files
* [x] Set file preferences
* [ ] Get folder peers
* [x] Get secrets
* [ ] Get folder preferences
* [ ] Set folder preferences
* [ ] Get folder hosts
* [ ] Set folder hosts
* [ ] Get preferences
* [ ] Set preferences
* [x] Get OS name
* [x] Get version
* [x] Get speed
* [x] Shutdown


## Notes

残念ながらBTSyncはプロプライエタリなソフトウェアです。
そのためAPIを利用するためには、BitTorrent社の許可を必要とします。
具体的にはAPIキーというものを以下のURLから取得する必要があります。

To use the API you will need to apply for a key. You can find out
how to do that, and learn more about the btsync API here:

<http://www.bittorrent.com/sync/developers/>

APIキーを取得したら、設定ファイルにキーを入力してください。

Once you receive your key, you need to enter it into the config file.
See `config.json` for a sample config file.

--configフラグをつけてBTSyncのバイナリを実行すればAPIが有効になります。

Then quit BTSync if it is running, and start it from the command line with the --config flag:

Macの実行例を以下に示します。

```bash
$ /Applications/BitTorrent\ Sync.app/Contents/MacOS/BitTorrent\ Sync --config path/to/config.json
```

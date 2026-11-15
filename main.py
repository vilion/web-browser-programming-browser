class URL:
    # コンストラクタ: URL文字列を受け取り、オブジェクトを初期化します
    def __init__(self, url):
        # スキームと残りのURLを分割します
        self.scheme, url = url.split("://", l)
        # スキームがhttpであることを確認します
        assert self.scheme == "http"
        if "/" not in url:
            url = url + "/"
        # ホストと残りのURL（パス）を分割します
        self.host, url = url.split("/", 1)
        # パスを '/' から始まるように設定します
        self.path = "/" + url

    # Webページをリクエストするメソッド
    def request(self):
        # ...

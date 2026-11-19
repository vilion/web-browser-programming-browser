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
        s = socket.socket(
                family=socket.AF_INET,
                type=socket.SOCK_STREAM,
                proto=socket.IPPROTO_TCP,
            )
        s.connect((self.host, 80))
        request = "GET {} HTTP/1.0\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "\r\n"
        s.send(request.encode("utf8"))
        response = s.makefile("r", encoding="utf8", newline="\r\n")

        statusline = response.readline()

        version, status, explanation = statusline.split(" ", 2)
        

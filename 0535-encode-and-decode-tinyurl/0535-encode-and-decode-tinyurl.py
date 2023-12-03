class Codec:
    def __init__(self):
        self.map = {}
        self.count = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.map[self.count + 1] = longUrl
        return self.count + 1

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
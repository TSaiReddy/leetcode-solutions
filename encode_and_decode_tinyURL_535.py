import random
import string


class Codec:
    def __init__(self) -> None:
        self.hash = {
            "jRDx": "https://leetcode.com/problems/design-tinyurl"
        }

    def generate_str(self):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(4))

    def encode(self, longUrl: str) -> str:
        tiny_url = self.generate_str()
        self.hash[tiny_url] = longUrl
        return f'http://tinyurl.com/{tiny_url}'

    def decode(self, shortUrl: str) -> str:
        hashed_key = shortUrl.split("/")[-1]
        return self.hash[hashed_key]


codec = Codec()
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode("http://tinyurl.com/jRDx"))

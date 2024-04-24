from urllib.parse import urlparse, urljoin


def is_relative_url(url):
    parsed_url = urlparse(url)
    return not all([parsed_url.scheme, parsed_url.netloc])


class LogoFinder:
    def __init__(self, url, soup_object):
        self.soup_object = soup_object
        self.url = url

    def search_for_logos(self):
        logos = []
        for img in self.soup_object.find_all("img"):
            if (
                "logo" in img.get("src", "").lower()
                or "logo" in img.get("alt", "").lower()
            ):
                if is_relative_url(img["src"]):
                    absolute_logo_url = urljoin(self.url, img["src"])
                    logos.append(absolute_logo_url)
                else:
                    logos.append(img["src"])
        return logos

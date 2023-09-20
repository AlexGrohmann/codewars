def domain_name(url):
    url = url.replace("https://", '')
    url = url.replace("http://", '')
    url = url.replace("www.", '')
    return url.split('.')[0]


print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
print(domain_name("https://www.xk5o4w4kf.it/warez/"), "xk5o4w4kf")
print(domain_name("4k6kf5np6ms.jp/"), "4k6kf5np6ms")

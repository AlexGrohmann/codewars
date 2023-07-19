function domainName(url) {
  let start = 0;
  if (url.indexOf("www.") != -1) {
    start = url.indexOf("www.") + 4;
  } else if (url.indexOf("//") != -1) {
    start = url.indexOf("//") + 2;
  }
  let endString = url.slice(start, url.length);
  return endString.slice(0, endString.indexOf("."));
}

console.log(domainName("http://google.com"), "google");
console.log(domainName("http://google.co.jp"), "google");
console.log(domainName("www.xakep.ru"), "xakep");
console.log(domainName("https://youtube.com"), "youtube"); //https://www.xk5o4w4kf.it/warez/
console.log(domainName("https://www.xk5o4w4kf.it/warez/"), "xk5o4w4kf");
console.log(domainName("4k6kf5np6ms.jp/"), "4k6kf5np6ms");

//   url = url.replace("https://", '');
//   url = url.replace("http://", '');
//   url = url.replace("www.", '');
//   return url.split('.')[0];

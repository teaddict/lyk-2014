# coding:utf_8
_author__ = 'schwappkopf'



#
def parse_url(url):
    url = str(url)
    my_url={"protokol": url.split("/")[0].strip(":"),
            "uzanti":   url.split("/")[2].split(".")[2],
            "alanadi":  url.split("/")[2],
            "yol":      url.split("/")[3].split(".")[0]+"."+url.split("/")[3].split(".")[1] }

    print my_url



def parse(url):
    parts=url.split("/")
    protokol=parts[0].strip(":")
    alanadi=parts[2]
    uzanti=alanadi.split(".")[-1] # -1 sondan birinci ifadeyi verir
    yol="/" + parts[-1]

    return dict(protokol = protokol, alanadi=alanadi,uzanti=uzanti,yol=yol)



url ="http://kamp.linux.org/index.html"
parse_url(url)
print parse(url)
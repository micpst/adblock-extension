import urllib.request

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt"
    
    with open("blocked-urls.js", "w") as f: 
        f.write("const blockedUrls = [")
        
        with urllib.request.urlopen(url) as res:
            data = res.read()
            data = data.decode("utf-8").split("\n")
            
            for line in data:
                if "127.0.0.1 " in line:
                    line = line.lstrip("127.0.0.1 ").rstrip("]\n")
                    f.write(f"\"*://*.{line}/*\",")

        f.write("];")

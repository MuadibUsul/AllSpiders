import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3"
}
movieid = 52782267
localid = 268
while True:
    url = "https://pp.ziyuan605.com/20181228/9ae3948V/800kb/hls/MhcxV"+str(movieid)+".ts"
    x = requests.get(url, headers=headers)
    if x.status_code == 200:
        moviename = "ts/"+str(localid)+".ts"
        print(moviename)
        with open(moviename, 'wb') as f:
            f.writelines(x)
            print("download "+moviename+" success!")
        localid += 1
    else:
        print("下载完毕")
        break
    movieid += 1
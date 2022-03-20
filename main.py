try:
    import requests
    import youtube_dl
except:
    print('Thư viện `requests` hoặc `youtube_dl` chưa được cài đặt!')
try:
    content_choose = """|---------------------
| 1. Tải file
| 2. Tải video youtube
|---------------------"""
    print(content_choose)
    choose = int(input('> '))
    if choose == 1:
        link = input('Đường dẫn file cần tải:\n> ') # Ví dụ: https://youtube.com
        name_file = input('Tên file cần tải:\n> ')
        end_file = input('Đuôi file cần tải(ví dụ: py, json, html, png, svg, js, ts,....)\n> ')
        get = requests.get(link)
        with open(f'{name_file}.{end_file}','wb') as f:
            f.write(get.content)
    elif choose == 2:
        url = input('Đường dẫn video:\n> ') # Ví dụ: https://youtube.com/watch?v=codevideo
        with youtube_dl.YoutubeDL() as yt:
            list_video = []
            list_video.append(url)
            yt.download(url_list=list_video)
    elif choose < 1:
        pass
    elif choose > 2:
        pass
except:
    print('Lỗi!')
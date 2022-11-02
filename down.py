import requests
from bs4 import BeautifulSoup
import yt_dlp
import server
def list(user , pas ,url, fpath, s):
    login_url = "https://els-engmet.com/login/"
    payload = {
"log" : user,
"pwd" : pas,
"wp-submit" : "دخول",
"redirect_to": "https://els-engmet.com/"
}
    headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"}
    f1 = open(fpath,"w")
    log_in = s.post(login_url , data = payload , headers=headers )
    server.url(url , s)
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text , "html.parser").find_all("div" , {"class" : "tutor-course-lesson"} )
    for i in soup:
     x =BeautifulSoup(str(i) , "html.parser").find("a")
     print(i.text)
     lec = s.get(x["href"] , headers = headers)
     z= BeautifulSoup(lec.text , "html.parser").find("iframe",{"allow" : "autoplay"})["src"]
     print ('video ',  z ,'\n')
     f1.write(i.text + "\n "+ z+"\n ===========\n\n")
     list.append(z)
    return list


def format_selector(ctx):
  
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }

def down(fpath , url , list):
    ydl_opts = {
    'format': format_selector,
    'outtmpl': fpath+"/"+str(url[31:-1]+'/%(title)s.%(ext)s')
}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
     ydl.download(list)
from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup
def checkmet(user , pas , s):
    login_url = "https://els-engmet.com/login/"
    payload = {
"log" : user,
"pwd" : pas,
"wp-submit" : "دخول",
"redirect_to": "https://els-engmet.com/"
}
    headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"}

    log_in = s.post(login_url , data = payload , headers=headers )
    r = s.get("https://els-engmet.com/dashboard/", headers=headers)
    if r.url =="https://els-engmet.com/dashboard/":
     return "true"
    else:
     return " false"
def url(url, s):
    tex = s.get(url).text
    soup = BeautifulSoup( tex , "html.parser")
    check =soup.find("button" ,{ "type":"submit" , "class":"tutor-btn-enroll tutor-btn tutor-course-purchase-btn"  })
    print(check)
    if str(check) == "None":
        print("enrolled")
        return
    if input("you aren't inrolled into the course inroll?? y/n: ") == "y":
        nonce = soup.find("input" , {"name" :"_tutor_nonce" })["value"]
        ref = soup.find("input" , {"name" :"_wp_http_referer" })["value"]
        id = soup.find("input" , {"name" :"tutor_course_id" })["value"]
        print(nonce , ref , id)
        payload = {
"_tutor_nonce" : nonce,
"_wp_http_referer" : ref,
"tutor_course_id" : id,
"tutor_course_action" : "_tutor_course_enroll_now"
}
        s.post(url , data = payload )
        print("you have been enrolled")

import requests
from bs4 import BeautifulSoup

def get_from_cache(url, file_name):
    try:
        html = open(file_name, 'r').read()
    except:
        response = requests.get(url)
        html = response.text
        # same as doing: html = requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text

        f = open(file_name, 'w')
        f.write(html)
        f.close()

    return html

html = get_from_cache("http://www.nytimes.com/pages/todayspaper/index.html", 'nyt_frontpage.html')
soup = BeautifulSoup(html, 'html.parser')
front_page_section = soup.find("div", {"class": "aColumn"})
# print(front_page_section)
list_of_stories = front_page_section.find_all("div", {"class": "story"})
# print(list_of_stories)

stories = []
for story in list_of_stories:
    # extract values
    # - Title
    # - Author(s)
    # - Summary
    # - Thumbnail
    title = story.find("h3").text.strip()
    # print(repr(title))

    authors = story.find("h6").text.strip()
    # print(authors)

    summary = story.find("p", {"class": "summary"}).text.strip()
    # print(summary)

    thumbnail_soup = story.find('img')
    # try:
    #     thumbnail = thumbnail_soup.get('src')
    # except AttributeError:
    #     thumbnail = None

    if thumbnail_soup:
        thumbnail = thumbnail_soup.get('src')
    else:
        thumbnail = None
    # print(story.find('img'))
    # thumbnail = story.find('img')['src']

    # print(story)
    # print('-'*10)

    url = story.find('h3').find('a')['href']
    print(url)

    article_html = get_from_cache(url, title.split()[0] + '.html')
    print(article_html)

    story_dict = {
        "title": title,
        "authors": authors,
        "thumbnail": thumbnail,
        "summary": summary,
        "url": url
        "article_html": article_html
    }

    stories.append(story_dict)






# for story in stories:
#     print(story)
#     print('-'*10)

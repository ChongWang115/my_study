import  requests
import re
from lxml import etree


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def get_rank(html):
    partten = re.compile('<dd>.*?board-index .*?>(\d+)</i>',re.S)
    rank_list = re.findall(partten,html)
    print (rank_list)
    return rank_list

def get_film_name(html):
    return html.xpath('//dd//div//@title')

def get_film_actor(html):
    return html.xpath('//dl//*[@class="star"]/text()')

def get_film_releasetime(html):
    return html.xpath('//dl//*[@class="releasetime"]/text()')

def get_film_score_inter(html):
    return html.xpath('//dl//*[@class="integer"]/text()')

def get_film_score_fra(html):
    return  html.xpath('//dl//*[@class="fraction"]/text()')

def main(offset):
    url=f'https://maoyan.com/board/4?offset={offset}'
    html = get_one_page(url)
    film_rank_list = get_rank(html)

    html = etree.HTML(html)
    film_name_list = get_film_name(html)
    film_actor_list = get_film_actor(html)
    film_releasetime_list = get_film_releasetime(html)
    film_score_inter_list = get_film_score_inter(html)
    film_score_fra_list = get_film_score_fra(html)
    write_text=''
    print(film_name_list)
    for i in range(len(film_name_list)):
        rank = film_rank_list[i]
        name = film_name_list[i]
        actor = film_actor_list[i].strip()
        score = film_score_inter_list[i]+film_score_fra_list[i]
        releasetime = film_releasetime_list[i]
        write_text = f"{rank},{name},{actor},{score},{releasetime}"
        print(write_text)

        with open('manyan_rank.txt','a',encoding='utf-8') as fp:
            fp.write(write_text+'\n')

if __name__ == '__main__':
    for i in range(0,100,10):
        print (i)
        main(i)

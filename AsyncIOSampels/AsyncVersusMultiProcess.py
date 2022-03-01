import requests
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
import time
import aiohttp
from aiohttp import ClientSession
import asyncio

def get_html_by_movie_id(movie_id):
    url = f"https://www.imdb.com/title/{movie_id}/fullcredits"
    response = requests.get(url)
    return response.text

async def get_html_by_movie_id_new(movie_id, session):
    print(f"Processing movie {movie_id}")
    url = f"https://www.imdb.com/title/{movie_id}/fullcredits"
    response = await session.request(method="GET", url=url)
    html = await response.text()
    print(f"Done Processing movie {movie_id}")

    return html


async def scrape_all_titles(movies_list):
    async with ClientSession() as session:
        tasks = []
        for movie_id in movies_list:
            tasks.append(get_html_by_movie_id_new(movie_id, session))
        result = await asyncio.gather(*tasks)
    return result


def multi_process_main(movies_list:list):
    s = time.perf_counter()
    result = Parallel(n_jobs=8)(delayed(get_html_by_movie_id)(movie_id) for movie_id in movies_list)
    elapsed = time.perf_counter() - s
    print(f"Multi process Executed in {elapsed:0.2f} seconds.")

async def aio_main(movies_list:list):
    # aio
    s = time.perf_counter()

    result = await asyncio.gather(scrape_all_titles(movies_list))
    elapsed = time.perf_counter() - s
    print(f"AIO Executed in {elapsed:0.2f} seconds.")

if __name__ == "__main__":
    movies_list = ['tt2935510','tt7131622','tt5463162','tt4758646','tt3640424','tt6024606','tt1596363','tt3707106','tt2713180','tt2193215','tt2024544','tt0816711','tt1764234','tt1402488','tt1210166','tt0478304','tt1001526','tt0361748','tt0421715','tt0887883','tt0443680','tt0496806','tt0449467','tt0356910','tt0349903','tt0332452','tt0165982','tt0270288','tt0240772','tt0266987','tt0236493','tt0208092','tt0137523','tt0120601','tt0119643','tt0120102','tt0118972','tt0117665','tt0114746','tt0114369','tt0110322','tt0110148','tt0109783','tt0108399','tt0107302','tt0105265','tt0104009','tt0104567','tt0103074','tt0101268','tt0097478','tt0097136','tt0118930','tt0093407','tt0093638','tt0093640','tt0093231']


    #multi process
    multi_process_main(movies_list)
    #AIO
    #you could do this in windows for higher python versions
    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #result = asyncio.run(scrape_all_titles(movies_list))
    loop=asyncio.get_event_loop()
    loop.run_until_complete(aio_main(movies_list=movies_list))

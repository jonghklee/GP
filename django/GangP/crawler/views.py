from django.shortcuts import render
import requests as req
from bs4 import BeautifulSoup as bs


def crawler(request):
    web_cpu = req.get('https://www.cpubenchmark.net/high_end_cpus.html')
    
    html = web_cpu.text

    soup = bs(html, 'html.parser')
    
    cpu_name = soup.select(
    '#mark > div > div.chart_body > ul > li > a > .prdname'
    )
    cpu_name = list(map(lambda cpustr : str(cpustr)[22:-7], cpu_name))

    cpu_mark = soup.select(
    '#mark > div > div.chart_body > ul > li > a > .count'
    )
    cpu_mark = list(map(lambda cpustr : str(cpustr)[20:-7], cpu_mark))

    if len(cpu_mark) == len(cpu_name):
        num = len(cpu_name)
    else:
        raise Exception()

    return render(request, 'crawler.html', {'cpu_name' : cpu_name, 'cpu_mark' : cpu_mark, 'numlist' : range(num)})
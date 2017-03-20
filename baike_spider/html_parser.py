# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import re


class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):  #获取soup对象中的URL节点

        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/.*'))
        for link in links:
            new_url = link['href']  # 获得节点的href属性
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 该方法自动拼接URL
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

        res_data = {}
        res_data['url'] = page_url

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):   # 解析下载后的网页
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)  # 获取解析到的所有URL
        new_data = self._get_new_data(page_url, soup)   # 获取解析到的所有URL
        return new_urls, new_data



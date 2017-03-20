# -- coding:utf-8 --
from baike_spider import html_parser, html_downloader
from baike_spider import url_manager, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # URL下载器
        self.parser = html_parser.HtmlParser()              # URL解析器
        self.outputer = html_outputer.HtmlOutputer()        # 输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  # 添加爬虫入口URL到URL管理器
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()   # 获取一个URL管理器中的URL
                print('craw %d: %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  # 下载该URL
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析该URL，得到新的URL和数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 5:
                    break
                count += 1
            except:
                print('craw false!!!')

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/android/60243'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

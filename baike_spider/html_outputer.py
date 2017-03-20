# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html>')
        # fout.write('<head><meta charset="utf-8"></head>')
        fout.write("<head>")
        fout.write("<meta charset=\'utf-8\'>")
        fout.write("</head>")
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
    #
    # def output_html(self):
    #     fileout = open("output.html", "w", encoding='utf-8')
    #     fileout.write("<html>")
    #     fileout.write("<head>")
    #     fileout.write("<meta charset=\'utf-8\'>")
    #     fileout.write("</head>")
    #     fileout.write("<body>")
    #     fileout.write("<table>")
    #     for data in self.datas:
    #         fileout.write("<tr>")
    #         fileout.write("<td>%s</td>" % data['url'])
    #         fileout.write("<td>%s</td>" % data['title'])
    #         fileout.write("<td>%s</td>" % data['summary'])
    #         fileout.write("</tr>")
    #     fileout.write("</table>")
    #     fileout.write("</body>")
    #     fileout.write("</html>")
    #     fileout.close()

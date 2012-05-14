# -*- coding : utf-8 -*-

from django import template
from django.template import Context

class PageDigg:
    pages = []

    def __init__(self, page, segment):
        border = 3
        num_pages = page.paginator.num_pages
        segment = int(segment)

        pages = []

        if num_pages <= (segment * 2) + 1:
            pages = range(1, num_pages + 1, 1)
        else:

            if page.number - segment <= border:
                part1 = range(1, page.number, 1)
            else:
                part1 = [1, 2, 0] + range(page.number - segment, page.number , 1)

            if page.number + segment >= num_pages - border:
                part2 = range(page.number, num_pages + 1, 1)
            else:
                part2 = range(page.number, page.number + segment + 1, 1) + [0, num_pages - 1, num_pages]
                
            pages = part1 + part2
            
        self.pages = pages
        
    def get_pages(self):
        return self.pages

class PaginationNode(template.Node):

    def __init__(self, page_obj, url, segment):
        self.page_obj = page_obj
        self.url = url
        self.segment = segment

    def render(self, context):
        page_obj = template.Variable(self.page_obj).resolve(context)
        url = template.Variable(self.url).resolve(context)
        segment = template.Variable(self.segment).resolve(context)
        
        t = template.loader.get_template('store/paginator-tag.html')

        obj = PageDigg(page_obj, segment)
        pages = obj.get_pages()

        data = {
            'pages': pages,
            'page_obj': page_obj,
            'url': url
        }
        return t.render(Context(data))
        

def pagination_ctl(parser, token):
    tokens = token.contents.split()
    # template, paginatorObj, url, segment
    return PaginationNode(tokens[1], tokens[2], tokens[3])
    

register = template.Library()
register.tag('pagination_ctl', pagination_ctl)

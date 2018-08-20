# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Date    : 2014-11-29 19:09:59
# # @Author  : Linsir (vi5i0n@hotmail.com)
# # @Link    : http://linsir.org
# import json
# import time

# import qrcode
# import requests
# import top
# import top.api
# from PIL import Image, ImageEnhance, ImageDraw, ImageFont
# from bs4 import BeautifulSoup
# from django.conf import settings

# from config.settings.setup import MEDIA_ROOT
# from restful.models.goods import QueryRule

# APPKEY = settings.TOP_APPKEY
# SECRET = settings.TOP_SECRET


# # QUERYS = QueryRule.objects.last()
# # GOODS_COLUMN = [field.column for field in Goods._meta.fields]
# # RULES_COLUMN = [field.column for field in QueryRule._meta.fields]


# def text2img(text, font_color="White", font_size=28):
#     """生成内容为 TEXT 的水印"""

#     font = ImageFont.truetype(MEDIA_ROOT + '/fonts/yahei.ttf', font_size)
#     text = text.split('\n')

#     mark_width = 0

#     for i in range(len(text)):
#         (width, height) = font.getsize(text[i])
#         if mark_width < width:
#             mark_width = width

#     mark_height = height * len(text)

#     # 生成水印图片
#     mark = Image.new('RGBA', (mark_width, mark_height))
#     draw = ImageDraw.ImageDraw(mark, "RGBA")
#     draw.setfont(font)

#     for i in range(len(text)):
#         (width, height) = font.getsize(text[i])
#         draw.text((0, i * height), text[i], fill=font_color)

#     return mark


# def set_opacity(im, opacity):
#     assert opacity >= 0 and opacity < 1

#     if im.mode != "RGBA":
#         im = im.convert('RGBA')
#     else:
#         im = im.copy()

#     alpha = im.split()[3]
#     alpha = ImageEnhance.Brightness(alpha).enhance(opacity)

#     im.putalpha(alpha)

#     return im


# def watermark(im, mark, position, opacity=1):
#     try:
#         if opacity < 1:
#             mark = set_opacity(mark, opacity)

#         if im.mode != 'RGBA':
#             im = im.convert('RGBA')

#         if im.size[0] < mark.size[0] or im.size[1] < mark.size[1]:
#             print "The mark image size is larger size than original image file."
#             return False

#         # 设置水印位置
#         if position == 'left_top':
#             x = 0
#             y = 0
#         elif position == 'left_bottom':
#             x = 0
#             y = im.size[1] - mark.size[1]
#         elif position == 'right_top':
#             x = im.size[0] - mark.size[0]
#             y = 0
#         elif position == 'right_bottom':
#             x = im.size[0] - mark.size[0]
#             y = im.size[1] - mark.size[1]
#         elif position == 'center':
#             x = (im.size[0] - mark.size[0]) / 2
#             y = (im.size[1] - mark.size[1]) / 2
#         else:
#             x = (im.size[0] - mark.size[0]) / 2 if position[0] == 'center' else position[0]
#             y = (im.size[1] - mark.size[1]) / 2 if position[1] == 'center' else position[1]

#         layer = Image.new('RGBA', im.size)
#         layer.paste(mark, (x, y))

#         return Image.composite(layer, im, layer)
#     except Exception as e:
#         print ">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e)
#         return False


# def createQRCode(data, size=11):
#     qr = qrcode.QRCode(version=1, box_size=size, border=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
#     qr.add_data(data)
#     qr.make(fit=True)
#     im = qr.make_image()

#     return im


# def top_items(keyword, page_size=50, sleep=1):
#     QUERYS = QueryRule.objects.last()
#     RULES_COLUMN = [field.column for field in QueryRule._meta.fields]

#     req = top.api.AtbItemsGetRequest()
#     req.set_app_info(top.appinfo(APPKEY, SECRET))

#     if QUERYS:
#         for field in RULES_COLUMN:
#             if hasattr(QUERYS, field) and field != 'id':
#                 value = QUERYS.__getattribute__(field)
#                 if value:
#                     setattr(req, field, value)

#     req.keyword = keyword
#     req.page_size = page_size
#     req.fields = "open_iid,title,nick,pic_url,price,commission,commission_rate," \
#                  "commission_num,commission_volume,seller_credit_score,item_location,volume,promotion_price,shop_type"

#     time.sleep(sleep)

#     try:
#         item = {}
#         resp = req.getResponse()
#         rows = resp.get('atb_items_get_response').get('items').get('aitaobao_item')

#         for x in rows:
#             item[x.get('open_iid')] = x
#             item[x.get('open_iid')]['cid'] = ''
#             item[x.get('open_iid')]['desc'] = ''
#             item[x.get('open_iid')]['item_img'] = ''

#         return item

#     except Exception, e:
#         print e.message
#         return None


# def top_detail(iids):
#     req = top.api.AtbItemsDetailGetRequest()
#     req.set_app_info(top.appinfo(APPKEY, SECRET))
#     req.fields = "open_iid,cid,title,desc,item_img,pic_url,promotion_price,price,delist_time,shop_type"
#     req.open_iids = ",".join(iids)

#     try:
#         resp = req.getResponse()
#         rows = resp.get('atb_items_detail_get_response').get('atb_item_details').get('aitaobao_item_detail')
#         items = []
#     except Exception, e:
#         print e.args, e.message, resp, iids
#         return None

#     for x in rows:
#         try:
#             item = x.get('item')

#             if item.get('item_imgs'):
#                 item['item_img'] = item.get('item_imgs').get('item_img', None)
#                 item['item_img'] = json.dumps(item.get('item_img'))
#             else:
#                 print item.get('item_imgs')

#             if item.get('open_iid', None) is None:
#                 raw_input(item.get('open_iid'))

#             if item.get('desc', None) is None:
#                 raw_input(item.get('desc'))

#             if item.get('item_img', None) is None:
#                 raw_input(item.get('item_img'))

#             items.append(item)
#         except Exception, e:
#             print e.args, e.message
#             continue

#     return items


# def compile_html(html):
#     soup = BeautifulSoup(html, 'html5lib')
#     soup.head.append(soup.new_tag("meta", charset="utf-8"))
#     meta = soup.new_tag("meta", content="width=device-width,initial-scale=1")
#     meta.attrs['name'] = 'viewport'
#     soup.head.append(meta)

#     for img in soup.find_all('img'):
#         src = img.get('src')

#         if src:
#             if '.jpg' in img.get('src'):
#                 img['class'] = 'lazy img-responsive'
#                 img['data-original'] = img['src']
#                 img['src'] = img['src'].replace('.jpg', '.jpg_' + settings.THUMB_LIST + '.jpg')

#     soup.body.append(soup.new_tag("script", src="/static/frontend/js/lazyload.js"))
#     # lazy = soup.new_tag("script", type="text/javascript")
#     # lazy.string = '$(function() {$("img.lazy").lazyload()});'
#     # soup.body.append(lazy)
#     # open('desc.html', 'w').write(soup.prettify('utf-8'))
#     return soup.prettify('utf-8')


# def get_trend():
#     url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT' \
#           '&cmd=0000011,3990012,3990052,3990062,hsi5,djia7&sty=MPNSBAS&st=&sr=1' \
#           '&p=1&ps=1000&token=44c9d251add88e27b65ed86506f6e5da' \
#           '&cb=callback08571712439879775&callback=callback08571712439879775&_=1457324522778'

#     req = requests.get(url)
#     txt = req.text.replace('callback08571712439879775', '').strip('(').strip(')')
#     ret = json.loads(txt)
#     ret = ret[0].split(',')[3].replace('.', '')[-3:]

#     return ret


# if __name__ == '__main__':
#     text = u'我是你的朋友, 我邀请你加入够惊喜'
#     qr = createQRCode(data=text, size=11)
#     im = Image.open('thumb_IMG_0215_1024.jpg')

#     mark = text2img(text)
#     image = watermark(im, qr, ('center', 527))
#     image = watermark(image, mark, ('center', 427))

#     if image:
#         # image.save('watermark.png')
#         image.show()
#     else:
#         print "Sorry, Failed."
from rest_framework import mixins, status
from rest_framework.response import Response


class MyDestroyModelMixin(mixins.DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': '删除成功'}, status=status.HTTP_204_NO_CONTENT)

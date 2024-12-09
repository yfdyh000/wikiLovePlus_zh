import urllib.parse

# 定义HTML内容
html_content = """
</th></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E5%8C%97%E4%BA%AC%E7%83%A4%E9%B8%AD" title="Template:北京烤鸭">北京烤鸭</a>|留言}}
</td>
<td>== 北京烤鸭送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Roasted_Beijing_Duck_sliced.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/75/Roasted_Beijing_Duck_sliced.jpg/200px-Roasted_Beijing_Duck_sliced.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/75/Roasted_Beijing_Duck_sliced.jpg/300px-Roasted_Beijing_Duck_sliced.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/75/Roasted_Beijing_Duck_sliced.jpg/400px-Roasted_Beijing_Duck_sliced.jpg 2x" data-file-width="4032" data-file-height="3024"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td><span style="background:#ffffdd" title="本句仅作幽默目的，请勿当真。"><b>此菜品可能会导致感染<a href="/wiki/Wikipedia:%E9%A4%B5%E9%9B%9E%E7%97%85%E6%AF%92" title="Wikipedia:喂鸡病毒">喂鸡病毒</a>，请慎重食用。</b></span><sup><a href="/wiki/Wikipedia:%E5%9D%8F%E7%AC%91%E8%AF%9D%E5%92%8C%E5%88%A0%E9%99%A4%E7%9A%84%E8%83%A1%E8%AF%9D" title="Wikipedia:坏笑话和删除的胡话">[开玩笑的]</a></sup>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E7%82%B8%E9%85%B1%E9%9D%A2" title="Template:炸酱面">炸酱面</a>|留言}}
</td>
<td>== 请您吃老北京炸酱面！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Taste_of_Beijing,_Soho,_London_(4363231155).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg/200px-Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg/300px-Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg/400px-Taste_of_Beijing%2C_Soho%2C_London_%284363231155%29.jpg 2x" data-file-width="2808" data-file-height="1872"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E7%85%8E%E9%A5%BC%E6%9E%9C%E5%AD%90" title="Template:煎饼果子">煎饼果子</a>|留言}}
</td>
<td>== 煎饼果子送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Jianbing_being_prepared.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jianbing_being_prepared.jpg/200px-Jianbing_being_prepared.jpg" decoding="async" width="200" height="312" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jianbing_being_prepared.jpg/300px-Jianbing_being_prepared.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jianbing_being_prepared.jpg/400px-Jianbing_being_prepared.jpg 2x" data-file-width="656" data-file-height="1024"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E7%82%92%E6%A0%97%E5%AD%90" title="Template:炒栗子">炒栗子</a>|留言}}
</td>
<td>== 炒栗子送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Roastedchestnut.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Roastedchestnut.jpg/200px-Roastedchestnut.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Roastedchestnut.jpg/300px-Roastedchestnut.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Roastedchestnut.jpg/400px-Roastedchestnut.jpg 2x" data-file-width="2048" data-file-height="1536"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E9%A9%B4%E8%82%89%E7%81%AB%E7%83%A7" title="Template:驴肉火烧">驴肉火烧</a>|留言}}
</td>
<td>== 驴肉火烧送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Donkey_sandwich,_Baoding_style_(20160310111719).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg/200px-Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg/300px-Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg/400px-Donkey_sandwich%2C_Baoding_style_%2820160310111719%29.jpg 2x" data-file-width="3264" data-file-height="2448"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E5%9B%9B%E5%96%9C%E4%B8%B8%E5%AD%90" title="Template:四喜丸子">四喜丸子</a>|留言}}
</td>
<td>== 四喜丸子送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Sixi_Balls.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Sixi_Balls.png/200px-Sixi_Balls.png" decoding="async" width="200" height="222" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Sixi_Balls.png/300px-Sixi_Balls.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Sixi_Balls.png/400px-Sixi_Balls.png 2x" data-file-width="3062" data-file-height="3401"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E5%BE%B7%E5%B7%9E%E6%89%92%E9%B8%A1" title="Template:德州扒鸡">德州扒鸡</a>|留言}}
</td>
<td>== 送您一只德州扒鸡！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Single_Dezhou_braised_chicken_wrapped_in_paper_(20170115132902).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/78/Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg/200px-Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg" decoding="async" width="200" height="140" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/78/Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg/300px-Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/78/Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg/400px-Single_Dezhou_braised_chicken_wrapped_in_paper_%2820170115132902%29.jpg 2x" data-file-width="3264" data-file-height="2278"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E8%91%B1%E7%87%92%E6%B5%B7%E5%8F%83" title="Template:葱烧海参">葱烧海参</a>|留言}}
</td>
<td>== 葱烧海参送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg/200px-Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg/300px-Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg/400px-Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg 2x" data-file-width="4032" data-file-height="3024"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E4%B9%9D%E8%BD%89%E5%A4%A7%E8%85%B8" title="Template:九转大肠">九转大肠</a>|留言}}
</td>
<td>== 九转大肠送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:Jiuqu_dachang_2009_03.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Jiuqu_dachang_2009_03.jpg/200px-Jiuqu_dachang_2009_03.jpg" decoding="async" width="200" height="111" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Jiuqu_dachang_2009_03.jpg/300px-Jiuqu_dachang_2009_03.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Jiuqu_dachang_2009_03.jpg/400px-Jiuqu_dachang_2009_03.jpg 2x" data-file-width="2510" data-file-height="1388"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E6%8B%94%E7%B5%B2%E5%9C%B0%E7%93%9C" title="Template:拔丝地瓜">拔丝地瓜</a>|留言}}
</td>
<td>== 拔丝地瓜送给您！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg/200px-%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg/300px-%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg/400px-%E6%8B%94%E4%B8%9D%E5%9C%B0%E7%93%9C.jpg 2x" data-file-width="4032" data-file-height="3016"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr>
<tr>
<td>{{<a href="/wiki/Help:%E6%9B%BF%E6%8D%A2%E5%BC%95%E7%94%A8" title="Help:替换引用">subst</a>:<a href="/wiki/Template:%E9%9F%AD%E8%8F%9C%E7%9B%92%E5%AD%90" title="Template:韭菜盒子">韭菜盒子</a>|留言}}
</td>
<td>== 送您一盘韭菜盒子！ ==
<table style="background-color: #fdffe7; border: 1px solid #fceb92;">
<tbody><tr>
<td style="vertical-align: middle; padding: 5px;"><span typeof="mw:File"><a href="/wiki/File:%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg/200px-%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg" decoding="async" width="200" height="267" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg/300px-%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8c/%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg/400px-%E9%9F%AD%E8%8F%9C%E7%9B%92.jpg 2x" data-file-width="2448" data-file-height="3264"/></a></span>
</td>
<td style="vertical-align: middle; padding: 3px;">留言--~~~~
</td></tr></tbody></table>
</td>
<td>
</td></tr></tbody></table>
"""

# 定义要提取的信息的正则表达式
import re

# 提取模板名称
template_name_pattern = r'title="Template:(.*?)">'
template_names = re.findall(template_name_pattern, html_content)

# 提取文件名
file_name_pattern = r'/wiki/File:(.*?)"'
file_names = re.findall(file_name_pattern, html_content)

# 提取内容
content_pattern = r'== (.*?) =='
contents = re.findall(content_pattern, html_content)

# 将提取的信息保存到CSV文件
import csv

if len(template_names) == len(file_names) == len(contents):
    pass  # 如果相等，什么都不做
else:
    print("数量不相等")
    exit(1)

with open('extracted_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(["Template Name", "File Name", "Content"])
    for i in range(len(template_names)):
        csvwriter.writerow([template_names[i], urllib.parse.unquote(file_names[i]), contents[i]])

print("信息已成功提取并保存到extracted_info.csv文件中。")

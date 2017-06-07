#!/usr/bin/python

# NB! Do not forget to copy all the neccessary images!

import sys,requests,json;


HTML_START = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="github-markdown.css">
    <style>
      .markdown-body {{
        box-sizing: border-box;
        min-width: 200px;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
      }}
    </style>
    <title>{title}</title>
  </head>
  <body>
    <article class="markdown-body">
"""

HTML_END = """    </article>
  </body>
</html>
"""


# Function that converts input MD file to output HTML file.
def md2html(htmltitle, infile, outfile):
    inf = open(infile, 'r')
    payload = {'text': inf.read(), 'mode': 'markdown'}
    result = requests.post('https://api.github.com/markdown', data=json.dumps(payload))
    inf.close()

    html = result.text.encode('utf-8')
    html = html.replace("user-content-", "")
    outf = open(outfile, 'w')
    outf.write(HTML_START.format(title=htmltitle))
    outf.write(html)
    outf.write(HTML_END)
    outf.close()    


md2html("X-Road: Security Server Installation Guide", "md/ig-ss_x-road_v6_security_server_installation_guide.md", "docs/ig-ss_x-road_v6_security_server_installation_guide.html")
md2html("X-Road: Protocol for Downloading Configuration", "md/pr-gconf_x-road_protocol_for_downloading_configuration.md", "docs/pr-gconf_x-road_protocol_for_downloading_configuration.html")
md2html("X-Road: Message Protocol v4.0", "md/pr-mess_x-road_message_protocol.md", "docs/pr-mess_x-road_message_protocol.html")
# Not converted yet in that version
#md2html("X-Road: Security Server User Guide", "md/ug-ss_x-road_6_security_server_user_guide.md", "docs/ug-ss_x-road_6_security_server_user_guide.html")
md2html("X-Road: System Parameters User Guide", "md/ug-syspar_x-road_v6_system_parameters.md", "docs/ug-syspar_x-road_v6_system_parameters.html")

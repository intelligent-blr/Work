import re

# text = '''
# <div class="vector-body-before-content">
#     <div class="mw-indicators">
#         <div id="mw-indicator-good-star" class="mw-indicator"><div class="mw-parser-output"><span typeof="mw:File"><a href="/wiki/Wikipedia:Good_articles*" title="This is a good article. Click here for more information."><img alt="This is a good article. Click here for more information." src="//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png" decoding="async" width="19" height="20" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/29px-Symbol_support_vote.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/39px-Symbol_support_vote.svg.png 2x" data-file-width="180" data-file-height="185"></a></span></div></div>
#     </div>
#     <div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>
# </div>
# '''

text = '''
<div class="card-body m-0 p-0 pt-3">
  <a href="/python-guitar-synthesizer/">
    <h2 class="card-title h2 my-0 py-0">Build a Guitar Synthesizer: Play Musical Tablature in Python</h2>
  </a>
  <p class="my-1">In this tutorial, you'll build a guitar synthesizer using the Karplus-Strong algorithm in Python. You'll model vibrating strings, simulate strumming techniques, read musical notation and tablature, and apply audio effects. By the end, you'll have created a digital guitar that can play any song.</p>
  <p class="card-text">
    <small class="text-muted">
      <span class="mr-2">Jun 19, 2024</span>
      <span class="icon baseline ml-2" aria-hidden="true"><svg aria-hidden="true"><use href="/static/icons.acb887171118.svg#@category"></use></svg></span>
      <a href="/tutorials/intermediate/" class="badge badge-light text-muted">intermediate</a>
      <a href="/tutorials/projects/" class="badge badge-light text-muted">projects</a>
    </small>
  </p>
</div>
'''


def remove_html_tags(html_text):
    plain_text = re.sub(r'<[^>]+>', '', html_text)
    return plain_text.strip()


clear_text = remove_html_tags(text)
print(clear_text)

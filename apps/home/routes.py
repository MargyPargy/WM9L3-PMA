from apps.home import blueprint
from flask import render_template
from jinja2 import TemplateNotFound

@blueprint.route('/index')
def index():
  return render_template('home/index.html')

@blueprint.route('/<template>')
def route_template(template):
  try:
    if not template.endswith('.html'):
      template += '.html'

    return render_template('home/'+template)
  
  except TemplateNotFound:
    return render_template('home/page-404.html'), 404
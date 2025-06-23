from odoo.http import route, request
from odoo import http, fields
from odoo.addons.website_blog.controllers.main import WebsiteBlog
import random
class Home(http.Controller):
  @route('/api/testimonials', type='json', auth='public', methods=['POST'], website=True)
  def get_testimonials(self, **kwargs):
      current_website = http.request.website
      domain = [('website_id', '=', current_website.id)]
      testimonials = http.request.env['testimonials.model'].sudo().search(domain)
      data = testimonials.read(['job_title', 'img_url', 'display_name', 'description'])
      return data
  
  @route('/api/faqs', type='json', auth='public', methods=['POST'], website=True)
  def get_faqs(self, **kwargs):
      current_website = http.request.website
      domain = [('website_id', '=', current_website.id)]
      faqs = http.request.env['website.faqs'].sudo().search(domain)
      data = faqs.read([])
      return data
  
  @route('/api/blog/latest-posts', type='json', auth='public', methods=['POST'], website=True)
  def get_latest_blog_posts(self, **kwargs):
      latest_posts = http.request.env['blog.post'].sudo().search(
          [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())],
          order="post_date desc",
          limit=4
      )
      data = latest_posts.read(['name', 'post_date', 'visits', 'blog_id', 'website_url', 'teaser', 'cover_properties', 'author_name'])
      print("latest posts", data)
      return data
  
class CustomWebsiteBlog(WebsiteBlog):
    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False,
                             page=False, search=None, **post):
        values = super()._prepare_blog_values(blogs, blog, date_begin, date_end, tags, state, page, search, **post)
        top_posts = request.env['blog.post'].sudo().search(
            [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())], 
            order="visits desc", limit=5)
        values['top_posts'] = top_posts
        return values

    @http.route([
        '''/blog/<model("blog.blog"):blog>/<model("blog.post", "[('blog_id','=',blog.id)]"):blog_post>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog_post(self, blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        """ Extend the original method to include top_posts """
        res = super(CustomWebsiteBlog, self).blog_post(blog, blog_post, tag_id=None, page=1, enable_editor=None, **post)
        BlogPost = request.env['blog.post']
        alternative_posts = BlogPost.search([
            ("website_published", "=", True),
            ("post_date", "<=", fields.Datetime.now()),
            ('id', '!=', blog_post.id)
        ])
        if len(alternative_posts) > 4:
            alternative_posts = random.sample(alternative_posts, 4)

        res.qcontext.update({
            'alternative_posts': alternative_posts,
        })
        return res

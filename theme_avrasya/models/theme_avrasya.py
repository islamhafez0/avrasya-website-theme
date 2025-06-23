from odoo import models


class ThemeEdama(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_edama_post_copy(self, mod):
        self.enable_view('website.template_header_sales_two')
        self.enable_view('website_blog.opt_blog_post_sidebar')
        self.enable_view('website_blog.opt_blog_post_sidebar')
        self.disable_view('website_blog.opt_blog_post_read_next')
        self.disable_view('website_blog.opt_blog_post_archive_display')
        self.disable_view('website_blog.opt_blog_post_author_avatar_display')
        self.disable_view('website_blog.opt_blog_post_blogs_display')
        self.disable_view('website_blog.opt_blog_post_tags_display')
        self.disable_view('portal.user_sign_in')
        self.enable_view('website.header_social_links')
        self.disable_view('website.header_text_element')
        self.enable_view('website_blog.opt_blog_post_sidebar')

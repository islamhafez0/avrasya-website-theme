{
    'name': 'Theme Avrasya',
    'description': 'Through our innovative solutions and extensive network, we provide unlimited opportunities to grow your business globally and help you achieve sustainability and enhance efficiency in your projects in an integrated manner. ',
    'summary': 'Where Global Trade Becomes More Successful!',
    'author': 'Islam Hafez',
    'contributors': [
        "<Ahmed Lakosha> <<ahmed.lakosha94@gmail.com>>",
    ],
    'category': 'Theme',
    'version': '17.0.0.4',
    'depends': ['social_media', 'mass_mailing', 'crm', 'web', 'website',
                'multiple_websites_models', 'website_blog', 'base'],
    'license': 'OPL-1',
    'company': 'Pearl Pixels',
    'images': [
        'static/description/avrasya_description.png',
        'static/description/avrasya_screenshot.png',
    ],
    'data': [
        # Inheritance 
        'views/custom_header.xml',
        'views/custom_footer.xml',
        'views/custom_blog.xml',
        'views/single.xml',

        # Templates 
        'views/templates/contact_form.xml',
        'views/templates/newsletter_form.xml',
        'views/templates/info_map.xml',
        'views/templates/avrasya_in_numbers.xml',


        # Snippets
        'views/snippets/latest_posts_snippet.xml',
        'views/snippets/faqs_snippet.xml',
        'views/snippets/testimonials_snippet.xml',
        'views/snippets/index.xml',

        # Pages 
        'data/pages/home_page.xml',
        'data/pages/aboutus_page.xml',
        'data/pages/services_page.xml',
        'data/pages/facilitating_global_trade.xml',
        'data/pages/strategic_investments.xml',
        'data/pages/supply_chain_optimization.xml',
        'data/pages/market_entry_strategies.xml',
        'data/pages/case_study_page.xml',
        'data/pages/contactus_page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_avrasya/static/src/scss/main.scss',
            'theme_avrasya/static/src/scss/customize.scss',
            'theme_avrasya/static/src/components/testimonials/index.js',
            'theme_avrasya/static/src/components/testimonials/index.xml',
            'theme_avrasya/static/src/components/faqs/index.js',
            'theme_avrasya/static/src/components/faqs/index.xml',
            'theme_avrasya/static/src/components/blog/index.js',
            'theme_avrasya/static/src/components/blog/index.xml',
            'theme_avrasya/static/src/lib/owl-carousel/css/owl.carousel.min.css',
            'theme_avrasya/static/src/lib/owl-carousel/css/owl.theme.default.min.css',
            'theme_avrasya/static/src/lib/owl-carousel/js/owl.carousel.min.js',
            'theme_avrasya/static/src/js/owl-init.js',
            'theme_avrasya/static/src/js/index.js',
            'theme_avrasya/static/src/js/snippets.component.js',
        ],
        'web._assets_primary_variables': [
            'theme_avrasya/static/src/scss/primary_variables.scss',
        ],
    },
    'sequence': '1'
}

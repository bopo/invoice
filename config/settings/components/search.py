# -*- coding: utf-8 -*-

INSTALLED_APPS += (
    'haystack',
    'drf_haystack',
)


HAYSTACK_CONNECTIONS = {
    # 'default': {
    #     'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    # },
    # 'solr': {
    #     'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
    #     'URL': 'http://127.0.0.1:8983/solr'
    #     # ...or for multicore...
    #     # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    # },
    # 'default': {
    #     'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #     'URL': 'http://127.0.0.1:9200/',
    #     'INDEX_NAME': 'haystack',
    # },
    # 'default': {
    #     'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
    #     'URL': 'http://127.0.0.1:9200/',
    #     'INDEX_NAME': 'haystack',
    # },    
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), '..', 'runtime', 'whoosh_index'),
        'PATH': ROOT_DIR.path('runtime/indexes/whoosh_index').__str__(),
    },
    # 'xapian': {
    #     'ENGINE': 'xapian_backend.XapianEngine',
    #     'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
    # },    
}

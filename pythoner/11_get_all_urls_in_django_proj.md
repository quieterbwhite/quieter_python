# 获取 Django 项目中所有URL
> https://stackoverflow.com/questions/1828187/determine-complete-django-url-configuration

```python
def all_urls_view(request):
    from your_site.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically
    return render(request, "yourapp/links.html", {"links":nice_urls})

def get_urls(raw_urls, nice_urls=[], urlbase=''):
    '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
    from operator import itemgetter
    for entry in raw_urls:
        fullurl = (urlbase + entry.regex.pattern).replace('^','')
        if entry.callback: #if it points to a view
            viewname = entry.callback.func_name
            nice_urls.append({"pattern": fullurl, 
                  "location": viewname})
        else: #if it points to another urlconf, recur!
            get_urls(entry.url_patterns, nice_urls, fullurl)
    nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
    return nice_urls
```

```
Django is Python, so introspection is your friend.

In the shell, import urls. By looping through urls.urlpatterns, and drilling down through as many layers of included url configurations as possible, you can build the complete url configuration.

import urls
urls.urlpatterns
The list urls.urlpatterns contains RegexURLPattern and RegexURLResolver objects.

For a RegexURLPattern object p you can display the regular expression with

p.regex.pattern
For a RegexURLResolver object q, which represents an included url configuration, you can display the first part of the regular expression with

q.regex.pattern
Then use

q.url_patterns
which will return a further list of RegexURLResolver and RegexURLPattern objects.
```

# nginx+django 下载文件
> http://www.dannysite.com/blog/103/  

实现访问同一地址，鉴权，通过Nginx下载指定文件  

Django
```python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import View


class FileDownloadView(View):

    def get(self, request, *args, **kwargs):

        url = "/file/toto.txt?renameto=haha.txt"

        response = HttpResponse()
        response['Content-Type'] = ''
        response['X-Accel-Redirect'] = url
        return response

        """
        content_type='application/octet-stream
        response = HttpResponse(mimetype='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(path_to_file)
        response['X-Sendfile'] = "/home/bwhite/work/debt/docs/cfg/README.md"
        """
```

Nginx
```
upstream debt_server {
    server 127.0.0.1:8000;
}
 
server {

    server_name quieter.me;
 
    client_max_body_size 128M;
 
    access_log /tmp/debt-nginx-access.log;
    error_log /tmp/debt-nginx-error.log;

    keepalive_timeout 70;
    
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        add_header 'Access-Control-Allow-Origin' '*';
        add_header 'Access-Control-Allow-Credentials' 'true';
        add_header 'Access-Control-Allow-Methods' 'OPTION, POST, GET';
        add_header 'Access-Control-Allow-Headers' 'X-Requested-With, Content-Type';
 
        if (!-f $request_filename) {
            proxy_pass http://debt_server;
            break;
        }
    }

    location /file {
        internal;
        alias   /home/bwhite/work/debt/static/file;
        add_header Content-Disposition "attachment; filename=$arg_renameto";
    }
}
```

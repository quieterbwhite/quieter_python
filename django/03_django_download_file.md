# Django download file

## 读取本地文件并下载
```python
import os
from django.conf import settings
from django.http import HttpResponse

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
```

```
You need to read that file.
Serve it using HttpResponse along with proper content type.

Here's some sample code:

content = open("uploads/something.txt").read()
return HttpResponse(content, content_type='text/plain')

This should serve a text file.

But as you described, on some browser, it will not ask to download the file, rather, it would show it in the browser. If you want to show a download prompt, use this:

response = HttpResponse(open("uploads/something.txt", 'rb').read())
response['Content-Type'] = 'text/plain'
response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'
return response

However, please note that it might be a better idea to serve static contents or uploaded files via nginx or the reverse proxy of your choice. Sending large files through Django might not be the most optimum way of doing that.
```

## 内存中生成文件并下载
```
https://docs.djangoproject.com/en/1.8/howto/outputting-csv/
```

```python
from xlwt import Workbook

def get(self, request, *args, **kwargs):
    book = Workbook(encoding='utf-8')
    // fill book with your data here...
    response = HttpResponse(content_type='application/ms-excel')
    book.save(response)
    response['Content-Disposition'] = 'attachment; filename="%s"' % self.excel_file_name.encode("utf-8")
    response['Cache-Control'] = 'no-cache'
    return response
```

## 生成并下载pdf
```
https://docs.djangoproject.com/en/2.0/howto/outputting-pdf/
```

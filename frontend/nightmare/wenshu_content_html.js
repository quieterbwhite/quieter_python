const Nightmare = require('nightmare');
require('nightmare-webrequest-addon');

// Ref
// https://babycannotsay.github.io/Nightmare%E4%B8%AD%E6%96%87/ 【测试框架】Nightmare中文版
// https://my.oschina.net/mingyuejingque/blog/1573666 Nightmarejs 支持代理、命令行参数
// https://www.cnblogs.com/shengulong/p/9099992.html 定时任务crontab如何实现每秒执行？
// https://github.com/segmentio/nightmare/issues/665 could not make the proxy work
// https://github.com/segmentio/nightmare#proxies
// https://www.cnblogs.com/enjoymylift/archive/2018/01/29/8377507.html JS实现sleep()方法

const request = require('request');

const nightmare = Nightmare({
    switches: {
        'proxy-server': 'http-dyn.abuyun.com:9020',
        'ignore-certificate-errors': true
    },
    show: false
});

function sleep(delay) {
  var start = (new Date()).getTime();
  while ((new Date()).getTime() - start < delay) {
    continue;
  }
}

function getData(docid) {
    nightmare
    .authentication('HNB21F6H12B5WPOD', 'ADDC90A1041F6500')
    .goto('http://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=db20f235361046c68c7eaad500b0f513')
    .wait(3000)
    .evaluate(function() {
        let searchResults = {
            title : '',
            divList : []
        };

        searchResults.title = document.querySelector('.PDF_title').innerText;

        const PDF_pox =  document.querySelectorAll('.PDF_pox');
        
        PDF_pox.forEach(function(result) {
            searchResults.divList.push(result.innerHTML);
        });

        return searchResults;
    })
    .end()
    .then(function(result) {
        let title = result.title;
        let htmlDiv = result.divList[0];

        let totalLen = htmlDiv.length;
        let indexOfTitle = htmlDiv.indexOf('<title></title>')+15;
        let indexOfExtra = htmlDiv.indexOf('</div> </div> <div class="detail');
        let htmlDivPure = htmlDiv.substring(indexOfTitle, indexOfExtra);

        let html = '<html><head><title>' + title + '</title></head><body>' + htmlDivPure + '</body></html>';
        
        let res = {
            "doc_id": docid,
            "title": title,
            "trial_round": "",
            "case_no": "",
            "lawfirm": "",
            "lawfirm_province": "",
            "lawfirm_city": "",
            "lawfirm_country": "",
            "case_type": "",
            "reason": "",
            "html": html
        }

        console.log(res);

        // 发送数据
        var url="http://forward.spider.lhjksaas.com/recv/sifa";
        request({
            url: url,
            method: "POST",
            json: true,
            headers: {
                "content-type": "application/json",
            },
            body: res
        }, function(error, response, body) {
            if (!error && response.statusCode == 200) {
                console.log("upload data success");
                var updateUrl = "http://info.spider.lhjksaas.com/api/wsTask/updateWsTask"
                var body = {
                    'docid' : docid,
                    'statusContent' : 2
                }
                request({
                    url: updateUrl,
                    method: "POST",
                    json: true,
                    headers: {
                        "content-type": "application/json",
                    },
                    body: body
                }, function(error, response, body) {
                    if (!error && response.statusCode == 200) {
                        console.log("update task status to done success");
                    } else {
                        console.log("update task status to done fail");
                    }
                });
            } else {
                console.log("upload data fail");
            }
        }); 
    }).catch(function(e) {
        console.log(e);
    });
}

function foo() {
    // 获取任务
    request('http://info.spider.lhjksaas.com/api/wsTask/getWsTask2Content?count=1', function (error, response, body) {
        if (!error && response.statusCode == 200) { 
            let taskRes = JSON.parse(body);
            console.log(taskRes);
            if(taskRes.data.length > 0) {
                let docid = taskRes.data[0].docid;
                console.log(docid);
                getData(docid);
            } else {
                console.log('no task any more for now');
            }
        } else {
            console.log('bad request');
        }
    })
}

// 问题
// 1. 循环执行
// 2. 异步
// 3. 捕获异常
// 4. 用superip代理测试

try {
    console.log('start to get data');
    foo();
} catch(exception) {
    console.log(exception.message);
}

console.log("sleep for 3s");

/*
nightmare
    .goto('http://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=db20f235361046c68c7eaad500b0f513')
    .wait(3000)
    .evaluate(function() {
            let searchResults = "";
            
            searchResults =  document.querySelector('.PDF_pox div').innerHTML;
        
            return searchResults;
    })
    .end()
    .then(function(result) {
        console.log(result);
    })
    .catch(function(e)  {
            console.log(e);
    });
*/
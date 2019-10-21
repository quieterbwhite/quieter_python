const Nightmare = require('nightmare');
const nightmare = Nightmare({
    show: false,
    // switches: {
        // 'proxy-server': 'HNB21F6H12B5WPOD:ADDC90A1041F6500@http-dyn.abuyun.com:9020',
        // 'ignore-certificate-errors': true
    // }
});

function sleep(delay) {
  var start = (new Date()).getTime();
  while ((new Date()).getTime() - start < delay) {
    continue;
  }
}

function parseData(result) {
    console.log(result);
    console.log('222');
}

function getData(docid) {
    nightmare
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

        // console.log(htmlDiv);
        // console.log(title);

        let totalLen = htmlDiv.length;
        let indexOfTitle = htmlDiv.indexOf('<title></title>')+15;
        let indexOfExtra = htmlDiv.indexOf('</div> </div> <div class="detail');
        let htmlDivPure = htmlDiv.substring(indexOfTitle, indexOfExtra);

        let html = '<html><head><title>' + title + '</title></head><body>' + htmlDivPure + '</body></html>';
        console.log(html);
    })
    .catch(function(e)  {
        console.log(e);
    });
}

for (var i=0;i<10;i++)
{ 
    let docid = 'db20f235361046c68c7eaad500b0f513';
    console.log(docid);
    if(i==1) {
        let a = getData(docid);
        // console.log(a);
        console.log('a');
        break;
    } else {
        console.log('hah');
        sleep(2000);
        continue;
    }
}


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
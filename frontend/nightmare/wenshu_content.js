const Nightmare = require('nightmare');
const nightmare = Nightmare({show: false});


nightmare
    .goto('http://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=db20f235361046c68c7eaad500b0f513')
    .wait(3000)
    .evaluate(function() {
            let searchResults = [];

            const results =  document.querySelectorAll('.PDF_title');
            results.forEach(function(result) {
                    let row = {
                                    'title':result.innerText,
                              }
                    //searchResults.push(row);
            });
            
            const PDF_pox =  document.querySelectorAll('.PDF_pox div');
            
            PDF_pox.forEach(function(result) {
                    let row = {
                                    'title':result.innerText,
                              }
                    searchResults.push(row);
            });
            
            return searchResults;
    })
    .end()
    .then(function(result) {
            result.forEach(function(r) {
                    console.log('Title: ' + r.title);
            })
    })
    .catch(function(e)  {
            console.log(e);
    });

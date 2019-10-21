const Nightmare = require('nightmare');
const nightmare = Nightmare({show: false});



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
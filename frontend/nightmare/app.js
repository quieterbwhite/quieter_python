const Nightmare = require('nightmare')
const nightmare = new Nightmare({
     show: true
 })

//nightmare.goto('http://zxgk.court.gov.cn/zhzxgk/')
nightmare.goto('http://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=db20f235361046c68c7eaad500b0f513')
.wait(3000)
.evaluate(function() {
    // 该环境中能使用浏览器中的任何对象window/document，并且返回一个promise
    // console.log('hello nightmare')
    // console.log('5 second close window')
    
    //document.getElementById("pName").value = "nimade";
})
.wait(1000)
.end()
.then(()=> {
    console.log('close nightmare')
})

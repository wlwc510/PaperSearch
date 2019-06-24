/**
 * 返回一个当前的时间
 * @return {{time: string, date: string, week: string}}
 */
export function updateTime() {
    let week = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
    let mTime = {
        //时间
        time: '',
        //日期
        date: '',
        //星期
        week: ""
    };
    let cd = new Date();
    mTime.time = zeroPadding(cd.getHours(), 2) + ':' + zeroPadding(cd.getMinutes(), 2) + ':' + zeroPadding(cd.getSeconds(), 2);
    mTime.date = zeroPadding(cd.getFullYear(), 4) + '-' + zeroPadding(cd.getMonth() + 1, 2) + '-' + zeroPadding(cd.getDate(), 2);
    mTime.week = week[cd.getDay()];

    return mTime;
}


//处理时间
function zeroPadding(num, digit) {
    let zero = '';
    for (let i = 0; i < digit; i++) {
        zero += '0';
    }
    return (zero + num).slice(-digit);
}





/**
 * 字符串转日期格式，strDate要转为日期格式的字符串
 * @param strDate
 * @return 转换好的时间格式
 */
export function getDate(strDate) {

    if(strDate===null||strDate===""){
        return "";
    }
    let  arr=strDate.split(".");
    return arr[0].replace("T", "  ");
}

/**
 * 时间转字符串
 * @param now 需要转换的时间
 * @return string
 */
export function dateToString(now){

     //判断是否为日期类型
    if(!isDate(now)){
        return now;
    }


    let year = now.getFullYear();
    let month =(now.getMonth() + 1).toString();
    let day = (now.getDate()).toString();
    let hour = (now.getHours()).toString();
    let minute = (now.getMinutes()).toString();
    let second = (now.getSeconds()).toString();
    if (month.length === 1) {
        month = "0" + month;
    }
    if (day.length === 1) {
        day = "0" + day;
    }
    if (hour.length === 1) {
        hour = "0" + hour;
    }
    if (minute.length === 1) {
        minute = "0" + minute;
    }
    if (second.length === 1) {
        second = "0" + second;
    }

    return year + "-" + month + "-" + day +" "+ hour +":"+minute+":"+second;
}

function isDate(obj){
    return (typeof obj=='object')&&obj.constructor==Date;
}


/**
 * 判断开始时间小于结束时间
 * @param startDate  开始时间
 * @param endDate  结束时间
 */
export function enTime(startDate,endDate){
    console.log(startDate,endDate);
    let  mStartDate=0;

    let  mEndDate =0;

    if(startDate!==null&&startDate!==""){
        mStartDate= new Date((startDate).replace(new RegExp("-","gm"),"/")).getTime();
    }

   if(endDate!==null&&endDate!==""){
       mEndDate = new Date((endDate).replace(new RegExp("-","gm"),"/")).getTime();
   }
    console.log(mStartDate,mEndDate);

    return mStartDate <= mEndDate;
}

/**
 * 时间格式转化
 * @param obj 传入的时间
 * @return {string} 返回的字符串
 */
export function fmtDate(obj){
    const date =  new Date(obj);
    const y = 1900+date.getYear();
    const m = "0"+(date.getMonth()+1);
    const d = "0"+date.getDate();
    return y+"-"+m.substring(m.length-2,m.length)+"-"+d.substring(d.length-2,d.length);
}


/************************************************************
 * 这个工具类主要是判断一些字符，以及做一些正则，
 * 不要往里面乱添加方法
 ************************************************************
 **/

/**
 *这个是判断这个值是不是一个空值
 * @param exp  传入的一个值
 */
export function whetherNull(exp) {
    return typeof(exp) !== "undefined" && exp !== 0 && exp !== null && exp !== "";
}

/**
 * 判断是否为数字
 * @param nubmer 传入的数字
 * @return {boolean}
 */
export function checkRate(nubmer) {
    let re = /^[0-9]+.?[0-9]*/;//判断字符串是否为数字//判断正整数/[1−9]+[0−9]∗]∗/
    if (re.test(nubmer)) {
        return true;
    }else {
        return false;
    }
}

/**判断字符串是否为时间字符串*/
export function   isnothour(str) {
    let re = /^(([0-1]\d)|(2[0-4])):[0-5]\d$/; //判断是不是小时
    if (re.test(str)) {
        return true;
    } else {
        return false;
    }
}

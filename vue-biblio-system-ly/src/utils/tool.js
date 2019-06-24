/*工具类-绝大多数页面都要用到的封装类集合*/
// noinspection JSAnnotator
import store from '../store/index';
/**
 *表格、右侧展示页高度自适应。窗口高度-头部高度-一些附加的高度
 * @param 表格id,根据不同情况页面减去的自定义高度
 */
export function sreenFullHeight(id,customH) {
    let body_h = store.state.zheight.body;
    let tags_h =store.state.zheight.tags;
    let hh=document.getElementById(id).getBoundingClientRect().top;
    document.getElementById(id).style.height=(body_h-tags_h-hh-customH)+"px";

    console.log("调试高度2", document.getElementById(id).style.height);
}
export function newMessage (str){
    const newMessage= this.$message({
        message: str,
        type: 'warning'
    });
};



//浮点加法计算
//加
export function add(a, b) {
    var c, d, e;
    try {
        c = a.toString().split(".")[1].length;
    } catch (f) {
        c = 0;
    }
    try {
        d = b.toString().split(".")[1].length;
    } catch (f) {
        d = 0;
    }
    return e = Math.pow(10, Math.max(c, d)), (mul(a, e) + mul(b, e)) / e;
}
//减
export function sub(a, b) {
    var c, d, e;
    try {
        c = a.toString().split(".")[1].length;
    } catch (f) {
        c = 0;
    }
    try {
        d = b.toString().split(".")[1].length;
    } catch (f) {
        d = 0;
    }
    return e = Math.pow(10, Math.max(c, d)), (mul(a, e) - mul(b, e)) / e;
}
//除
export function mul(a, b) {
    var c = 0,
        d = a.toString(),
        e = b.toString();
    try {
        c += d.split(".")[1].length;
    } catch (f) {}
    try {
        c += e.split(".")[1].length;
    } catch (f) {}
    return Number(d.replace(".", "")) * Number(e.replace(".", "")) / Math.pow(10, c);
}

//乘
export function div(a, b) {
    if(Number(b) !==0){
        var c, d, e = 0,
            f = 0;
        try {
            e = a.toString().split(".")[1].length;
        } catch (g) {}
        try {
            f = b.toString().split(".")[1].length;
        } catch (g) {}
        c = Number(a.toString().replace(".", "")), d = Number(b.toString().replace(".", ""));
        var divNum = mul(c / d, Math.pow(10, f - e));

        return divNum;
    }else {
        return 0;
    }
}

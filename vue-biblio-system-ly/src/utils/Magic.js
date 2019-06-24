/*存放一些魔法值*/

const config = {
    //添加用户
    ADDUSER:'01',
    //更新用户
    UPDATEUSER:'02'
};

let bindToGlobal = (obj, key) => {
    if (typeof window[key] === 'undefined') {
        window[key] = {};
    }

    for (let i in obj) {
        window[key][i] = obj[i]
    }
};

bindToGlobal(config,'_Magic');

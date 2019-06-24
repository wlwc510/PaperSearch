import axios from 'axios';
import {Loading} from 'element-ui';
import {Message} from 'element-ui';
import {MessageBox} from 'element-ui';
import router from './../router';

axios.defaults.timeout = 30000;
axios.defaults.baseURL = '';


//http request 拦截器
axios.interceptors.request.use(
    config => {
        // const token = getCookie('名称');注意使用的时候需要引入cookie方法，推荐js-cookie
        config.data = JSON.stringify(config.data);

        let tokenId = localStorage.getItem('tokenId');
        config.headers = {
            /* 'Content-Type':'application/x-www-form-urlencoded'*/
            'Content-Type': 'application/json',
            'tokenId': tokenId
        };
        /*if(localStorage.getItem('ms_username')){
          config.params = {'token':localStorage.getItem('ms_username')}
        }*/
        // if(token){
        //   config.params = {'token':token}
        // }
        return config;
    },
    error => {
        return Promise.reject(err);
    }
);


//http response 拦截器
axios.interceptors.response.use(
    response => {
        if (response.data.errCode === 2) {
            router.push({
                path: "/login",
                querry: {redirect: router.currentRoute.fullPath}//从哪个页面跳转
            })
        }
        return response;
    },
    error => {
        return Promise.reject(error)
    }
);


/**
 * 封装get方法
 * @param url
 * @param params
 * @returns {Promise}
 */
export function fetch(url, params = {}) {
    return new Promise((resolve, reject) => {
        const loading = this.$loading({
            lock: true,
            text: '加载中',
            spinner: 'el-icon-loading',
            background: 'rgba(0, 0, 0, 0.7)'
        });

        axios.get(url, {
            params: params
        })
            .then(response => {

                landing(url, params, response.data);
                resolve(response.data);
                setTimeout(() => {
                    loading.close();
                }, 1000);
            })
            .catch(err => {
                reject(err);
                setTimeout(() => {
                    loading.close();
                    msag();
                }, 1000);

            })
    })
}


/**
 * 封装get方法 不待loading
 * @param url
 * @param params
 * @returns {Promise}
 */
export function fetchNo(url, params = {}) {

    return new Promise((resolve, reject) => {
        axios.get(url, {
            params: params
        }).then(response => {
            landing(url, params, response.data);
            resolve(response.data);

        }).catch(err => {
            reject(err);

        })
    })
}


/**
 * 封装post请求
 * @param url
 * @param data
 * @returns {Promise}
 */

export function post(url, data) {
    return new Promise((resolve, reject) => {
        //j进度条
        const loading = this.$loading({
            lock: true,
            text: 'Loading',
            spinner: 'el-icon-loading',
            background: 'rgba(0, 0, 0, 0.7)'
        });

        axios.post(url, data).then(response => {

            //关闭进度条
            resolve(response.data);
            setTimeout(() => {
                landing(url, data, response.data);
                loading.close();
            }, 1000);


        }, err => {
            setTimeout(() => {
                loading.close();
                msag();
            }, 1000);

            reject(err)
        })
    })
}

/**
 * 封装patch请求
 * @param url
 * @param data
 * @returns {Promise}
 */

export function patch(url, data = {}) {
    return new Promise((resolve, reject) => {
        axios.patch(url, data)
            .then(response => {
                resolve(response.data);
            }, err => {
                msag();
                reject(err)
            })
    })
}

/**
 * 封装put请求
 * @param url
 * @param data
 * @returns {Promise}
 */

export function put(url, data = {}) {
    return new Promise((resolve, reject) => {
        axios.put(url, data)
            .then(response => {
                resolve(response.data);
            }, err => {
                msag();
                reject(err)
            })
    })
}


//失败提示
function msag() {
    Message({
        message: "网络请求失败,请检查网络",
        type: 'warning'
    });
}


/**
 * 查看返回的数据
 * @param url
 * @param params
 * @param data
 */
function landing(url, params, data) {

    console.log("接口请求地址=====>", url);
    console.log("接口传递参数=====>", params);
    console.log("接口返回数据=====>", data);


    if (data.code === -1) {
        MessageBox.alert(data.msg, '提示', {
            confirmButtonText: '确定',
            callback: action => {
                window.location.href=window.location.origin + '/#/login'
               /* router.replace('/login');
               //人为制造一个错误，引发js 异常机制。中断执行
                $ddd.dd();*/
            }
        });
    }
}

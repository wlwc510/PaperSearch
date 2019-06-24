import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
import '../static/css/icon.css';
import "babel-polyfill";

Vue.use(ElementUI, {size: 'small'});
Vue.prototype.$axios = axios;

//引入全局静态变量
import './utils/global.js'
//引入魔法值
import './utils/Magic.js'

//网络请求
import {post, fetch, fetchNo, put} from './utils/http'
//定义全局变量
Vue.prototype.$post = post;//发
Vue.prototype.$fetch = fetch;//取
Vue.prototype.$fetchNo = fetchNo;  //不待loading get
Vue.prototype.$put = put;//更新 更新

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
    const role = localStorage.getItem('ms_username');
    if (to.path === '/registered') {
        console.log(to.path);
        console.log("dsd")
        next();
    }else if (!role && to.path !== '/login') {
        next('/login');
    } else {
        next();
    }
});

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

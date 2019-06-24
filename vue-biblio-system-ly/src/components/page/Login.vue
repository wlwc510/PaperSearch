<script src="../../router/index.js"></script>
<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">文献全文语义检索系统登陆</div>
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="ms-content">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="username">
                        <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')">
                        <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                    </el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button el-button type="primary" round @click="submitForm('ruleForm')">登录</el-button>
                    <el-button el-button type="warning" round @click="subRegistered()">注册</el-button>
                </div>
                <p class="login-tips">Tips : 用户名和密码。</p>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        data: function(){
            return {
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            //点击登陆
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                       // localStorage.setItem('ms_username',this.ruleForm.username);
                        console.log(this.ruleForm);
                       // this.$router.push('/');
                        /*const data = {
                            username: this.ruleForm.username,
                            password: this.ruleForm.password
                        };*/
                        const data = {
                            username: this.ruleForm.username,
                            password: this.ruleForm.password
                       };
                        //网络请求登陆接口
                        this.httplogin(global.LOGIN,data);
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            //登陆的网络请求
            httplogin(url,data) {
                console.log(this.ruleForm);
                let tbh = this;
                this.$post(url,data).then((response) => {
                    console.log(response);
                    if (response.code === 200) {
                        // this.tableData = response.list;
                        //存到缓存
                        localStorage.setItem('ms_username', response.data.username);
                        localStorage.setItem('userRole', 0);
                        //将存到缓存唯一标识
                        localStorage.setItem('uuid', response.data.uuid);

                        tbh.$router.push('/');
                        // 请求菜单
                       // this.httpMenu();
                    } else {
                        tbh.$notify.info({
                            title: '消息',
                            message: response.message,
                            type: 'warning'
                        });
                    }
                }, err => {
                    console.log(err);
                });
            },
            //点击注册
            subRegistered(){
                this.$router.push('/registered');
                console.log("点击注册");
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width:100%;
        height:100%;
        background-image: url(../../assets/naturecover.jpg);
        background-size: 100%;
    }
    .ms-title{
        width:100%;
        line-height: 50px;
        text-align: center;
        font-size:20px;
        color: #fff;
        border-bottom: 1px solid #ddd;
    }
    .ms-login{
        position: absolute;
        left:50%;
        top:50%;
        width:350px;
        margin:-190px 0 0 -175px;
        border-radius: 5px;
        background: rgba(255,255,255, 0.3);
        overflow: hidden;
    }
    .ms-content{
        padding: 30px 30px;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width:45%;
        height:36px;
        margin-bottom: 10px;
    }
    .login-tips{
        font-size:12px;
        line-height:30px;
        color:#fff;
    }
</style>

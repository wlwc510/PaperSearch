<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">用户信息注册</div>
            <el-form :model="ruleForm"  label-width="80px" class="aform">

                <el-form-item label="用户名">
                    <el-input v-model="ruleForm.username"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                    <el-input type="password" v-model="ruleForm.password"></el-input>
                </el-form-item>
                <el-form-item label="确认密码">
                    <el-input type="password" v-model="ruleForm.password2"></el-input>
                </el-form-item>
                <el-form-item label="偏好">
                    <el-input  v-model="ruleForm.preference"></el-input>
                </el-form-item>

                <div class="login-btn">
                    <el-button el-button type="primary" round @click="subRegistered(ruleForm)">注册</el-button>
                    <el-button el-button type="warning" round @click="submitForm()">返回登录</el-button>
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
                //初始化用过户信息
                ruleForm: {
                    username: '',
                    password: '',
                    password2: '',
                    preference:""
                }
            }
        },
        methods: {
            //点击注册
            subRegistered(ruleForm){
                console.log(ruleForm);
                if(ruleForm.username===""){
                    this.$notify.error({
                        title: '错误',
                        message: '请输入用户名！'
                    });
                    return;
                }
                if(ruleForm.password===""){
                    this.$notify.error({
                        title: '错误',
                        message: '请输入密码！'
                    });
                    return;
                }
                if(ruleForm.password2===""){
                    this.$notify.error({
                        title: '错误',
                        message: '请输入确认密码！'
                    });
                    return;
                }

                if(ruleForm.preference===""){
                    this.$notify.error({
                        title: '错误',
                        message: '请输入偏好！'
                    });
                    return;
                }

               if(ruleForm.password!==ruleForm.password2){
                   this.$notify.error({
                       title: '错误',
                       message: '密码不一致'
                   });
                   return;
               }
                const user = {
                    username: ruleForm.username,
                    password:ruleForm.password,
                    preference: ruleForm.preference
                };
                this.httplogin(global.REGISTERED,user);
            },
            //注册的网络请求
            httplogin(url,data) {
                console.log(this.ruleForm);
                let tbh = this;
                this.$post(url,data).then((response) => {
                    console.log(response);
                    if (response.code === 200) {
                        // this.tableData = response.list;
                        //存到缓存
//                        localStorage.setItem('ms_username', response.data.nickName);
                        //将存到缓存唯一标识
                        localStorage.setItem('username',response.data.name)
                        localStorage.setItem('uuid', response.data.uuid);
                        localStorage.setItem('userRole', "0");

                        tbh.$router.push('/login');
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

            //点击返回登陆
            submitForm(formName) {
                this.$router.push('/login');
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width:100%;
        height:100%;
        background-image: url(../../assets/login-bg.jpg);
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
        background: #e4e7ed;
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
    .aform{
        margin: 15px;
     }
</style>

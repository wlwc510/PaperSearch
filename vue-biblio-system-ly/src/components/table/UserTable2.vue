<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-calendar"></i> 用户管理test</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <el-button type="primary"  @click="handleAdd" >新增</el-button>
            <el-table
                :data="tableData"
                border
                style="width: 100%;margin-top: 10px">
                <el-table-column
                    prop="username"
                    label="用户名"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="nickName"
                    label="昵称">
                </el-table-column>

                <el-table-column label="性别">
                    <template slot-scope="scope">
                        <span>{{scope.row.sex===0?'男':'女'}}</span>
                    </template>
                </el-table-column>

                <el-table-column
                    prop="mail"
                    label="邮箱">
                </el-table-column>

                <el-table-column
                    label="注册时间">
                    <template slot-scope="scope">
                        <span>{{Timestr(scope.row.registerDate)}}</span>
                    </template>
                </el-table-column>

                <el-table-column
                    label="最近登陆时间">
                    <template slot-scope="scope">
                        <span>{{Timestr(scope.row.modifyDate)}}</span>
                    </template>
                </el-table-column>
                <el-table-column label="角色">
                    <template slot-scope="scope">
                        <span>{{scope.row.userRole===0?'管理员':'用户'}}</span>
                    </template>
                </el-table-column>

                <el-table-column label="操作"  width="200">
                    <template slot-scope="scope">
                        <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">编辑
                        </el-button>
                        <el-button
                            size="mini"
                            type="danger"
                            @click="handleDelete(scope.$index, scope.row)">删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="block">
                <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page="paging.currentPage"
                    :page-sizes="[10, 20, 50, 100]"
                    :page-size="this.paging.pageSize"
                    layout="total, sizes, prev, pager, next, jumper"
                    :total="paging.total">
                </el-pagination>
            </div>
        </div>
        <el-dialog
            :title="Anobject.title"
            :visible.sync="dialogVisible"
            width="30%">
            <el-form label-width="80px">
                <el-form-item label="姓名">
                    <el-input v-model="Anobject.username"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                    <el-input type="password" v-model="Anobject.password"></el-input>
                </el-form-item>
                <el-form-item label="性别">
                    <el-radio-group v-model="Anobject.sex">
                        <el-radio :label="0">男</el-radio>
                        <el-radio :label="1">女</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="邮箱">
                    <el-input v-model="Anobject.mail"></el-input>
                </el-form-item>

                <el-form-item label="昵称">
                    <el-input v-model="Anobject.nickName"></el-input>
                </el-form-item>
                <el-form-item label="手机号">
                    <el-input  v-model="Anobject.phoneNumber"  maxlength="11" ></el-input>
                </el-form-item>
                <el-form-item label="用户角色">
                    <el-radio-group v-model="Anobject.userRole">
                        <el-radio :label="0">管理员</el-radio>
                        <el-radio :label="1">普通用户</el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="updateUser">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import {getDate,dateToString} from '../../utils/Time'
    export default {
        name: "userTable",
        //表格的显示
        data: () => ({
            //其中一条
            Anobject: {},
            //表格列表的数据
            tableData: [],
            dialogVisible: false,
            paging: {
                //当前显示的页码
                currentPage: 1,
                pageSize: 10,
                total: 10
            }

        }),
        //自动执行的一个方法
        mounted() {
            //获取用户列表
            this.httpdata(global.GETUSER);
        },

        methods: {
            //获取每页条数
            handleSizeChange(val) {
                //console.log(`每页 ${val} 条`);
                this.paging.pageSize = val;
                this.httpdata(global.GETUSER);
            },
            //获取当前页数
            handleCurrentChange(val) {
                //console.log(`当前页: ${val}`);
                this.paging.currentPage = val;
                //console.log("网络请求地址==》",global.GETUSER);

                this.httpdata(global.GETUSER);
            },
            //点击编辑
            handleEdit(_index, row) {
                //vue对象拷贝
                this.Anobject = JSON.parse(JSON.stringify(this.tableData[_index]));
                this.Anobject.title="更新提示";
                this.Anobject.type=_Magic.UPDATEUSER;
                console.log(this.Anobject);

                this.dialogVisible = true;
            },
            //点击删除
            handleDelete(_index, row) {
                //console.log(_index, row);

                const data = {
                    id: row.id
                };
                this.deletehttpdata(global.DELETEUSER, data);

            },
            //处理时间
            Timestr(str) {
                //console.log(str);
                return getDate(str);
            },
            //添加或者更新的确定
            updateUser() {
                this.dialogVisible=false;
                //console.log( this.Anobject.registerDate);

                const user = {
                    //姓名
                    username: this.Anobject.username,
                    //密码
                    password:this.Anobject.password,
                    //性别
                    sex: this.Anobject.sex+"",
                    //昵称
                    nickName:this.Anobject.nickName,
                    //邮箱
                    mail:this.Anobject.mail,
                    //手机号
                    phoneNumber:this.Anobject.phoneNumber,
                    //用户角色
                    userRole:this.Anobject.userRole
                };

                if(this.Anobject.type===_Magic.ADDUSER){
                    //添加用户
                    this.addhttpdata(global.REGISTERED,user)
                }else if(this.Anobject.type===_Magic.UPDATEUSER){
                    user.id=this.Anobject.id;
                    //更新
                    this.updatehttpdata(global.UPDATEUSER, user)
                }
            },

            //添加用户
            handleAdd(){
                this.Anobject={};
                this.Anobject.title="新增用户";
                //添加状态
                this.Anobject.type=_Magic.ADDUSER;
                this.dialogVisible = true;
            },
            //网络请求列表数据
            httpdata(str) {
                //console.log(str);
                this.$fetch(str, {page: this.paging.currentPage, size: this.paging.pageSize}).then((response) => {
                    //console.log(response);
                    if (response.code === 200) {
                        const data = response.data;
                        this.tableData = data.list;
                        //console.log(data.total);
                        this.paging.total = parseInt(data.total);
                    } else {
                        this.$message.error('失败');
                    }
                    ////console.log(response.data);
                    const data = response.data;
                }, err => {
                    //console.log(err);
                });
            },
            //更新的网络请求
            updatehttpdata(str, user) {
                const _thb = this;
                this.$post(str, user).then((response) => {
                    if (response.code === 200) {
                        //console.log(response.data);
                        _thb.httpdata(global.GETUSER);
                    }
                }, err => {
                    //console.log(err);
                });
            },
            //删除的网络请求
            deletehttpdata(str, data) {
                const _thb = this;
                //console.log(str, data);
                this.$post(str, data).then((response) => {
                    if (response.code === 200) {
                        //console.log(response);
                        this.$message({
                            message: '删除成功',
                            type: 'success'
                        });
                        _thb.httpdata(global.GETUSER);

                    } else {
                        this.$message.error('失败');
                    }
                }, err => {
                    //console.log(err);
                });
            },
            //新增的网络请求
            addhttpdata(str, user){
                const _thb = this;
                this.$post(str, user).then((response) => {
                    if (response.code === 200) {
                        //console.log(response.data);
                        _thb.httpdata(global.GETUSER);
                    }
                }, err => {
                    //console.log(err);
                });
            }

        }

    }
</script>


<style scoped>
    .block {
        margin-top: 20px;
        width: 100%;
        text-align: center
    }
</style>

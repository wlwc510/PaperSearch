<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-calendar"></i> 结合全文语义的文献检索</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <!-- v-model="select_word"-->
                <el-input  placeholder="筛选关键词" v-model="select_word" class="handle-input mr10"></el-input>
                <!--<el-button type="primary" icon="search" @click="search">搜索</el-button>-->
                <el-button type="primary" icon="search" @click="SemanticSearch">语义搜索</el-button>
                <span v-model="similar_words">{{similar_words}}</span>
                <!--<el-button type="primary" icon="search" @click="search">协同过滤</el-button>-->
            </div>
                <!--<el-button type="primary"  @click="handleAdd" >新增</el-button>-->
            <el-table
                :data="tableData"
                border
                style="width: 100%;margin-top: 10px">

                <el-table-column
                    prop="authors"
                    label="作者"
                    width="180"
                    class="el_table" show-overflow-tooltip>
                </el-table-column>
                <el-table-column
                    prop="title"
                    label="标题" show-overflow-tooltip>
                </el-table-column>

                <el-table-column
                    prop="introduction"
                    label="引言" show-overflow-tooltip>
                </el-table-column>

                <el-table-column
                    prop="methods"
                    label="方法" show-overflow-tooltip>
                </el-table-column>

                <el-table-column
                    prop="results"
                    label="结果" show-overflow-tooltip>
                </el-table-column>

                <el-table-column
                    prop="discussion"
                    label="讨论" show-overflow-tooltip>
                </el-table-column>

                <el-table-column
                    prop="references"
                    label="引文" show-overflow-tooltip>
                </el-table-column>

                <el-table-column prop="url" label="地址" show-overflow-tooltip>
<!--                    <template slot-scope="scope">-->
<!--                        <span>{{"www.nature.com"+scope.row.url+''}}</span>-->
<!--                    </template>-->
                </el-table-column>
                <!--<el-table-column label="初始评分">-->
                    <!--<template slot-scope="scope">-->
                        <!--<el-input v-show="scope.row.edit" v-model="scope.row.score"></el-input>-->
                        <!--<span v-show="!scope.row.edit">{{scope.row.score}}</span>-->
                    <!--</template>-->
                <!--</el-table-column>-->
                <!--<el-table-column label="分值">-->
                    <!--&lt;!&ndash;v-model="defautl_score":disable="false"&ndash;&gt;-->
                    <!--<template slot-scope="scope">-->
                        <!--&lt;!&ndash;<el-input v-show="scope.row.edit" v-model="scope.row.score"></el-input>&ndash;&gt;-->
                        <!--&lt;!&ndash;<span v-show="!scope.row.edit">{{scope.row.score}}</span>&ndash;&gt;-->
                        <!--<el-button :type="scope.row.edit?'success':'primary'" @click='updateScore(scope.$index,scope.row)' size="small" icon="edit">{{scope.row.edit?'完成':'打分'}}</el-button>-->
                    <!--</template>-->

                <!--</el-table-column>-->
                <!--<el-table-column label="更新">-->
                    <!--<template slot-scope="scope">-->
                        <!--<el-button type="primary"  @click="Rating(scope.$index,scope.row)">-->
                            <!--打分-->
                        <!--</el-button>-->
                    <!--</template>-->
                <!--</el-table-column>-->
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
<!--        //跳出的编辑框-->
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
            select_word:'',
            similar_words:'',
            //默认分值
            defautl_score:'',
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
            SemanticSearch()
            {
                const input=this.select_word;
                const data={
                    input:input
                };
                this.httpsemanticquerydata(global.SearchPost,data);
            },
            updateScore(_index,row)
            {
                row.edit=!row.edit;
                if(!row.edit)
                {
                    const t_uuid=localStorage.getItem("uuid");
//                    alert(localStorage.getItem("uuid"));
//                    const score=Math.random();
                    const data={
                        uuid:t_uuid,
                        paperid:row.url,
                        score:row.score
                    };
//                    alert(global.RATING);
//                    alert(JSON.stringify(data));
                    this.httprating(global.RATING,data);
                }

            },

            //获取每页条数
            handleSizeChange(val) {
                //console.log(`每页 ${val} 条`);
                //判断获取对象不会空
                const querytext=localStorage.getItem("semantic");
//                alert(querytext);
                this.paging.pageSize = val;
                if(querytext!=null)
                {
                    const data={
                        text:querytext,
                        page:this.paging.currentPage,
                        size:this.paging.pageSize
                    }
                    this.httpdataquery(global.QUERY,data);
                }else
                {

                    this.httpdata(global.GETUSER);
                }

            },
            //获取当前页数
            handleCurrentChange(val) {
                //console.log(`当前页: ${val}`);
                this.paging.currentPage = val;
                //console.log("网络请求地址==》",global.GETUSER);
                const querytext=localStorage.getItem("semantic");

                if(querytext!=null)
                {
                    const data={
                        text:querytext,
                        page:this.paging.currentPage,
                        size:this.paging.pageSize
                    }
                    this.httpdataquery(global.QUERY,data);
                }else {
                    this.httpdata(global.GETUSER);
                }
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
            httprating(str,data) {
                //console.log(str);
                this.$post(str, data).then((response) => {
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
//                    const data = response.data;
                }, err => {
                    //console.log(err);
                });
            },
            //网络请求列表数据
            httpsemanticquerydata(str,data) {
                //console.log(str);
                this.$post(str,data).then((response) => {
                    //console.log(response);
                    if (response.code === 200) {
                        const data = response.data;
                        this.similar_words =JSON.stringify(data);
//                        alert(data[0][0]);
                        let query=this.select_word;
                        query+=" ";
                        //发送进一步查询
                        for (var key in data)
                        {
                            query+=data[key][0];
                            query+=" ";
                        }
//                        alert(query);
                        localStorage.setItem("semantic",query);
                        const querydata={
                            text:query,
                            page:this.paging.currentPage,
                            size:this.paging.pageSize
                        };
                        this.httpdataquery(global.QUERY,querydata);
                        //console.log(data.total);
//                        this.paging.total = parseInt(data.total);
                    } else {
                        this.$message.error('失败');
                    }
                    ////console.log(response.data);
//                    const data = response.data;
                }, err => {
                    //console.log(err);
                });
            },
            //网络请求列表数据
            httpdataquery(str,data) {
                //console.log(str);
                this.$fetch(str, data).then((response) => {
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
    .handle-box {
        margin-bottom: 20px;
    }
    .handle-input {
        width: 300px;
        display: inline-block;
    }
    .block {
        margin-top: 20px;
        width: 100%;
        text-align: center
    }
    .el_table
    {
        vertical-align:top
    }
</style>

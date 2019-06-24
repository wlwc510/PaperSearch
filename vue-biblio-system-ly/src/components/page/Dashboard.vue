<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover" class="mgb20" style="height:252px;">
                    <div class="user-info">
                        <img src="static/img/nature2.jpg" class="user-avator" alt="">
                        <div class="user-info-cont">
                            <div class="user-info-name">{{name}}</div>
                            <div>{{role}}</div>
                        </div>
                    </div>
<!--                    <div class="user-info-list">上次登录时间：<span>{{LastTime}}</span></div>-->
                    <div class="user-info-list">上次登录地点：<span>无锡</span></div>
                </el-card>
                <el-card shadow="hover">
                    <div slot="header" class="clearfix">
                        <span>用户信息</span>
                    </div>

                    <el-row v-for="(user,index) in userList" :key="index">
                        <el-col :span="6">
                            {{user.name}}
                        </el-col>
                        <el-col :span="18">
                            {{user.value}}
                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
            <el-col :span="16">
<!--                <el-row :gutter="20" class="mgb20">-->
<!--                    <el-col :span="8">-->
<!--                        <el-card shadow="hover" :body-style="{padding: '0px'}">-->
<!--                            <div class="grid-content grid-con-1">-->
<!--                                <i class="el-icon-lx-people grid-con-icon"></i>-->
<!--                                <div class="grid-cont-right">-->
<!--                                    <div class="grid-num">200</div>-->
<!--                                    <div>银行卡余额</div>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </el-card>-->
<!--                    </el-col>-->
<!--                    <el-col :span="8">-->
<!--                        <el-card shadow="hover" :body-style="{padding: '0px'}">-->
<!--                            <div class="grid-content grid-con-2">-->
<!--                                <i class="el-icon-lx-notice grid-con-icon"></i>-->
<!--                                <div class="grid-cont-right">-->
<!--                                    <div class="grid-num">12</div>-->
<!--                                    <div>系统消息</div>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </el-card>-->
<!--                    </el-col>-->
<!--                    <el-col :span="8">-->
<!--                        <el-card shadow="hover" :body-style="{padding: '0px'}">-->
<!--                            <div class="grid-content grid-con-3">-->
<!--                                <i class="el-icon-lx-goods grid-con-icon"></i>-->
<!--                                <div class="grid-cont-right">-->
<!--                                    <div class="grid-num">5000</div>-->
<!--                                    <div>贷款金额</div>-->
<!--                                </div>-->
<!--                            </div>-->
<!--                        </el-card>-->
<!--                    </el-col>-->
<!--                </el-row>-->
                <el-card shadow="hover">
                    <div slot="header" class="clearfix">
                        <span>查询文献记录</span>
                        <!--   <el-button style="float: right; padding: 3px 0" type="text">添加</el-button>-->
                    </div>
                    <el-table :data="todoList" height="360" style="width: 100%" :cell-class-name="changeCellStyle">
                        <el-table-column
                            prop="operate"
                            label="查询使用关键词">
                        </el-table-column>
                        <el-table-column
                            prop="target"
                            label="论文目标区域">
                        </el-table-column>
                        <el-table-column
                            prop="operateNO"
                            label="第几次操作">
                        </el-table-column>
                        <el-table-column
                            prop="address"
                            label="操作地点">
                        </el-table-column>
                        <el-table-column
                            prop="streamNumber"
                            label="选中记录">
                        </el-table-column>
                        <el-table-column
                            prop="date"
                            label="日期">
                        </el-table-column>
                    </el-table>
                </el-card>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    import Schart from 'vue-schart';
    import bus from '../common/bus';
    import {getDate,dateToString} from '../../utils/Time'
    export default {
        name: 'dashboard',
        data() {
            return {
                name: localStorage.getItem('ms_username'),
                userrole: localStorage.getItem('userRole'),
                LastTime:"2019-05-12",
                todoList:
                    [{
                        operate: 'DNA',
                        target: "introduction",
                        operateNO: "200",
                        address: "无锡",
                        streamNumber: "112345326",
                        date: "2019-5-13 15:10:40"
                    },
                        {
                            operate: 'Health',
                            target: "introduction",
                            operateNO: "202",
                            address: "无锡",
                            streamNumber: "112345326",
                            date: "2019-5-13 15:10:40"
                        },
                        {
                            operate: 'RNA',
                            target: "discussion",
                            operateNO: "203",
                            address: "无锡",
                            streamNumber: "112345326",
                            date: "2019-5-13 15:10:40"
                        },
                        {
                            operate: 'Crisp',
                            target: "methods",
                            operateNO: "204",
                            address: "无锡",
                            streamNumber: "112345326",
                            date: "2019-5-13 15:10:40"
                        },

                    ],
                userList: [
                    {
                        name: "用户名",
                        value: "test"
                    },
                    {
                        name: "偏好",
                        value: "DNA,Machine learning"
                    }
                ]
            }
        },
        components: {
            Schart
        },
        computed: {
            role() {
                return this.userrole === '0' ? '超级管理员' : '普通用户';
            }
        },
        created() {
            this.handleListener();
            this.changeDate();
        },
        activated() {
            this.handleListener();
        },
        deactivated() {
            window.removeEventListener('resize', this.renderChart);
            bus.$off('collapse', this.handleBus);
        },
        //自动执行的一个方法
        mounted() {
            const uuid = localStorage.getItem('uuid');
            let data = {
                uuid: uuid
            };
            //获取用户信息
            this.httpdata(global.GETUUID, data);
        },
        methods: {
            changeDate() {
                const now = new Date().getTime();
            },
            handleListener() {
                bus.$on('collapse', this.handleBus);
                // 调用renderChart方法对图表进行重新渲染
                window.addEventListener('resize', this.renderChart)
            },
            handleBus(msg) {
                /* setTimeout(() => {
                     this.renderChart()
                 }, 300);*/
            },
            changeCellStyle({row, column, rowIndex, columnIndex}) {
                //第八列添加 red 类
                if (columnIndex === 1) {
                    return 'red'
                }
                //某一行其中的一个变量applies值如果大于0，并且在第六列，即确定一个具体的单元格需要确定行和列
                if (parseFloat(row.applies) > 0) {
                    return 'red'
                }
            },
            //查询用户信息
            httpdata(url, data) {
                let _thb = this;
                this.$post(url, data).then((response) => {
                    if (response.code === 200) {
                        //console.log(response);
                       /* this.$message({
                            message: '查询成功过',
                            type: 'success'
                        });*/
                        _thb.dataProcessing(response.data);

                    } else {
                        this.$message.error('失败');
                    }
                }, err => {
                    //console.log(err);
                });
            },

            //处理数据
            dataProcessing(data) {
                this.LastTime=this.Timestr(data.modifyDate);
                this.LastTime===""?this.LastTime="新用户":this.LastTime;
                this.userList = [
                    {
                        name: "用户名",
                        value: data.username
                    },
                    {
                        name: "偏好",
                        value: data.preference
                    }

                ]
            },
            //处理时间
            Timestr(str) {
                //console.log(str);
                return getDate(str);
            },
        }
    }

</script>


<style scoped>
    .el-row {
        margin-bottom: 20px;
    }

    .grid-content {
        display: flex;
        align-items: center;
        height: 100px;
    }

    .grid-cont-right {
        flex: 1;
        text-align: center;
        font-size: 14px;
        color: #999;
    }

    .grid-num {
        font-size: 30px;
        font-weight: bold;
    }

    .grid-con-icon {
        font-size: 50px;
        width: 100px;
        height: 100px;
        text-align: center;
        line-height: 100px;
        color: #fff;
    }

    .grid-con-1 .grid-con-icon {
        background: rgb(45, 140, 240);
    }

    .grid-con-1 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-2 .grid-con-icon {
        background: rgb(100, 213, 114);
    }

    .grid-con-2 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-3 .grid-con-icon {
        background: rgb(242, 94, 67);
    }

    .grid-con-3 .grid-num {
        color: rgb(242, 94, 67);
    }

    .user-info {
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #ccc;
        margin-bottom: 20px;
    }

    .user-avator {
        width: 120px;
        height: 120px;
        border-radius: 50%;
    }

    .user-info-cont {
        padding-left: 50px;
        flex: 1;
        font-size: 14px;
        color: #999;
    }

    .user-info-cont div:first-child {
        font-size: 30px;
        color: #222;
    }

    .user-info-list {
        font-size: 14px;
        color: #999;
        line-height: 25px;
    }

    .user-info-list span {
        margin-left: 70px;
    }

    .mgb20 {
        margin-bottom: 20px;
    }

    .todo-item {
        font-size: 14px;
    }

    .todo-item-del {
        text-decoration: line-through;
        color: #999;
    }

    .schart {
        width: 100%;
        height: 300px;
    }


</style>

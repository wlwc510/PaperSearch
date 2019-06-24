<template>
    <div class="sidebar">
        <el-menu class="sidebar-el-menu" :default-active="onRoutes" :collapse="collapse" background-color="#324157"
            text-color="#bfcbd9" active-text-color="#20a0ff" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index">
                        <template slot="title">
                            <i :class="item.icon"></i><span slot="title">{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-submenu v-if="subItem.subs" :index="subItem.index" :key="subItem.index">
                                <template slot="title">{{ subItem.title }}</template>
                                <el-menu-item v-for="(threeItem,i) in subItem.subs" :key="i" :index="threeItem.index">
                                    {{ threeItem.title }}
                                </el-menu-item>
                            </el-submenu>
                            <el-menu-item v-else :index="subItem.index" :key="subItem.index">
                                {{ subItem.title }}
                            </el-menu-item>
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i><span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
    import bus from '../common/bus';
    export default {
        data() {
            return {
                collapse: false,
                items: []
            }
        },
        mounted(){
            this.getitems();
        },
        methods: {
            getitems(){
                console.log("管理员");
                const userRole = localStorage.getItem('userRole');
                console.log(userRole);
                if(userRole==="0"){
                    this.items=[
                        {
                            icon: 'el-icon-lx-home',
                            index: 'dashboard',
                            title: '系统首页'
                        },
                        {
                            icon: 'el-icon-lx-search',
                            index: 'userTable',
                            title: '字符匹配查询'
                        },
                        {
                            icon: 'el-icon-lx-searchlist',
                            index: 'SemanticPTable',
                            title: '语义查询'
                        },
                        {
                            icon: 'el-icon-lx-tag',
                            index: 'CFPTable',
                            title: '协同过滤评分'
                        },
                        {
                            icon: 'el-icon-lx-attention',
                            index: 'UserItemTable',
                            title: '协同过滤结果'
                        }
//                        ,
//                        {
//                            icon: 'el-icon-pie-chart',
//                            index: 'charts',
//                            title: 'schart图表'
//                        }

                    ];
                }else{
                    this.items=[
                        {
                            icon: 'el-icon-lx-home',
                            index: 'dashboard',
                            title: '系统首页'
                        }/*,
                        {
                            icon: 'el-icon-lx-home',
                            index: 'userTable',
                            title: '用户表格'
                        }*/
                    ];
                }

            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        },
        created(){
            // 通过 Event Bus 进行组件间通信，来折叠侧边栏
            bus.$on('collapse', msg => {
                this.collapse = msg;
            })
        }
    }
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        left: 0;
        top: 70px;
        bottom:0;
        overflow-y: scroll;
    }
    .sidebar::-webkit-scrollbar{
        width: 0;
    }
    .sidebar-el-menu:not(.el-menu--collapse){
        width: 200px;
    }
    .sidebar > ul {
        height:100%;
    }
</style>

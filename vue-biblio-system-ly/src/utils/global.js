let urlhttp="http://";

/*本机*/
let  admin="127.0.0.1:8088/";
let  machine="127.0.0.1:5000"

//远程服务器
//let  admin="/www.wynlx.com/test/";

//服务器域名
let  host=urlhttp+admin;
let  hostmachine=urlhttp+machine

//登陆接口
global.LOGIN=host+"/user/userLogin";

//注册接口
global.REGISTERED=host+"/user/registered";

//获取原始列表；
global.GETUSERRAW=host+"/user/listraw";

//获取用户列表";
global.GETUSER=host+"/user/list";

//获取用户选择表
global.GETUSERITEM=host+"/user/useritemlist";

//获取用户列表
global.DELETEUSER=host+"/user/delete";

//更新用户
global.UPDATEUSER=host+"/user/update";

//新增用户
global.ADDUSER=host+"/user/add";

//根据唯一标识查询用户
global.GETUUID=host+"/user/getuuid";

//字符串匹配
global.QUERY=host+"/user/query";

//打分
global.RATING=hostmachine+"/Rating"

//语义查询
global.SearchPost=hostmachine+"/SearchPost"

//协同过滤
global.CollaborateFilter=hostmachine+"/CF_knearest"

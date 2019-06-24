package jiangnan.edu.controller;

//import com.github.pagehelper.PageHelper;
//import com.github.pagehelper.PageInfo;
//import jiangnan.edu.core.Result;
//import jiangnan.edu.core.ResultGenerator;
//import jiangnan.edu.dao.MongoDao;
//import com.github.pagehelper.PageInfo;
import com.github.pagehelper.PageInfo;
import com.miao.PageResult;
import com.miao.MongoPageHelper;
import io.swagger.annotations.ApiOperation;
import jiangnan.edu.core.Result;
import jiangnan.edu.core.ResultGenerator;
import jiangnan.edu.model.paper;
//import jiangnan.edu.model.QueryRecord;
import jiangnan.edu.model.test;
import jiangnan.edu.model.user;
import jiangnan.edu.model.user2record;
import jiangnan.edu.service.MongoDbService;
import org.springframework.beans.factory.ObjectFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.web.bind.annotation.*;
import tk.mybatis.mapper.entity.Condition;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/***
 * kaihu
 * 2019.5
 */
@RestController
@RequestMapping("/user")
public class BaseController {
    @Autowired
    private MongoDbService mongodbservice;
    @Resource
    private MongoPageHelper mongoPageHelper;


//    @PostMapping("/mongo/save")
//    public String saveObj(@RequestBody QueryRecord qr) {return mongodbservice.SaveObj(qr);}
    @GetMapping("/query")
    public Result<PageInfo<paper>> findOneByinput(@RequestParam String text,@RequestParam(defaultValue = "1") Integer page, @RequestParam(defaultValue = "10") Integer size){

        return mongodbservice.getPaperByText(text,page,size);
    }

////    一个请求列表的操作
//    @GetMapping("/mongo/user/list")
//    public list<test> findOneByinput(){return mongodbservice.getPapers();}

    /***
     * 所有mongodb中的文档对象
     * @param page
     * @param size
     * @return
     */
    @GetMapping("/list")
    public Result<PageInfo<paper>> findAll(@RequestParam(defaultValue = "0") Integer page, @RequestParam(defaultValue = "0") Integer size)
    {
//        PageHelper.startPage(page, size);
//        Query query = new Query(Criteria.where("_id").ne(null));
//        PageResult<paper> result=mongoPageHelper.pageQuery(query,paper.class,size,page);
//        List<paper> list = mongodbservice.findAll(page,size);
//        PageInfo<paper> pageInfo = new PageInfo<>(list);
////      log.info(String.valueOf(ResultGenerator.genSuccessResult(pageInfo)));
//        return ResultGenerator.genSuccessResult(result);
        List<paper> list = mongodbservice.findAll(page,size);
        Long total=mongodbservice.getCount();
        Integer pages=(total.intValue())/size+1;
        PageInfo<paper> pageResult = new PageInfo<>();
        pageResult.setTotal(total);
        pageResult.setPages(pages);
        pageResult.setPageSize(size);
        pageResult.setPageNum(page+1);
        pageResult.setList(list);
        return ResultGenerator.genSuccessResult(pageResult);

    }


    /***
     * 所有mongodb中的文档对象
     * @param page
     * @param size
     * @return
     */
    @GetMapping("/useritemlist")
    public Result<PageResult<user2record>> findAllu2r(@RequestParam(defaultValue = "1") Integer page, @RequestParam(defaultValue = "5") Integer size)
    {
        List<user2record> list = mongodbservice.findAllu2r(page,size);
        Long total=mongodbservice.getU2rCount();
        Integer pages=(total.intValue())/size+1;
        PageInfo<user2record> pageResult = new PageInfo<>();
        pageResult.setTotal(total);
        pageResult.setPages(pages);
        pageResult.setPageSize(size);
        pageResult.setPageNum(page);
        pageResult.setList(list);
        return ResultGenerator.genSuccessResult(pageResult);
//        pageResult.setTotal(total);
//        pageResult.setPages(pages);
//        pageResult.setPageSize(size);
//        pageResult.setPageNum(page);
//        pageResult.setList(list);
//        return ResultGenerator.genSuccessResult(pageResult);

    }

    @ApiOperation(value = "用户登陆", notes = "查询用户名密码是否正确")
    @PostMapping("/userLogin")
    public Result login(@RequestBody Map<String, Object> person) {
//        log.info((String) person.get("username"));
//        log.info((String) person.get("password"));
        String username = (String) person.get("username");
        String password = (String) person.get("password");
        if (username != null && !username.equals("")) {
            if (password != null && !password.equals("")) {
//                //注入User表
//                Condition condition = new Condition(user.class);
//                //根据条件查询
//                condition.createCriteria().andEqualTo("name", username).
//                        andEqualTo("password", password);
                List<user> users = mongodbservice.findByCondition(username,password);

                user mUser = new user();
                if (users != null && users.size() != 0) {
                    //获取一条用户数据
                    mUser = users.get(0);
                } else {
                    return ResultGenerator.genFailResult("用户不存在");
                }

                Map<String, Object> mPerson = new HashMap<>();
                mPerson.put("username", mUser.getName());
                //偏好
                mPerson.put("perferences", mUser.getPreferences());
                mPerson.put("uuid", mUser.getUuid());
                return ResultGenerator.genSuccessResult(mPerson);
            } else {
                return ResultGenerator.genFailResult("用户密码不能为空");
            }
        } else {
            return ResultGenerator.genFailResult("用户名字不能为空");
        }
    }


    @ApiOperation(value = "根据UUID查询用户", notes = "根据UUID查询用户")
    @PostMapping("/getuuid")
    public Result detail(@RequestBody Map<String, Object> person) {
        String uuid = (String) person.get("uuid");
        user user = mongodbservice.findBy("uuid",uuid);
        return ResultGenerator.genSuccessResult(user);
    }

    @ApiOperation(value="注册新用户",notes="注册新用户")
    @PostMapping("/registered")
    @CrossOrigin(origins = "*",maxAge = 3600)
    public Result registered(@RequestBody Map<String,Object> person){
        user nUser=new user();
        nUser.setName((String)person.get("username"));
        nUser.setPassword((String)person.get("password"));
        nUser.setPreferences((String)person.get("preference"));
        nUser.setUuid(UUID.randomUUID().toString());
        user n=mongodbservice.insertOne(nUser);
        if(null==n)
        {
            return ResultGenerator.genFailResult("已经存在该用户");
        }else
        {
            return ResultGenerator.genSuccessResult(n);
        }

    }


}

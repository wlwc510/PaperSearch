package jiangnan.edu.service;
import com.github.pagehelper.PageInfo;
import jiangnan.edu.core.PaperPagingAndSortingRepository;
import jiangnan.edu.core.Result;
import jiangnan.edu.core.ResultGenerator;
import jiangnan.edu.core.U2rPagingAndSortingRepository;
import jiangnan.edu.model.paper;
import jiangnan.edu.model.query_record;
import jiangnan.edu.model.user;
import jiangnan.edu.model.user2record;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Condition;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
//import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import static org.springframework.data.domain.PageRequest.of;
import static org.springframework.data.mongodb.core.query.Criteria.where;


/***
 * kaihu
 * 2019.5.20
 */

@Service
public class MongoDbService {
    private static final Logger logger= LoggerFactory.getLogger(MongoDbService.class);

    @Autowired
    private MongoTemplate mongoTemplate;

    @Resource
    private PaperPagingAndSortingRepository paperRepo;

    @Resource
    private U2rPagingAndSortingRepository u2rRepo;




    /***
     * 保存对象
     * @param record
     * @param return
     */
    public String SaveObj(query_record record)
    {
        Timestamp time1 = new Timestamp(new Date().getTime());
        record.setCreateTime(time1);
        record.setUpadateTime(time1);
        mongoTemplate.save(record);
        return "成功保存";
    }

    public long getCount(){
        Query query = new Query(where("_id").ne(null));
//        Query query = new Query(Criteria.where("_id").ne(null));
        return mongoTemplate.count(query,paper.class);
    }

    public long getU2rCount(){
        Query query = new Query(where("_id").ne(null));
//        Query query = new Query(Criteria.where("_id").ne(null));
        return mongoTemplate.count(query,user2record.class);
    }

    /***
     * 根据输入进行查询
     * @param input
     * @param return
     */
    public Result<PageInfo<paper>> getPaperByText(String input,Integer pageNo,Integer pageSize)
    {
        logger.info("-------------->[MongoDB find start]");
        String[] input_list=input.split(" ");
        Criteria cr=new Criteria();
        List<Criteria> Clist=new ArrayList<>();
        int length=input_list.length;
        if(length>0)
        {
            for (int i=0;i<length;i++)
            {
                Clist.add(where("introduction").regex(".*"+input_list[i].trim()+".*"));
            }

        }
        cr.orOperator(Clist.toArray(new Criteria[Clist.size()]));
        Query query=new Query(cr);
        Long count=mongoTemplate.count(query,paper.class);
        Pageable pageable=PageRequest.of(pageNo-1,pageSize);
        query.with(pageable);
        List<paper> list=mongoTemplate.find(query,paper.class);
        Long total=count;
        //默认size=10 page=1
        Integer size=10;
        Integer pages=(total.intValue())/size+1;
        PageInfo<paper> pageResult = new PageInfo<>();
        pageResult.setTotal(total);
        pageResult.setPages(pages);
        pageResult.setPageSize(size);
        pageResult.setPageNum(1);
        pageResult.setList(list);
        return ResultGenerator.genSuccessResult(pageResult);

    }

    /***
     * 返回初始列表
     * @return
     */
    public List<paper> findAll(Integer pageNo, Integer pageSize)
    {
            Pageable pageable=PageRequest.of(pageNo-1,pageSize);
            Page<paper> page=paperRepo.findAll(pageable);
            return  page.getContent();

    }

    public List<user2record> findAllu2r(Integer pageNo, Integer pageSize)
    {
        Pageable pageable=PageRequest.of(pageNo-1,pageSize);
        Page<user2record> page=u2rRepo.findAll(pageable);
        return  page.getContent();
    }


    /***
     * 查询相应用户
     * @param condition
     * @return
     */
    public List<user> findByCondition(String username, String password)
    {
        Criteria criteria=new Criteria();
        criteria.and("name").is(username);
        criteria.and("password").is(password);
        Query query=new Query(criteria);
        return mongoTemplate.find(query,user.class);
    }

    /***
     *
     * @param key
     * @param input
     * @return
     */
    public user findBy(String key, String input)
    {
        Criteria criteria=new Criteria();
        where("uuid").is(input);
        Query query=new Query(criteria);
        return mongoTemplate.findOne(query, user.class);
    }

    public user insertOne(user nUser)
    {

        Criteria c=Criteria.where("name").is(nUser.getName());
        Query query=new Query(c);

        if(mongoTemplate.exists(query,user.class))
        {
            return null;
        }else
        {
//            mongoTemplate.insert(nUser);
            mongoTemplate.save(nUser);
            return nUser;
        }
    }


}

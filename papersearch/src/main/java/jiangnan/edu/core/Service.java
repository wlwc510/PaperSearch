package jiangnan.edu.core;

import org.apache.ibatis.exceptions.TooManyResultsException;
import tk.mybatis.mapper.entity.Condition;

import java.util.List;

/**
 * Service 层 基础接口，其他Service 接口 请继承该接口
 * @author 阳斌
 */
public interface Service<T> {
    /**
     * 持久化
     * @param model 传入的对象
     * @return 返回ID
     */
    Integer save(T model);

    /**
     * 批量插入
     * @param models 对象集合
     */
    void save(List<T> models);

    /**
     * 通过主鍵刪除
     * @param id 主键
     */
    void deleteById(Integer id);

    /**
     *批量刪除 eg：ids -> “1,2,3,4”
     * @param ids id集合
     */
    void deleteByIds(String ids);

    /**
     * /更新
     * @param model 对象
     */
    void update(T model);

    /**
     * //通过ID查找
     * @param id 传入id
     * @return 返回
     */
    T findById(Integer id);

    /**
     *  //通过Model中某个成员变量名称（非数据表中column的名称）查找,value需符合unique约束
     * @param fieldName 条件
     * @param value  值
     * @return  查询结果
     * @throws TooManyResultsException 异常
     */
    T findBy(String fieldName, Object value) throws TooManyResultsException;

    /**
     * 通过多个ID查找//eg：ids -> “1,2,3,4”
     * @param ids id结果集
     * @return 集合
     */
    List<T> findByIds(String ids);

    /**
     *  根据条件查找
     * @param condition 查询条件
     * @return 返回结果
     */
    List<T> findByCondition(Condition condition);

    /**
     *  获取所有
     * @return 所有集合
     */
    List<T> findAll();
}

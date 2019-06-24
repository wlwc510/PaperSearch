package jiangnan.edu.core;

import jiangnan.edu.model.paper;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.repository.PagingAndSortingRepository;

import java.util.List;

/***
 * PagingAndSortingRepository<paper, Integer>
 *
 */
public interface PaperPagingAndSortingRepository extends PagingAndSortingRepository<paper, Integer> {

//    @Query()
//    public List<paper> findpapersbyCritira(Pageable p, Criteria c);


}

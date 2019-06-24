package jiangnan.edu.model;


import java.sql.Timestamp;

public class query_record {
    private String Id;
    private String keyword;
    private String text;
    private String paperId;
    private String userId;
    private Timestamp createTime;
    private Timestamp upadateTime;

    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getPaperId() {
        return paperId;
    }

    public void setPaperId(String paperId) {
        this.paperId = paperId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getId() {
        return Id;
    }

    public void setId(String id) {
        Id = id;
    }

    public Timestamp getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Timestamp createTime) {
        this.createTime = createTime;
    }

    public Timestamp getUpadateTime() {
        return upadateTime;
    }

    public void setUpadateTime(Timestamp upadateTime) {
        this.upadateTime = upadateTime;
    }
}

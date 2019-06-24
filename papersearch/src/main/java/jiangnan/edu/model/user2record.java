package jiangnan.edu.model;

import org.springframework.data.mongodb.core.mapping.Field;

public class user2record {
    @Field("_id")
    private String Id;
    @Field("paperid")
    private String paperid;
    @Field("uuid")
    private String uuid;
    @Field("rating")
    private float rating;


    public String getId() {
        return Id;
    }

    public void setId(String id) {
        Id = id;
    }

    public String getPaperid() {
        return paperid;
    }

    public void setPaperid(String paperid) {
        this.paperid = paperid;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }

    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }
}

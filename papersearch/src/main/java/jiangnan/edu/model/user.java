package jiangnan.edu.model;

import org.springframework.data.mongodb.core.mapping.Field;

public class user {
    @Field("_id")
    private String Id;
    @Field("name")
    private String Name;
    @Field("preference")
    private String preferences;
    private String password;
    private String uuid;

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public String getPreferences() {
        return preferences;
    }

    public void setPreferences(String preferences) {
        this.preferences = preferences;
    }

    public String getId() {
        return Id;
    }

    public void setId(String id) {
        Id = id;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
}

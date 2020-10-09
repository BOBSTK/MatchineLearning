package com.stk.pojo;


import java.util.Date;


//员工
public class Employee {
    private Integer id;
    private String lastName;
    private String email;
    private Integer gendar;  // 0 - 女  1 - 男

    private Department department;
    private Date birth;

    public Employee() {
    }

    public Employee(Integer id, String lastName, String email, Integer gendar, Department department) {
        this.id = id;
        this.lastName = lastName;
        this.email = email;
        this.gendar = gendar;
        this.department = department;
        this.birth = new Date();
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Integer getGendar() {
        return gendar;
    }

    public void setGendar(Integer gendar) {
        this.gendar = gendar;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    public Date getBirth() {
        return birth;
    }

    public void setBirth(Date birth) {
        this.birth = birth;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "id=" + id +
                ", lastName='" + lastName + '\'' +
                ", email='" + email + '\'' +
                ", gendar=" + gendar +
                ", department=" + department +
                ", birth=" + birth +
                '}';
    }
}

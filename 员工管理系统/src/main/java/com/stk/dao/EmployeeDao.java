package com.stk.dao;

import com.stk.pojo.Department;
import com.stk.pojo.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

@Repository
//员工dao
public class EmployeeDao {

    //模拟数据库中得数据
    private static Map<Integer, Employee> employees = null;

    //员工有所属得部门
    @Autowired
    private DepartmentDao departmentDao;

        static {
            employees = new HashMap<Integer, Employee>(); //创建一个部门表
            employees.put(101,new Employee(1001,"AA","72323232@qq.com",0,new Department(101,"教学部")));
            employees.put(102,new Employee(1001,"BB","72323232@qq.com",1,new Department(102,"市场部")));
            employees.put(103,new Employee(1001,"CC","72323232@qq.com",0,new Department(103,"教研部")));
            employees.put(104,new Employee(1001,"DD","72323232@qq.com",1,new Department(104,"运营部")));
            employees.put(105,new Employee(1001,"EE","72323232@qq.com",1,new Department(105,"后勤部")));
        }
        //主键自增
        private static Integer initId = 1006;
        //增加一个员工
        public void save(Employee employee){
            if(employee.getId() == null){
                employee.setId(initId++);
            }
            employee.setDepartment(departmentDao.getDepartmentById(employee.getDepartment().getId()));
            employees.put(employee.getId(),employee);
        }

        //查询全部员工信息
        public Collection<Employee> getAll(){
            return employees.values();
        }

        //通过id查询员工信息
        public Employee getEmployeeById(Integer id){
            return employees.get(id);
        }

        //通过id删除员工
        public void deleteById(Integer id){
            employees.remove(id);
        }

}

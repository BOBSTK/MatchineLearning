# Mybatis

https://mybatis.org/mybatis-3/index.html

## 1、第一个Mybatis程序

思路：搭建环境-->导入Mybatis-->编写代码-->测试

### 1.1搭建环境

1. 搭建数据库
2. 新建maven项目
3. 删除src目录
4. 导入maven依赖

### 1.2创建一个模块

1. 编写mybatis核心配置文件

   ```
   <configuration>
       <environments default="development">
           <environment id="development">
               <transactionManager type="JDBC"/>
               <dataSource type="POOLED">
                   <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                   <property name="url" value="jdbc:mysql://127.0.0.1:3306/javaee?useSSL=true&amp;useUnicode=true&amp;characterEncoding=UTF-8&amp;serverTimezone=UTC"/>
                   <property name="username" value="root"/>
                   <property name="password" value="123456"/>
               </dataSource>
           </environment>
       </environments>
   
       <!--每一个Mapper.XML都需要在Mybatis核心文件中注册 -->
       <mappers>
           <mapper resource="StudentMapper.xml"/>
       </mappers>
   </configuration>
   ```

   

2. 编写mybatis工具类

   ```java
   package com.dlut.bc.utils;
   
   import org.apache.ibatis.io.Resources;
   import org.apache.ibatis.session.SqlSession;
   import org.apache.ibatis.session.SqlSessionFactory;
   import org.apache.ibatis.session.SqlSessionFactoryBuilder;
   
   import java.io.IOException;
   import java.io.InputStream;
   
   //sqlSessionFactory
   public class MybatisUtils {
       private static SqlSessionFactory sqlSessionFactory;
   
       static {
           try {
               //获取sqlSessionFactory对象
               String resource = "mybatis-config.xml";
               InputStream inputStream= Resources.getResourceAsStream(resource);
               sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   
       /*从SqlSessionFactory中获得 SqlSession 的实例
       * SqlSession 提供了在数据库执行 SQL 命令所需的所有方法。
       * 你可以通过 SqlSession 实例来直接执行已映射的 SQL 语句。
       * */
       public static SqlSession getSqlSession(){
   
           return sqlSessionFactory.openSession();
       };
   
   }
   
   ```

   

3. 编写代码

   - 实体类

   -  Dao接口

   -  接口实现类

     接口实现类由原来的DaoImp转变为一个Mapper配置文件  

4. 测试

   注意点：

   org.apache.ibatis.binding.BindingException: Type interface com.dlut.bc.dao.StudentDao is not known to the MapperRegistry. 核心配置文件

   **maven导出资源问题**

   

## 2、CRUD

选择，查询语句

```xml
<select id="getStudentList" resultType="com.dlut.bc.pojo.Student">
    select * from javaee.student;
 </select>
```

- id:对应的namespace中的方法名
- resultType：Sql语句执行的返回值
- parameterType: 参数类型

**增删改需要提交事务**

​    sqlSession.commit();

## 3、万能的Map

Map传递参数，直接在Sql中取初key即可。

## 4、动态SQL

### 4.1什么是动态SQL

  动态SQL就是根据不同的条件生成不同的SQL语句

- if
- choose(when, otherwise)
- trim(where,set)
- foreach

### 4.2搭建环境


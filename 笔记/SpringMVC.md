# SpringMVC

https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html

## 1、什么是MVC

- MVC：模型(dao,service) 视图(jsp) 控制器(servlet)，是一种软件设计规范。
- 将**业务逻辑**、**数据**、**显示**分离的方法来组织代码。

1. 用户发请求
2. Servlet接收请求数据，并调用对应的**业务逻辑**方法
3. 业务处理完毕，返回更新后的数据给servlet
4. servlet转向到JSP，由JSP来**渲染页面**
5. 响应给前端更新后的页面

职责分析：

**Controller(Servlet)：控制器**

1. 取得表单数据
2. 调用业务逻辑
3. 转向指定的页面

 **Model：模型**

1. 业务逻辑
2. 保存数据的状态

  **View：视图**

   显示页面

## 2、回顾Servlet

### 创建项目

创建一个maven项目

导入依赖

```xml
       <!--junit-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>

        <!--spring -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.1.9.RELEASE</version>
        </dependency>

        <!--servlet -JSP -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>2.5</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>jsp-api</artifactId>
            <version>2.2</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
            <version>1.2</version>
        </dependency>
```

添加框架支持（变成web项目）

1. 编写servlet类，处理用户的请求

2. 去web.xml下配置servlet

   ```xml
    <servlet>
           <servlet-name>hello</servlet-name>
           <servlet-class>com.bc.servlet.HelloServlet</servlet-class>
       </servlet>
       <servlet-mapping>
           <servlet-name>hello</servlet-name>
           <url-pattern>/hello</url-pattern>
       </servlet-mapping>
   
       <!--超时-->
       <!--session-config-->
           <!--session-timeout>15</session-timeout-->
       <!--/session-config-->
   
       <!--欢迎页面，默认为index.jsp-->
       <!--welcome-file-list-->
           <!--welcome-file>index.jsp</welcome-file-->
       <!--/welcome-file-list-->
   ```

3. 写一个表单jsp提交请求

   ```javascript
   <form action="/hello" method="post">
       <input type="text" name="method">
       <input type="submit">
   </form>
   ```

4. 配置TomCat

## 3、SpringMVC

### 3.1 什么是SpringMVC

Spring MVC是Spring Framework的一部分，是基于java实现MVC的**轻量级Web框架**。

### 3.2 为什么要用SpringMVC

优点：

- 轻量级，简单易学
- 高效，**基于请求响应**的MVC框架
- 与Spring兼容好
- 约定优于配置
- 功能强大
- 简介灵活

### 3.3 第一个SpringMVC项目

1. 创建maven项目

2. 添加框架支持（变成web项目）

3. 在web.xml中注册SpringMVC

   ```xml
    <!-- 注册DispatcherServlet-->
            <servlet>
                <servlet-name>springmvc</servlet-name>
                <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
                <!-- 关联一个springmvc的配置文件：【servlet-name】-servlet.xml-->
                <init-param>
                    <param-name>contextConfigLocation</param-name>
                    <param-value>classpath:springmvc-servlet.xml</param-value>
                </init-param>
                <!-- 启动级别-1-->
                <load-on-startup>1</load-on-startup>
            </servlet>
   
            <!-- /  匹配所有的请求：（不包括.jsp）-->
            <!-- /* 匹配所有的请求：（包括.jsp）-->
            <servlet-mapping>
                <servlet-name>springmvc</servlet-name>
                <url-pattern>/</url-pattern>
            </servlet-mapping>
   ```

   

4. 编写SpringMVC配置文件

   ```xml
    <!-- 处理映射器-->
       <bean class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>
       <!-- 处理器适配器-->
       <bean class="org.springframework.web.servlet.mvc.SimpleControllerHandlerAdapter"/>
   
       <!-- 视图解析器：ModelAndView-->
       <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver" id="internalResourceViewResolver">
           <!-- 前缀-->
           <property name="prefix" value="/WEB-INF/jsp/"/>
           <!-- 后缀-->
           <property name="suffix" value=".jsp"/>
       </bean>
   
       <!-- Handler-->
       <bean id="/hello" class="com.bc.controller.HelloController"/>
   ```

   

5. 编写Controller

   ```java
   import org.springframework.web.servlet.ModelAndView;
   import org.springframework.web.servlet.mvc.Controller;
   
   import javax.servlet.http.HttpServletRequest;
   import javax.servlet.http.HttpServletResponse;
   
   //先导入Controller接口
   public class HelloController implements Controller {
       public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception{
           //ModelAndView
           ModelAndView mv = new ModelAndView();
   
           //调用业务层
           
           //封装对象，放在ModelAndView中
           mv.addObject("msg","HelloSpringMVC!");
           //封装要跳转的视图，放在放在ModelAndView中中
           mv.setViewName("hello");//:/WEB-INF/jsp/hello.jsp
           return mv;
       }
   }
   
   ```

### 3.4 执行流程分析

![image-20200613024538361](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200613024538361.png)

1. DispatcherServlet表示前端控制器(本质上是一个Servlet)，接收并拦截用户的请求；
2. HandlerMapping为处理器映射，由DispatcherServlet调用，根据请求url查找Handler；
3. HandlerExecution表示具体的Handler，如3.3中的hello；
4. HandlerExecution将解析的信息返回给DispatcherServlet；
5. HandlerAdapter表示处理器适配器，按照特定的规则执行Handler；
6. Handler让具体的Controller执行，如3.3中的HelloController；
7. Controller将具体的执行信息返回给HandlerAdapter，如ModelAndView；
8. HandlerAdapter将视图逻辑名或模型传递给DispatcherServlet；
9. 视图解析器(ViewResolver)解析逻辑视图名
10. 逻辑视图名传回DispatcherServlet
11. DispatcherServlet调用具体视图；
12. 最终视图呈现给用户

## 4、使用注解开发SpringMVC

1. SpringMVC配置文件

   ```xml
   <?xml version="1.0" encoding="UTF8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:context="http://www.springframework.org/schema/context"
          xmlns:mvc="http://www.springframework.org/schema/mvc"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
           https://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">
   
   
   
       <!-- 自动扫描包，让指定包下的注解生效，由IOC容器统一管理-->
       <context:component-scan base-package="com.bc.controller"/>
   
       <!-- 让SpringMVC不再处理静态资源 .css .js .html .mp3 .mp4等-->
       <mvc:default-servlet-handler/>
   
       <!-- 自动完成处理器适配器和处理映射器的注入-->
       <mvc:annotation-driven/>
   
   
       <!--JSON乱码配置问题-->
       <mvc:annotation-driven>
           <mvc:message-converters register-defaults="true">
               <bean class="org.springframework.http.converter.StringHttpMessageConverter">
                   <constructor-arg value="UTF-8"/>
               </bean>
               <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter">
                   <property name="objectMapper">
                       <bean class="org.springframework.http.converter.json.Jackson2ObjectMapperFactoryBean">
                           <property name="failOnEmptyBeans" value="false"/>
                       </bean>
                   </property>
               </bean>
           </mvc:message-converters>
       </mvc:annotation-driven>
   
   
   
       <!-- 视图解析器：ModelAndView
       1.获取了ModelAndView的数据
       2.解析ModelAndView的视图名字
       3.拼接视图名字，找到对应的视图
       4.将数据渲染到这个视图上
       -->
       <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver" id="internalResourceViewResolver">
           <!-- 前缀-->
           <property name="prefix" value="/WEB-INF/jsp/"/>
           <!-- 后缀-->
           <property name="suffix" value=".jsp"/>
       </bean>
       
   
   
   
   
   
   </beans>
   ```

   

2. 创建HelloController，使用@Controller注解

   ```java
   @Controller //让Spring IOC容器初始化时自动扫描到
   public class HelloController {
   
       //真实访问地址：项目名/HelloController/hello
       @RequestMapping ("/hello")
       public String hello(Model model){
           //封装数据
           model.addAttribute("msg","Hello, SpringMVCAnnotation!");
           return "hello"; //会被视图解析器处理 //WEB-INF/hello.jsp
       }
   
   
   }
   ```

   @Component       组件

   @Service               service

   @Controller          controller

   @Repository         dao

​       

## 5、RestFul风格

  RestFul就是一个**资源定位**及**资源操作**的风格。基于这个风格设计的软件可以更简洁，更有层次，**更易于实现缓存**等机制。

  @PathVariable

  @GetMapping   = @RequestMapping(method = RequestMethod.GET)

  @PostMapping

  @PutMapping

  @DeleteMapping

  @PatchMapping

##   6、转发和重定向

### 6.1 ModelAndView

  根据view的名称，和视图解析器ViewResolver跳到指定的页面。

  页面：{前缀} + viewName + {后缀}

  对应的Controller类

### 6.2 ServletAPI

1. 通过HttpServletResponse进行输出
2. 通过HttpServletResponse实现重定向
3. 通过HttpServletResponse实现转发

### 6.3 SpringMVC

  通过SpringMVC来实现转发和重定向 - 无需视图解析器

```java
@RequestMapping ("/test")
public String Test(Model model){
    model.addAttribute("msg","TestController");
    return "WEB-INF/jsp/hello.jsp";
}
    return "forward:WEB-INF/jsp/hello.jsp";
    return "redirect:WEB-INF/jsp/hello.jsp";

```

## 7、SpringMVC数据处理

接收数据：url?para=value

接收对象：假设传递的是一个对象，会匹配对象中的字段名，如果名字一致则ok

提交数据：Model, Moedel Map, ModelAndView

## 8、乱码问题

在SpringMVC配置过滤器

```xml
 <!--配置SpringMVC的过滤器-->
<filter>
        <filter-name>encoding</filter-name>
        <filter-class>com.bc.filter.EncodingFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>encoding</filter-name>
        <url-pattern>/</url-pattern>
    </filter-mapping>
```

## 9、JSON

### 9.1 为什么

  前后端分离：

- 后端部署后端，提供接口，提供数据
- JSON
- 前端独立部署，负责渲染后端的数据

### 9.2 是什么

- JSON(JavaScript Object Notation, JS对象标记)是一种轻量级的**数据交换格式**，目前使用得特别广泛；
- 采用完全独立于编程语言的**文本格式**来存储和表示数据；
- 简洁清晰；
- 易于阅读，易于机器解析和生产，有效地**提升网络传输效率**。

  使用JSON键值对来保存JavaScript对象，键名在前，使用冒号:分隔，然后紧接着值。

- 方括号保存数组
- 花括号保存对象

将js对象转为json对象

```javascript
var json = JSON.stringify(user);
```

将json对象转为js对象

```javascript
var obj = JSON.parse(json)
```

### 9.3 Jackson

```xml
 <!--JSON乱码配置问题-->
    <mvc:annotation-driven>
        <mvc:message-converters register-defaults="true">
            <bean class="org.springframework.http.converter.StringHttpMessageConverter">
                <constructor-arg value="UTF-8"/>
            </bean>
            <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter">
                <property name="objectMapper">
                    <bean class="org.springframework.http.converter.json.Jackson2ObjectMapperFactoryBean">
                        <property name="failOnEmptyBeans" value="false"/>
                    </bean>
                </property>
            </bean>
        </mvc:message-converters>
    </mvc:annotation-driven>
```

## 10、整合SSM项目

### 10.1 Mybatis层

新建maven项目，导入依赖

```xml
 <dependencies>
        <!--mysql -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.20</version>
        </dependency>



        <!--数据库连接池-->
        <dependency>
            <groupId>com.mchange</groupId>
            <artifactId>c3p0</artifactId>
            <version>0.9.5.2</version>
        </dependency>

        <!--servlet -JSP -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>2.5</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>jsp-api</artifactId>
            <version>2.2</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
            <version>1.2</version>
        </dependency>

        <!--mybatis -->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.5</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
            <version>2.0.2</version>
        </dependency>

        <!--spring -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.1.9.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>5.1.9.RELEASE</version>
        </dependency>


        <!--junit-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
     
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.16.10</version>
        </dependency>

    </dependencies>

    <!--在build中配置resources,来防止我没资源导出失败的问题-->
    <build>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>true</filtering>
            </resource>
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>
```

1. 关联数据库：配置mybatis-config.xml
2. 写StudentMapper接口和StudentMapper.xml

### 10.2 Spring层

- 整合dao层和service

- 配置spring-dao.xml

  ```xml
  <?xml version="1.0" encoding="UTF8"?>
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:context="http://www.springframework.org/schema/context"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
          https://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">
  
      <!--关联数据库配置文件-->
      <context:property-placeholder location="classpath:database.properties"/>
  
      <!--连接池
      dpcp：半自动
      c3p0：自动化（自动化的加载配置文件，并且可以自动设置到对象中）
      druid
      hikari
      -->
      <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
          <property name="driverClass" value="${jdbc.driver}"/>
          <property name="jdbcUrl" value="${jbdc.url}}"/>
          <property name="user" value="${jdbc.username}"/>
          <property name="password" value="${jdbc.password}"/>
  
          <!--c3p0私有属性-->
          <property name="maxPoolSize" value="30"/>
          <property name="minPoolSize" value="10"/>
          <property name="autoCommitOnClose" value="false"/>
          <property name="checkoutTimeout" value="10000"/>
          <property name="acquireRetryAttempts" value="2"/>
      </bean>
  
      <!--sqlSessionFactory-->
      <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
          <property name="dataSource" ref="dataSource"/>
          <property name="configLocation" value="classpath:mybatis-config.xml"/>
      </bean>
  
      <!--配置dao接口扫描包，动态实现了Dao接口可以注入到Spring容器中-->
      <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
          <!--注入 sqlSessionFactory-->
          <property name="sqlSessionFactoryBeanName" value="sqlSessionFactory"/>
          <!--要扫描的mapper包-->
          <property name="basePackage" value="com.bc.mapper"/>
      </bean>
  
  
  
  </beans>
  
  
  <!--datasource-->
      <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
          <property name="driverClassName" value="com.mysql.cj.jdbc.Driver"/>
          <property name="url" value="dbc:mysql://127.0.0.1:3306/javaee?useSSL=true&amp;useUnicode=true&amp;characterEncoding=UTF-8&amp;serverTimezone=UTC"/>
          <property name="username" value="$root"/>
          <property name="password" value="$123456"/>
      </bean>
  ```

  

- spring-service.xml

  ```xml
  <?xml version="1.0" encoding="UTF8"?>
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:context="http://www.springframework.org/schema/context"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
          https://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">
      <!--扫描service的包-->
      <context:component-scan base-package="com.bc.service"/>
  
      <!--将所有的业务类注入到Spring-->
      <bean id="StudentServiceImpl" class="com.bc.service.StudentServiceImpl">
          <property name="studentMapper" ref="studentMapper"/>
      </bean>
  
      <!--声明事务配置-->
      <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
          <!--注入数据源-->
          <property name="dataSource" ref="dataSource"/>
      </bean>
  
  
  </beans>
  ```

### 10.3 SpringMVC层

- 配置web.xml

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
           version="4.0">
      <!-- 注册DispatcherServlet-->
      <servlet>
          <servlet-name>springmvc</servlet-name>
          <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
          <!-- 关联一个springmvc的配置文件：【servlet-name】-servlet.xml-->
          <init-param>
              <param-name>contextConfigLocation</param-name>
              <param-value>classpath:spring-mvc.xml</param-value>
          </init-param>
          <!-- 启动级别-1-->
          <load-on-startup>1</load-on-startup>
      </servlet>
  
      <!-- /  匹配所有的请求：（不包括.jsp）-->
      <!-- /* 匹配所有的请求：（包括.jsp）-->
      <servlet-mapping>
          <servlet-name>springmvc</servlet-name>
          <url-pattern>/</url-pattern>
      </servlet-mapping>
  
      <!--乱码过滤-->
      <filter>
          <filter-name>encodingFilter</filter-name>
          <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
          <init-param>
              <param-name>encoding</param-name>
              <param-value>utf-8</param-value>
          </init-param>
      </filter>
      <filter-mapping>
          <filter-name>encodingFilter</filter-name>
          <url-pattern>/*</url-pattern>
      </filter-mapping>
  
      <!--Session-->
      <session-config>
          <session-timeout>15</session-timeout>
      </session-config>
  
  
  </web-app>
  ```

  

- s
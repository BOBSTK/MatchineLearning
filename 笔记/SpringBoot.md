# SpringBoot

## 一、第一个SpringBoot程序

1. 使用IDEA创建一个空的SpringBoot项目

2. 导入依赖

   ```xml
    <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
   ```

3. 写`HelloController`

## 二、运行原理

### 2.1 pom.xml

### 2.2 主启动类

> SpringApplication

- 推断应用的类型是普通的项目还是Web项目
- 查找并加载所有可用初始化器 ， 设置到initializers属性中
- 找出所有的应用程序监听器，设置到listeners属性中
- 推断并设置main方法的定义类，找到运行的**主类**

## 三、yaml语法

> 是什么

- SpringBoot 全局配置文件
- 修改SpringBoot自动配置的默认值
- **标记语言**，以数据为中心

> 语法结构

`key: vlue`

1、空格不能省略

2、以缩进来控制层级关系，只要是左边对齐的一列数据都是同一个层级的。

3、属性和值的大小写都是十分敏感的。

**对象、Map（键值对）**

```
#对象、Map格式
k: 
    v1:
    v2:
```

在下一行来写对象的属性和值得关系，注意缩进；比如：

```
student:
    name: qinjiang
    age: 3
```

行内写法

```
student: {name: qinjiang,age: 3}
```

**数组（ List、set ）**

用 - 值表示数组中的一个元素,比如：

```
pets:
 - cat
 - dog
 - pig
```

行内写法

```
pets: [cat,dog,pig]
```

**修改SpringBoot的默认端口号**

配置文件中添加，端口号的参数，就可以切换端口；

```
server:
  port: 8082
```

### 3.1 直接给实体类赋值

- 在yaml中配置类

  ```yaml
  person:
    name: BC${random.uuid} # 随机uuid
    age: ${random.int}   # 随机int
    happy: false
    birth: 2019/11/02
    maps: {k1: v1,k2: v2}
    lists:
      - code
      - music
      - girl
    dog:
      name: ${person.hello:hello}_旺财  #默认值
      age: 3
  ```

- 在实体类中注解

  ```java
  @ConfigurationProperties(prefix = "person") //将实体类和yaml中的配置类绑定
  /*
  将配置文件中配置的每一个属性的值，映射到这个组件中；
  告诉SpringBoot将本类中的所有属性和配置文件中相关的配置进行绑定
  参数 prefix = “person” : 将配置文件中的person下面的所有属性一一对应
   */
  ```

- 需要导入一个依赖，不影响程序运行

  ```xml
  <!-- 导入配置文件处理器，配置文件进行绑定就会有提示，需要重启-->
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-configuration-processor</artifactId>
              <optional>true</optional>
          </dependency>
  ```

- 加载指定的配置文件

  - **@PropertySource ：**加载指定的配置文件； 

    `@PropertySource(value = "classpath:person.properties")`

  - **@configurationProperties**：默认从全局配置文件中获取值；

![img](E:\Code\MachineLearning\MatchineLearning\笔记\SpringBoot\1418974-20200310172022780-374285033.png)

### 3.2 JSR303数据校验

> 是什么

- 在字段是增加一层**过滤器**验证 ， 可以保证数据的**合法性**

> 怎么做

- 导入依赖

  ```xml
  <!-- 导入数据验证-->
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-validation</artifactId>
          </dependency>
  ```

- 实体类注解

  `@Validated //数据校验`

  `@Email()`

> 常见参数

```java
@NotNull(message="名字不能为空")
private String userName;
@Max(value=120,message="年龄最大不能查过120")
private int age;
@Email(message="邮箱格式错误")
private String email;

空检查
@Null       验证对象是否为null
@NotNull    验证对象是否不为null, 无法查检长度为0的字符串
@NotBlank   检查约束字符串是不是Null还有被Trim的长度是否大于0,只对字符串,且会去掉前后空格.
@NotEmpty   检查约束元素是否为NULL或者是EMPTY.
    
Booelan检查
@AssertTrue     验证 Boolean 对象是否为 true  
@AssertFalse    验证 Boolean 对象是否为 false  
    
长度检查
@Size(min=, max=) 验证对象（Array,Collection,Map,String）长度是否在给定的范围之内  
@Length(min=, max=) string is between min and max included.

日期检查
@Past       验证 Date 和 Calendar 对象是否在当前时间之前  
@Future     验证 Date 和 Calendar 对象是否在当前时间之后  
@Pattern    验证 String 对象是否符合正则表达式的规则

.......等等
除此以外，我们还可以自定义一些数据校验规则
```

### 3.3 多环境配置

> 为什么

- 通过激活不同的环境版本，实现快速**切换环境**

> 是什么

- 优先级

  - 优先级**由高到低**，高优先级的配置会**覆盖**低优先级的配置

  ```txt
  优先级1：项目路径下的config文件夹配置文件
  优先级2：项目路径下配置文件
  优先级3：资源路径下的config文件夹配置文件
  优先级4：资源路径下配置文件
  ```

- 如果yml和properties同时都配置了端口，并且没有激活其他环境 ， **默认会使用properties配置文件的**

> 怎么做

```yaml
server:
  port: 8081

#指定环境
spring:
  profiles:
    active: dev
---
server:
  port: 8082
spring:
  profiles: dev
---
server:
  port: 8083
spring:
  profiles: test

```



##  四、注解开发

@Component       组件

@Service               service

@Controller          controller

@Repository         dao



> 属性赋值

- `@Value("${value}")` 
  - 环境变量赋值
    - 从**配置文件**读取值 `@Value("${savePath}")`  
- `@Autowired`
  - 按类型**装配依赖对象**, 给指定的字段或方法注入所需的外部资源

## 五、SpringBoot Web 开发

> SpringBoot 配置

- **xxxxAutoConfigurartion：自动配置类；**给容器中添加组件
- **xxxxProperties:封装配置文件中相关属性；**

> 要解决的问题

- 导入静态资源
- 首页
- jsp，模板引擎Thymeleaf
- 装配扩展SpringMVC
- 增删改查
- 拦截器
- 国际化

### 5.1 加载静态资源

> 添加资源处理器

```java
 public void addResourceHandlers(ResourceHandlerRegistry registry) {
            if (!this.resourceProperties.isAddMappings()) {
                logger.debug("Default resource handling disabled");
            } else {
                Duration cachePeriod = this.resourceProperties.getCache().getPeriod();
                CacheControl cacheControl = this.resourceProperties.getCache().getCachecontrol().toHttpCacheControl();
                if (!registry.hasMappingForPattern("/webjars/**")) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{"/webjars/**"}).addResourceLocations(new String[]{"classpath:/META-INF/resources/webjars/"}).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

                String staticPathPattern = this.mvcProperties.getStaticPathPattern();
                if (!registry.hasMappingForPattern(staticPathPattern)) {
                    this.customizeResourceHandlerRegistration(registry.addResourceHandler(new String[]{staticPathPattern}).addResourceLocations(WebMvcAutoConfiguration.getResourceLocations(this.resourceProperties.getStaticLocations())).setCachePeriod(this.getSeconds(cachePeriod)).setCacheControl(cacheControl));
                }

            }
        }
```

- webjars  

  `META-INF/resources/webjars/`

- resources下文件夹

  `private static final String[] CLASSPATH_RESOURCE_LOCATIONS = new String[]{"classpath:/META-INF/resources/", "classpath:/resources/", "classpath:/static/", "classpath:/public/"};`

  - resources  上传文件
  - static    静态资源 图片
  - public   公共资源 js
  - 对静态资源的访问会在下面文件夹中找

### 5.2 首页与模板引擎

- 在文件中加入index.html文件

> 为什么

- 写一个页面模板

> 是什么

- Thymeleaf、freemarker、JSP

> 导入

```xml
<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
```

> 怎么用

- 将html放在templates目录下
- 头文件约束 `<html lang="en"  xmlns:th="http://www.thymeleaf.org">`
- 所有html元素都可以被Thymeleaf接管

> 基础语法

- 遍历
  - `<h3 th:each="user: ${users}" th:text="${user}"> </h3>`

### 5.3 扩展MVC

> 怎么做

- 编写一个@Configuration注解类，并且类型要为**WebMvcConfigurer**

- ```java
  //应为类型要求为WebMvcConfigurer，所以我们实现其接口
  //可以使用自定义类扩展MVC的功能
  @Configuration
  public class MyMVCConfig implements WebMvcConfigurer {
      //视图跳转
      @Override
      public void addViewControllers(ViewControllerRegistry registry) {
          registry.addViewController("/kuang").setViewName("test");
      }
  }
  ```

## 六、员工管理系统

### 6.1 首页

- 一般用扩展MVC config配置

  ```java
  @Configuration
  public class MyMVCConfig implements WebMvcConfigurer {
      //视图跳转
      @Override
  
      public void addViewControllers(ViewControllerRegistry registry) {
          //一般用来配置首页
          registry.addViewController("/").setViewName("index");
          registry.addViewController("/index.html").setViewName("index");
      }
  }
  ```

- 所有页面的**静态资源**都要使用Thymeleaf接管 @{}


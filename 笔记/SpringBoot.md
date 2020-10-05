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

 
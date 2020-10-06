# Maven

### 为什么

- 在javaweb开发中自动导入和配置jar包

### 是什么

项目架构管理工具

**约定大于配置**(有约束就不要违反)

### 环境变量

- M2_HOME: bin目录
- MAVEN_HOME: maven目录
- Path: %MAVEN_HOME%\bin

### 阿里云镜像

```
    <mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>*,!jeecg,!jeecg-snapshots</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>
```

### 代码仓库

```
<localRepository>F:\apache-maven-3.6.3\maven-repo</localRepository>
```

### IDEA使用Maven

#### 1、创建Maven项目

![image-20200610015850737](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610015850737.png)

#### 2、观察Maven仓库

#### 3、IDEA中的Maven设置

- IDEA项目创建成功后，看Maven的配置。

#### 4、一个干净的Maven项目

![image-20200610021303111](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610021303111.png)

![image-20200610021849772](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610021849772.png)



#### 5、在IDEA中配置Tomcat

![image-20200610033725050](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610033725050.png)

#### 6、pom文件

pom.xml是maven的核心配置文件

![image-20200610040621089](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610040621089.png)

可能会遇到我没写的配置文件无法导出或生效的问题，解决方案

![image-20200610041302497](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200610041302497.png)

```xml
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


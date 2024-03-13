-- creates database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY "user_0d_2_pwd";

-- grant privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;

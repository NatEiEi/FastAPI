-- CREATE DATABASE IF NOT EXISTS fastapi_app;
USE fastapi_app;

CREATE TABLE accidents (
  accident_date varchar(60),
  accident_time varchar(60),
  step varchar(60),
  ad_state varchar(60) ,
  acman_rec int(10) ,
  acfem_rec int(10)
  deadman_rec int(10) ,
  deadfem_rec int(10) ,
  cause_type varchar(60) 
);
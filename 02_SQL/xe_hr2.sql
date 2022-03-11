select sysdate, systimestamp
from dual;

select
to_char(sysdate, 'YYYY-MM-DD'),
to_char(sysdate, 'YYYY'),
to_char(sysdate, 'DD'),
to_char(sysdate, 'DAY'),
to_char(sysdate, 'HH24:MI:SS'),
to_char(sysdate, 'HH:MI:SS')
from dual;

select extract (day from sysdate)일자,extract (month from sysdate)월, extract (year from sysdate)년
from dual;

select
to_char(sysdate, 'YYYY-MM-DD')
from dual;

select sysdate,
to_char(sysdate, 'DD-MONTH-YYYY','NLS_DATE_LANGUAGE=ENGLISH') AS "Date"

FROM DUAL;

select employee_id, last_name,salary, salary*1.155 "NEW SALARY",
salary*1.155 - salary "Increace"
from employees;

select last_name ||' earns $'||salary||' monthly but wants $'||salary*3 "Dream Salaries"
from employees;

select last_name, trunc((sysdate - hire_date)/ 7,0)  "MONTH_WORKED"
from employees
order by sysdate - hire_date asc;

select last_name, lpad( salary, 15,'$')
from employees;

select last_name, rpad( salary, 15,'$')
from employees;

alter session set NLS_DATE_LANGUAGE=ENGLISH;
select last_name, to_char(hire_date, 'DD-MON-YY') "HIRE_DATE", 
to_char(add_months(hire_date, 6),'Day, "the" Ddspth "of" Month, YYYY') "review"
from employees;

alter session set NLS_DATE_LANGUAGE=ENGLISH;
select last_name, to_char(hire_date, 'DD-MON-YY') "HIRE_DATE", to_char(hire_date, 'DAY') "DAY"
from employees;

select last_name, NVL(to_char(commission_pct), 'No COMMISION')
from employees;


SELECT   rpad(last_name, 8)||' '|| rpad(' ', salary/1000+1, '*') 
EMPLOYEES_AND_THEIR_SALARIES     
FROM     employees      
ORDER BY salary DESC;

select job_id, case job_id
when 'AD_PRES' then 'A'
when 'ST_MAN' then 'B'
when 'T_PROG' then 'C'
when 'SA_REP' then 'D'
when 'ST_CLERK' then 'E'
else '0' end grade
from employees;

select max(salary) Maximum,min(salary) Minimum ,avg(salary) Average ,sum(salary) Sum
from employees;

select job_id, max(salary ) Maximum , min(salary)  Minimum ,
sum(salary) Sum , trunc(avg(salary),2) Average
from employees
group by job_id;

select job_id, count(JOB_ID) as "count(*)"
from employees
group by job_id
order by count(job_id) desc;

select count (manager_id) as "Number of Managers"
from departments;

select manager_id, count(manager_id)
from departments
group by manager_id;

select (MAX(salary)-MIN(salary)) as "DIFFERENCE"
from employees;

select MANAGER_ID, MIN(salary)
from employees
where MANAGER_ID is not null
group by MANAGER_ID
order by MANAGER_ID asc;

select count(*) as TOTAL,
    sum(decode(to_char(hire_date, 'YY'),95,1,0)) as "1995" ,
    sum(decode(to_char(hire_date, 'YY'),96,1,0)) as "1996" ,
    sum(decode(to_char(hire_date, 'YY'),97,1,0)) as "1997" ,
    sum(decode(to_char(hire_date, 'YY'),98,1,0)) as "1998"
from employees;

--11번 문제

select job_id as job,
    sum(decode(department_id, 20,salary)) as "Dept 20",
    sum(decode(department_id, 50,salary)) as "Dept 50",
    sum(decode(department_id, 80,salary)) as "Dept 80",
    sum(decode(department_id, 90,salary)) as "Dept 90",
    sum(salary) as TOTAL
from employees
group by job_id
order by job_id asc;

-- join 1번

select location_id, street_address, city, state_province,country_name
from countries
natural join locations;

-- join 2번

select e.first_name, e.last_name, e.department_id, d.department_name
from employees e join departments d
on e.department_id =  d.department_id
order by e.department_id asc;

-- join 3번

select e.employee_id, e.first_name, e.last_name, 
e.job_id, e.department_id, d.department_name
from employees e inner join departments d 
on e.department_id =  d.department_id
inner join locations t on d.location_id = t.location_id
where t.city = 'Toronto';

-- join 4번

select e.last_name as Employee, e.employee_id as EMP#,
       b.last_name as Manager, b.employee_id as Mgr#
from employees e left outer join employees b
     on e.manager_id = b.employee_id
where b.employee_id is not null;

-- join 5번
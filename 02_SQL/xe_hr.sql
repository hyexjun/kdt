select department_id, avg(salary)
from employees
where manager_id is not null
group by department_id
having avg(salary) < 6000;

select max(avg(salary))
from employees
group by department_id;

select department_id, avg(salary)
from employees
group by department_id
having avg(salary) = (select max(avg(salary))
from employees
group by department_id);


desc job_history
select*from job_history
order by department_id;

desc job_history
select * from job_history;

select employee_id, job_id, department_id
from employees
union
select employee_id, job_id, department_id
from job_history;

select employee_id, job_id, department_id
from employees
intersect
select employee_id, job_id, department_id
from job_history;

select employee_id
from employees
minus
select employee_id
from job_history;

select employee_id
from employees
intersect
select employee_id
from job_history
order by 1;

select employee_id
from employees
union
select (min_salary+max_salary)/2
from jobs;

desc employees
select * from employees;

--문> employees, departments 테이블로부터 사번, 이름, 부서번호, 부서이름을 조회

select a.employee_id, a.first_name, a.last_name, department_id, b.department_name
from employees a natural join departments b;

select a.employee_id, a.first_name, a.last_name, a.department_id, b.department_name
from employees a, departments b
where a.department_id = b.department_id
and a.manager_id = b.manager_id;

select a.employee_id, a.last_name, a.first_name,department_id, b.department_name
from employees a join departments b using(department_id);

select a.last_name, b.department_name, c.city
from employees a, departments b, locations c
where a.department_id = b.department_id
and c.location_id = b.location_id;

select a.last_name, b.department_name, c.city
from employees a join departments b on a.department_id = b.department_id
join locations c on c.location_id = b.location_id;
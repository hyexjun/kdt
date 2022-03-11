--문> job_history, employees 사원들중에서 부서 또는 직무를 2회이상
--변경한 사원 조회 (사원번호, 현재 직무, 현재 부서번호)

select employee_id, last_name, job_id, department_id
from employees t1
where 2<= (select count(*)
                from job_history
                where t1.ememployee_id = employee_id)

select employee_id, last_name, job_id, department_id
from employees t1, (select employee_id, count(*) cnt
                          from job_history
                          group by employee_id ) t2
where t1.ememployee_id = t2.employee_id
and t2.cnt >=2 ;



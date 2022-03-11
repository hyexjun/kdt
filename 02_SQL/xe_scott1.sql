--문> 7566번 사원보다 급여를 많이 받는 사원의 이름, 급여를 조회하라.

select ename, sal
from emp
where sal > (
select sal
from emp
where empno = 7566);

--문> emp테이블에서 사원번호가 7521인 사원과 업무가 같고 급여가 7934인 사원보다
--많은 사원의 사원번호, 이름, 담당업무, 입사일자, 급여를 조회하라
--where절에 조건마다 subquery 선언 가능

select  empno, ename, job, hiredate, sal
from emp
where job = (select job
from emp
where empno = 7521)
and sal >(select sal 
from emp
where empno = 7934);

--문>emp 테이블에서 급여를 제일 많이 받는 사원의 이름, 부서번호, 급여, 입사일을
--조회하라.
--부서별로 최대값의 급여를 받는 사원의 사원번호, 이름, 급여, 부서번호
select empno, ename, sal, deptno, hiredate
from emp
where sal in (select max(sal)
from emp);

--문>emp 테이블에서 급여의 평균보다 적은 사원의 사원번호, 이름, 담당업무, 급여,
--부서번호를 출력하여라.

select empno, ename, sal, deptno, job
from emp
where sal < (select avg(sal)
from emp);

--문>emp 테이블에서 부서별 최소급여가 20번 부서의 최소 급여보다 많은 부서를 조회하라.

select deptno, min(sal)
from emp
group by deptno
having min(sal) > (select min(sal)
from emp
where deptno = 20);

--문> 각 부서별 최대 급여를 받은 사원의 사원번호, 이름, 급여, 부서번호를 출력
select empno, ename, sal, deptno
from emp
where sal in (select max(sal)
from emp
group by deptno);

update emp set deptno=10, sal=3000
where empno = 7000;
commit;
insert into emp ( empno, ename, deptno, sal) values(7000, 'Hong',10,3000);

select empno, ename, sal, deptno
from emp
where (deptno,sal) in (select deptno, max(sal)
from emp
group by deptno);

--문>업무가 salesman인 최소 한 명 이상의 사원보다 급여를 많이 받는 사원의 이름,
--급여, 업무를 조회하다.

select ename, sal, job
from emp
where job !='SALESMAN'
and sal > any(select sal
from emp
where job ='SALESMAN');

--문>업무가 SALESMAN인 모든 사원보다 급여를 많이 받는 사원의 이름, 급여, 업무, 입사일,
--부서번호를 조회하라

select ename, sal, job, hiredate, deptno
from emp
where job != 'SALESMAN'
and sal> all(select sal from emp
where job='SALESMAN');

--문>FORD, BLAKE와 관리자 및 부서가 같은 사원의 정보를 조회
--(단, FORD, BALKE 사원 정보는 결과에서 제외)

select ename, sal, mgr, deptno
from emp
where mgr in (select mgr from emp
where ename in ('FORD', 'BLAKE'))
and deptno in (select deptno from emp
where ename in ('FORD', 'BLAKE'))   --non-pair wise비교
and ename not in ('FORD', 'BLAKE');

select ename, mgr, deptno
from emp
where (mgr ,deptno) in (select mgr , deptno
from emp
where ename in ('FORD', 'BLAKE'))  -- pair wise비교
and ename not in ('FORD', 'BLAKE');

--문> 소속 부서의 평균 급여보다 많은 급여를 받는 사원의 이름, 급여, 부서번호, 입사일,
--업무 정보를 조회하는 SQL문이다. (Co-related subquery와 join)

select ename,deptno,hiredate,sal,
(select avg(sal) from emp t
where t.deptno=e.deptno) deptavgsal
from emp e
where sal < (select avg(sal)
from emp t
where t.deptno=e.deptno);

select ename, sal, deptno, hiredate, job
from emp e
where sal > (select avg(sal)
from emp
where deptno = e.deptno);

select e.ename, e.sal, e.deptno, e.hiredate, e.job
from emp e,(select deptno, avg(sal) avg_sal
from emp
group by deptno) e2
where e.sal > e2.avg_sal
and e.deptno = e2.deptno;

select rownum, empno, ename, deptno, sal
from emp;


select rownum, empno, ename, deptno, sal      ---2
from emp                    -----1
order by sal desc;          ----3

select rownum no, empno, ename, deptno, sal 
from (select  empno, ename, deptno, sal      
        from emp                    
        order by sal desc) a 
where rownum < 6 ;    --Top_N 쿼리

select empno, ename, (case when deptno = (select deptno from dept
where loc = 'DALLAS') then 'TOP'
else 'BRENCH' end) as location
from emp;

select ename, empno, 
decode (deptno ,(select deptno from dept
where loc = 'DALLAS'), 'TOP', 'BRENCH') as location
from emp;

select ename, deptno, sal,
(select avg(sal) from emp where deptno = a.deptno)as asal
from emp a;

select ename, deptno, sal, hiredate
from emp a
order by(select dname from dept
where deptno = a.deptno) desc;

select deptno, ename
from emp
where deptno in(
    select deptno
    from emp
    where ename like '%T%');


--문>소속 사원이 존재하는 부서의 부서번호, 부서명 조회 
select deptno, ename
from emp
where exists(
    select deptno
    from emp
    where deptno in (10,20,30));
--문> 관리자인 사원들만 조회 
SELECT ENAME,JOB
FROM EMP
WHERE JOB = 'MANAGER';

SELECT ename, JOB
FROM emp
where job = 'MANAGER';

select empno, ename
from emp
where empno in(select mgr
from emp);

select empno, ename, job ,hiredate, sal, deptno
from emp e
where exists (select 1
from emp
where e.empno=mgr);


--문> 관리자가 아닌 일반 사원들만 조회
select ename,empno
from emp
where empno not in (select mgr from emp
where mgr is not NULL);

select empno, ename, job, hiredate, sal deptno
from emp e
where not exists(select 1 from emp
where e.empno=mgr);

desc dept
 INSERT INTO dept VALUES (70, 'MARKETING','seoul' ) ;
 
desc dept
INSERT INTO dept (deptno, dname, loc)
 VALUES (70, 'MARKETING','seoul' ) ;  --deptno컬럼에 PK선언된 경우 

insert into emp (empno, ename, hiredate)
values (6000, 'Kim', sysdate);  ---단일행 함수
select * from emp;

INSERT INTO dept
values (60, 'MIS', null);
select * from dept;

insert into emp (empno, ename, hiredate)
values (6000, 'Kim', sysdate);  ---단일행 함수
select * from emp;


insert into emp (empno, ename, hiredate)
values (6000, 'Kim', to_date('02-25-97','MM-DD-RR'));  --?

insert into emp (empno, ename, hiredate)
values (6000, 'Kim', to_date('02-25-97', 'MM-DD-RR'));

INSERT INTO dept (deptno, dname)
values (1000, 'IT'); ---?

INSERT INTO dept ( dname, loc)
values ('IT', 'KangNam');  ---?

insert into emp(empno,ename,deptno)
values(7001, 'Lee',50);

insert into emp (empno, ename, hiredate)
values (6000, 'Kim', sysdate);  ---단일행 함수
select * from emp;

drop table test purge;
create table test (name varchar2(10),
address varchar2(50) default 'seoul');

desc test
select * from test;

INSERT INTO dept (deptno, dname)
values (60, 'MIS');

insert into emp(empno, ename, hiredate)
values (6000, 'Kim', to_date('02-25-97', 'MM-DD-RR'));

drop table test purge;
create table test(name varchar2(10),
address varchar2(50) default 'seoul');
desc test
select * from test;

insert into test(name)values('kim');

drop table test (name) values ('kim');
insert into test values ('lee', 'inchon');
insert into test values ('park', null);
select * from test;
insert into test values ('song', default);

select * from test;

drop table test purge;

create table test (name varchar2(10),
                       address varchar2(50) default 'seoul');
                       
desc test
select * from test;

insert into test (name) values ('kim');
insert into test values ('lee', 'inchon');
insert into test values ('park', null);
select * from test;
insert into test values ('song', default);

select * from test;

create table new_emp(
id number(4),
name varchar2(10));

insert into new_emp
select empno, ename from emp
where ename like '%A%';
select * from new_emp;

--# INSERT문의 VALUES 절 대신에 서브쿼리를 사용하면
--기존 테이블의 값을 포함하는 행을 추가 할 수 있다.
--(INSERT문의 VALUES로 레코드 추가할 때는 1개의 행만 추가됨)
--INSERT문의 VALUES 절 대신에 서브쿼리를 사용하면
--subquery의 검색 결과 행수만큼 추가됨

--# INSERT 절의 열 목록에서 열의 수 및 데이터 유형은
--서브쿼리의 열의 수 및 데이터 유형과 일치해야 함

select empno, ename, sal
from emp;

update emp
set sal = 0;
select * from emp;

rollback;
select*from emp;

--문> 짝수 사번의 사원들의 급여를 10% 인상 변경하시오

update emp
set sal = sal*1.1
where mod(empno,2)=0;
select*from emp;

rollback;
select*from emp;

update emp  set empno = 7788  where deptno = 10;
update emp  set deptno = 90 where empno = 7788;

update emp set hiredate = sysdate where deptno = (select deptno from dept
where loc = 'DALLAS');
select hiredate from emp;
rollback;

select * from emp where ename = 'KING';
update emp
set deptno = (select deptno from emp where ename = 'SCOTT'),
sal = (select sal from emp where ename = 'JANES')
where ename = 'KING';
select * from emp where ename = 'KING';
rollback;

update emp
set(job, deptno)=(select job,deptno
from emp
where empno = 7499),
where empno=7698;

delete from emp ;
select * from emp ;
rollback;
select * from emp;
delete from emp where sal >= 3000;
select empno, ename, sal from emp;
rollback;
select * from emp;

delete from emp where deptno =( select deptno 
from emp where ename ='SCOTT');
select*from emp;

rollback;
select*from emp;

delete from dept where deptno = 0;

select max(sal),min(sal),sum(sal),avg(sal)
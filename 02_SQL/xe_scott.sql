select sal
from emp;

select ename, sal, job, hiredate, deptno, empno
from emp
order by sal desc;  --desc(내림차순) / asc(오름차순)
 
select ename, sal, job, hiredate, deptno, empno
from emp
order by to_date(hiredate);

select empno, ename, job, deptno, sal
from emp
order by deptno, sal desc; --테이블에서 부서번호로 오름차순 정렬 후 부서번호가 같을 경우 급여가 많은 순으로 정렬

select empno, ename, job, deptno, sal
from emp
order by 4,5 desc; --4,5는 select절에 선언된 column position값

select ename, sal, sal*12 "Annual Salary"
from emp
order by sal*12 desc; -- 표현식 가능한지 알아보자

select ename, sal, sal*12 "Annual Salary"
from emp
order by "Annual Salary" desc; -- Alias가능한지 알아보자

select lower('Hello World'), upper('Hello World'), initcap('hello world')
from dual;

select concat(ename, concat('works as a',job))
from emp;

select length('korea'),length('대한민국'),lengthb('korea'),lengthb('대한민국')
from dual;

desc dual
select*from dual;

select substr('Hello World', 7), substr('Hello World',2,4)
,substr('Hello World',-5)
from dual;

-- emp 테이블에서 이름의 첫글자가 'K'보다 크고 'Y'보다 작은 사원의 사원번호, 이름, 업무, 급여, 부서번호를 조회한다.
-- 결과는 이름순으로 정렬하라.
select empno, ename, job, sal, deptno
from emp
where substr(ename,1,1)>'K' and substr(ename,1,1)<'Y'
order by ename;

--emp 테이블에서 이름 중 'L'자의 위치를 조회한다.

select ename,instr(ename, 'L')e_null,
instr(ename,'L',1,1)e_11,
instr(ename,'L',1,1)e_12,
instr(ename,'L',4,1)e_41
from emp
order by ename;

select sal, lpad(sal, 10, '$'), rpad(sal, 10, '$')
from emp;

select ltrim('Hello World', 'H') , ltrim('Hello World', 'e') 
       , rtrim('Hello World', 'd') , rtrim('Hello World', 'l') 
from dual; --중간에 있는 것들은 지울 수 없다.

select length('   he  llo   '), trim('   he  llo   '), trim(length('   he  llo   '))
from dual;

select replace('JACK and JUE', 'J', 'BL') 
from dual; -- jack과 jue단어에서 j를 bl로 대체해서 프린트해라.

select translate('SQL*Plus', ' *SQL', '_s3#') 
from dual;

SELECT CHR(67)||CHR(65)||CHR(84) "Dog"
  FROM DUAL;
  
select empno, ename, job, sal, deptno
from emp
where substr(ename,1,1)>'K' and substr(ename,1,1)<'Y'
order by ename;

select ename, job, LTRIM(job,'A'),sal,LTRIM(sal,1)
from emp
where deptno=20;

select ename, job, rtrim(job,'T'), sal,rTRIM(sal,1)
from emp
where deptno=10;

select ename, replace(ename,'SC','*?')
from emp
where deptno=20;

select ename, translate(ename,'SC','*?')
from emp
where deptno=20;

SELECT TRIM ( LEADING 'A' FROM 'AABDCADD') 결과1 , -- 앞에 A
TRIM ( 'A' FROM 'AABDCADD') 결과2,-- 앞에 A
TRIM ( TRAILING 'D' FROM 'AABDCADD') 결과3 -- 뒤에 D
FROM DUAL ;

-- 문>  translate 함수를 이용해서 사원이름을 소문자로 바꾸어 조회
SELECT empno, ename,
          translate(ename, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'abcdefghijklmnopqrstuvwxyz') u_lower
FROM emp
WHERE deptno = 10;

select round(4567.678) 결과1, round(4567.678, 0) 결과2,
round(4567.678, 2) 결과3, round(4567.678, -2) 결과4
from dual;

select trunc(4567.678) 결과1, trunc(4567.678, 0) 결과2,
trunc(4567.678, 2) 결과3, trunc(4567.678, -2) 결과4
from dual;


SELECT POWER( 2, 10) 결과1, CEIL (3.7) 결과2, FLOOR (3.7) 결과3
 FROM dual;
 
 --문> emp 테이블에서 급여를 30으로 나눈 나머지를 구하여 출력하라.
 select sal, mod(sal,30)
 from emp
 where deptno=10;
 
 --문> emp 테이블에서 사번이 홀수인 사원 정보 출력하여라.
 select empno, ename, sal
 from emp
 where mod(empno, 2)=1;

select ename, sal, sign (sal-2975)
from emp
where deptno=20;

ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';
select SYSDATE, SYSTIMESTAMP, current_date, current_timestamp
        , sessiontimezone
from dual;

alter session set time_zone='+3:00';
select sysdate, systimestamp, current_date, current_timestamp,sessiontimezone
from dual;


-- 문>EMP 테이블에서 현재까지의 근무일수가 몇 주 몇 일인가를 조회한다.
select ename, hiredate, sysdate, sysdate-hiredate "Totoal Days",
trunc((sysdate-hiredate)/7,0) weeks,
round(mod((sysdate-hiredate),7),0) days
from emp
order by sysdate-hiredate desc;

select extract ( day from sysdate) 일자,
extract ( month from sysdate) 월,
extract ( year from sysdate) 년도
from dual;

select systimestamp a,
extract(hour from systimestamp) b,
to_char(systimestamp,'HH24')c
from dual;

select ename, hiredate, extract(year from hiredate)"year",
extract(day from hiredate)"day"
from emp
where deptno = 20;

select ename, hiredate, to_char ( hiredate, 'YYYY')"year",
to_char(hiredate, 'DD')"day"
from emp
where deptno = 20;


--emp 테이블에서 10번 부서원이 현재까지의 근무 월수를 계산하여 조회한다.
select ename, hiredate, sysdate,
months_between(sysdate, hiredate) m_between,
trunc(months_between(sysdate, hiredate),0) t_between
from emp
where deptno =10
order by months_between(sysdate, hiredate)desc;

--emp 테이블에서 10번과 30번 부서원의 입사 일자로부터 5개월이 지난 후 날짜를 계산하여 출력
select ename, hiredate, add_months(hiredate,5)a_month
from emp
where deptno in (10,30)
order by hiredate desc;

--emp 테이블에서 10,30번 부서원의 입사 일자로부터 돌아오는 금요일, 토요일을 계산하여 조회
select ename, hiredate, next_day(hiredate, '금요일') n_6,
next_day(hiredate, '토요일') n_7
from emp
where deptno in (10,30)
order by hiredate desc;

--emp 테이블에서 입사한 달의 근무 일수를 계산하여 조회한다.
-- 단, 토요일과 일요일도 근무일수에 포함한다.

select empno, ename, hiredate, last_day(hiredate)l_last,
last_day(hiredate) - hiredate l_day
from emp
order by last_day(hiredate)-hiredate desc;

--
select round(to_date('21/7/16'),'month'),
round(to_date('21/7/15'),'month'),
round(to_date('21/7/16'),'year'),
round(to_date('21/6/15'),'year')
from dual;

select  trunc(to_date('21/7/16'), 'MONTH'),
trunc(to_date('21/7/15'), 'MONTH'), 
trunc(to_date('21/7/16'), 'YEAR'),
trunc(to_date('21/6/15'), 'YEAR')
from dual;

select 10||10 from dual;
select '10'+'10' from dual;

select sal, to_char(sal, '$999,999,999.00')from emp;
select hiredate, to_char(hiredate, 'YYYY"년" MM"월" DD"일"')from emp;

select to_number('$12,345.50','$99,999.00') from dual;
select to_date('2022년 1월 3일','YYYY"년"MM"월"DD"일"')from dual;

--문> 오늘날짜가 1년 중 몇번째 주인지 조회한다.
--단, 1월 1일 부터 첫째 일요일 까지를 1주차로 한다.
select to_char(sysdate,'WW')test
from dual;

--문> emp업무가 clerk인 사원들의 사번, 이름, 입사일자를 날짜/시간을
--'1998년 1월 1일(요일) 시:분:초'의 형태로 조회.
select empno, ename,job, to_char(hiredate,'YYYY"년"MM"월"DD"일"')
from emp
where job='CLERK';

--문> 모든 사원의 입사후 첫번째 인터뷰 날짜는 6개월이 경과한 첫번째 금요일입니다.
-- 모든 사원의 입사후 인터뷰 날짜를 출력하세요.

select ename, hiredate, to_char(next_day(add_months(hiredate,6),'금'),'YYYY/month/DD')"next 6 month"
from emp;

--# TO_TIMESTAMP : 한 문자를 timestamp 날짜 데이터 유형으로 변환
--# TO_YMINTERVAL : 문자열을 INTERVAL YEAR TO MONTH 형태로 변환
--# TO_DSINYERVAL : 문자열을 INTERVAR DAY TO SECOND값으로 변환

select to_timestamp('2004-8-20 1:30:00', 'YYYY-MM-DD HH:MI:SS')
from dual;

select to_timestamp('10-09-77 14:10:10.123000', 'DD-MM-RR HH24:MI:SS.FF')
from dual;

select sysdate, sysdate + to_dsinterval('003 11:25:33')as "결과"
from dual;

--문> 사원의 이름, 입사일, 입사일자, 입사일에서 1년 6개월 후의 날짜를 조회하라 -- 'to yminterval' 함수 이용

select empno, ename, hiredate,
hiredate+to_yminterval('01-06')as date2
from emp;

--emp 테이블 30번 부서원들의 사원이름, 급여, 보너스, 급여+보너스값 조회

select ename, sal, comm,sal+comm, sal+nvl(comm,0)
from emp
where deptno=30; 

select ename, sal, comm,sal+comm
from emp
where deptno=30
and comm is not null;

--문 emp 테이블의 30번 부서원 아닌 사원들의 사원이름, 부서번호, 매니저 번호, 매니저번호가 null이면
--'상위자'로 표시하고, 매니저번호가 있으면 '담당'으로 표시

select ename, mgr, deptno, nvl2(mgr,'담당','상위자')
from emp
where deptno!=30;

--문 emp 테이블의 30번 부서원들의 사원이름, 업무, 업무가 'salesman'인 경우 null값으로 변경해서 조회한다.
select ename, job, nullif(job,'SALESMAN')as result
from emp
where deptno=30;

--문> emp 테이블에서 이름, 보너스, 연봉, 보너스가 null 아닌 경우 보너스를, 보너스가 null인 경우엔 연봉을, 모두 null인 경우엔 50으로 표시.
select ename, comm, sal, coalesce(comm,sal,50) result
from emp;

select ename, sal, comm, greatest(sal,comm)결과
from emp
where comm is not null;

select ename, sal, comm, least(sal,comm)결과
from emp
where comm is not null;

select coalesce(null, null, null, 1,2,3),
coalesce(null, null, null, null, null, null),
coalesce(0, null, null, 1,2,3)
from dual;

--#decode : SQL 내에서 IF - THEN - ELSE IF - END 로직을 사용 할 수 있도록 Oracle 에서 제공하는 함수
 select DECODE (9+1, 9, '정답1', 10, '정답2') from dual;
 select DECODE (9+1, 9, '정답1', 10, '정답2', '정답3') from dual;

--decode(표현식, 비교값1, 리턴값1, 비교값2, 리턴값 2,....[리턴값n])
--if 표현식=비교값 1 then 리턴값 1
--else if 표현식 = 비교값2 then 리턴값 2
--....
--else 리턴값 n

 --문> EMP사원의 담당 업무가 analyst인 경우 급여는 10% 증가, clerk인 경우 급여는 20%증가, manager인 경우 30%증가,
 --president인 경우 40% 증가, salesman인 경우 50%증가, 그 외엔 기존 급여값으로 나오도록 조회한다.
 
--ANSI협회 - SQL 표준 제정
--SQL1999표준에서 조건처리 구문이 추가됨
--CASE  [표현식] WHEN 비교값1 THEN 처리1
--      	      [ WHEN 비교값2 THEN 처리2
--                      :
--                   WHEN 비교값N THEN 처리N ]
--                   [ ELSE 디폴트처리 ]
--                    END
--CASE  WHEN 비교조건1 THEN 처리1
--        [ WHEN 비교조건2 THEN 처리2
--                     :
--         WHEN 비교조건N THEN 처리N ]
--        [ ELSE 디폴트처리 ]
--         END

 select empno, ename, job, sal, decode (job, 'ANALYST',sal*1.1,'CLERK',sal*1.2,'MANAGER',sal*1.3,'PRESIDENT',sal*1.4,
 'SALESMAN',sal*1.5,sal)
 from emp;

select empno, ename, sal, job, case job when 'ANALYST' then sal*1.1 
when 'CLERK' then sal*1.2
when 'MANAGER' then sal*1.3
when 'PRESIDENT' then sal*1.4
when 'SALESMAN' then sal*1.5
else sal end salary
from emp;

--문> 사원번호, 이름, 급여, 급여의 세금을 출력하시오.
--급여가 1000미안이면 0
--급여가 1000이상~2000미만이면 급여의 3%
--급여가 2000이상~3000미만이면 급여의 6%
--급여가 3000이상~4000미만이면 급여의 9%
--급여가 4000이상이면 급여의 12%

select empno, ename, sal, case when sal<1000 then sal*1 
when sal<2000 then sal*0.97
when sal<3000 then sal*0.94
when sal<4000 then sal*0.91
else sal*0.88 end "세금을 제외한 급여"
from emp;

select empno, ename, sal, decode(trunc(sal/1000),0,0,
1, sal*0.03,
2, sal*0.06,
3, sal*0.09,
sal*0.12) "TAX"
from emp;

SELECT MIN(ename), MAX(ename), MIN(hiredate), MAX(hiredate)    
FROM emp;

select avg(sal), max(sal), min(sal),sum(sal)
from emp
where job = 'salesman';


select count(*)c1,count(comm)c2,avg(comm)c3,avg(nvl(comm,0))c4
from emp;

select count(deptno) c_dept, count(distinct deptno) c_dis,
count(distinct job)c_job
from emp;

select stddev(sal), variance(sal)
from emp;

select count(*),trunc(avg(sal),1), min(sal),max(sal),sum(sal)
from emp
group by deptno;

select count(*)부서번호,job 직업,trunc(avg(sal),1)평균, min(sal)최소,max(sal)최대,sum(sal)합
from emp
group by deptno, job;

select count(*)인원수, job 업무,trunc(avg(sal),1)평균,sum(sal)합
from emp
group by job;

select deptno 부서번호, count(*)인원수, trunc(avg(sal),1)평균,sum(sal)합,min(sal)최소,max(sal)최대
from emp
group by deptno
order by sum(sal) desc;

--select ~ column, 표현식, 그룹함수표현식, ..  --- 5
--from ~        --1
--[where ~]    ---2     filter 조건
--[group by ~]  --3  
--[having 그룹함수 적용 조건]  ---4
--[order by ~]  --6     

SELECT deptno 부서번호, count(*) 인원수, sum(sal) 급여의합
FROM emp
GROUP BY deptno
HAVING count(*) > 4;

select deptno , avg(sal), sum(sal)
from emp
group by deptno
HAVING max(sal) >= 2900;

select listagg(ename,',')within group (order by ename)as names
from emp;

select deptno, listagg(ename,',') within group (order by ename) as names
from emp
group by deptno;

select deptno, listagg(job,',') within group(order by job desc) as jobs
from emp
group by deptno;

select listagg(ename, ':') within group(order by ename desc) "Ename",
listagg(hiredate, ':') within group(order by ename desc) "hiredate",
min(hiredate) "Earliest"
from emp
where deptno=20;

select ename, job, listagg(ename,',') within group(order by ename)over(partition by job)
as names
from emp
where job in('MANAGER','SALESMAN');

select ename, job, listagg(ename,',')within group(order by ename) as names
from emp
where job in ('MANAGER', 'SALESMAN')
group by job;

select sum(sal), deptno, listagg(ename,',')
within group(order by sal)as names
from emp
group by deptno
order by sum(sal) desc;

select to_number(null), ' ',avg(sal)
from emp
union all
select deptno, ' ',avg(sal)
from emp
group by deptno
union all
select deptno, job,avg(sal)
from emp
group by deptno, job;

select deptno,job,avg(sal)
from emp
group by rollup(deptno,job);

select emp.empno, emp.ename, emp.deptno, dept.dname
from emp, dept;

select a.ename, a.deptno, b.dname, b.loc
from emp a, dept b
where a.deptno=b.deptno;

select emp.empno, emp.ename, emp.deptno, dept.dname
from emp, dept;  ----56rows (14rows * 4rows)   조인 조건 누락으로  cartesian product,  cross join(sql3표준)

select a.ename, a.deptno, b.dname, b.loc
from emp a natural join dept b;

--natural join은 두 테이블에서 동일한 이름을 가진 모든 열을 기준으로 join수행
--natural join은 두 테이블에서 동일한 이름의 컬럼이 컬럼타입이 다른 경우 join을 수행하면 오류 발생
--natural join은 join 조건의 컬럼명 앞에 소유자 테이블명이나 alias를 사용할 수 없음

create table emp20
as select empno, ename, deptno deptid, sal, job
from emp
where deptno = 20;

desc emp20
select * from emp20;

select a.empno, a.ename, a.deptid, b.dname
from emp20 a join dept b on a.deptid = b.deptno;

select a.empno,a.ename, a.deptid, b.dname
from emp20 a join dept b on a.deptid = b.deptno;

desc salgrade 
select * from salgrade;

select a.empno, a.ename, a.salgrade, b.sal
from emp20 b join sal a on a.salgrade = sal;

select a.empno, a.ename, a.sal, b.grade
from emp a, salgrade b
where a.sal between b.losal and b.hisal;

select a.empno, a.ename, a.sal, b.grade
from emp a join salgrade b on (a.sal between b.losal and b.hisal);


--문> 사원번호, 사원이름, 관리자번호, 관리자이름 조회결과 생성
--self join - 자기 참조가 가능한 테이블(PK<-FK이 존재)에서만 수행됨
select a.empno, a.ename, a.mgr, b.ename
from emp a, emp b
where a.mgr = b.empno;

select a.empno, a.ename, a.mgr, b.ename
from emp a join emp b on a.mgr = b.empno;

insert into emp (empno, ename)
value(7000,'홍길동');
commit;

select empno, ename, deptno,job,sal
from emp;

--조인 컬럼값이 null인경우 PK와 FK equi 조인 조건에서는 조인되지 못해서 조인
--결과에 누락됨 => 조인 결과로 가져오려면 outer join을 수행해야함

--문>부서를 아직 배정받지 못한 사원을 포함해서 사원들의 부서번호와 부서이름을 출력

select a.ename,a.deptno, b.dname,b.loc
from emp a, dept b
where a.deptno = b.deptno;

select a.ename, a.deptno, b.dname, b.loc
from emp a, dept b
where a.deptno=b.deptno(+);

select a.ename, a.deptno, b.dname, b.loc
from emp a left outer join dept b on a.deptno = b.deptno;

--문> 부서별 사원정보를 출력
--(40번 부서 정보 조인 결과로 생성하도록 SQL 작성)

select b.deptno, b.dname, a.empno, a.ename
from emp a, dept b
where a.deptno = b.deptno
order by 1 asc;

select b.deptno, b.dname, a.empno, a.ename
from emp a right outer join dept b on a.deptno = b.deptno
order by 1 asc;

select b.deptno, b.dname, a.empno, a.ename
from emp a, dept b
where a.deptno(+)=b.deptno
order by 1 asc;

desc mgr
select * from emp;

select a.empno a.ename, b.deptno, d.ename
from emp a, dept b
where a.deptno(+)=b.deptno(+)
order by 1 asc;

--7000번대 사원 레코드와 40번 부서 정보 레코드를 모두 조인 결과로 생성

select b.deptno, b.dname, a.empno, a.ename
from emp a full outer join dept b on a.deptno = b.deptno
order by 1 asc;

select b.deptno, b.dname, a.empno, a.ename
from emp a cross join dept b;


-- Практические задания:

-- 1. Чтобы успешно справиться с данным практическим заданием, вам необходимо выполнить как минимум задания 1-4 практики в теме 2.3 "Реляционные базы данных: PostgreSQL", 
-- но желательно сделать, конечно же, все.

-- 2. Теперь мы знакомы с гораздо большим перечнем операторов языка SQL и это дает нам дополнительные возможности для анализа данных. Выполните следующие запросы:
-- a. Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.
SELECT 
    full_name,
    salary 
FROM 
    employees
WHERE 
    salary = (
        SELECT 
            MAX(salary)
        FROM 
            employees
    );

-- b. Попробуйте вывести фамилии сотрудников в алфавитном порядке
SELECT 
    SPLIT_PART(full_name, ' ', 1) 
FROM 
    employees 
ORDER BY 
    full_name ASC;

-- c. Рассчитайте средний стаж для каждого уровня сотрудников
SELECT 
    grade, 
    AVG(CURRENT_DATE - start_date) AS avg_exp 
FROM 
    employees 
GROUP BY 
    grade 
ORDER BY 
    avg_exp ASC;

-- d. Выведите фамилию сотрудника и название отдела, в котором он работает
SELECT
    e.full_name,
    d.title
FROM
    employees e
INNER JOIN departments d ON e.department_id = d.id
ORDER BY 
    d.title ASC;

-- e. Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.
SELECT 
    e.full_name, 
    d.title, 
    e.salary 
FROM 
    employees e 
    INNER JOIN departments d ON e.department_id = d.id 
    AND salary IN (
      SELECT 
        MAX(e.salary) AS max_salary 
      FROM 
        employees e 
        INNER JOIN departments d ON e.department_id = d.id 
      GROUP BY 
        d.title
  );
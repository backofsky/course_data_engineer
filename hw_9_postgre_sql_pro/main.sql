-- Практические задания:

-- * Выведите название самого крупного отдела.
SELECT 
    title
FROM 
    departments
WHERE 
    employee_count = (
        SELECT 
            max(employee_count) 
        FROM departments
    );

-- * Выведите номера сотрудников от самых опытных до вновь прибывших
SELECT 
    id
FROM 
    employees
ORDER BY 
    CURRENT_DATE - start_date DESC;

-- * Рассчитайте среднюю зарплату для каждого уровня сотрудников
SELECT
    grade,
    AVG(salary)
FROM 
    employees
GROUP BY 
    grade;

-- * Добавьте столбец с информацией о коэффициенте годовой премии к основной таблице. 
-- Коэффициент рассчитывается по такой схеме: базовое значение коэффициента – 1, каждая оценка действует на коэффициент так:
-- Е – минус 20%
-- D – минус 10%
-- С – без изменений
-- B – плюс 10%
-- A – плюс 20%
-- Соответственно, сотрудник с оценками А, В, С, D – должен получить коэффициент 1.2.
WITH coeff AS(
  SELECT 
    employee_id,
    q1, 
    CASE WHEN q1 = 'A' THEN 0.2 WHEN q1 = 'B' THEN 0.1 WHEN q1 = 'D' THEN -0.1 WHEN q1 = 'E' THEN -0.2 ELSE 0.0 END AS coeff1, 
    q2, 
    CASE WHEN q2 = 'A' THEN 0.2 WHEN q2 = 'B' THEN 0.1 WHEN q2 = 'D' THEN -0.1 WHEN q2 = 'E' THEN -0.2 ELSE 0.0 END AS coeff2, 
    q3, 
    CASE WHEN q3 = 'A' THEN 0.2 WHEN q3 = 'B' then 0.1 WHEN q3 = 'D' then -0.1 WHEN q3 = 'E' THEN -0.2 ELSE 0.0 END AS coeff3, 
    q4, 
    CASE WHEN q4 = 'A' THEN 0.2 WHEN q4 = 'B' THEN 0.1 WHEN q4 = 'D' THEN -0.1 WHEN q4 = 'E' THEN -0.2 ELSE 0.0 END AS coeff4 
  FROM 
    scores
)
SELECT 
    t2.full_name, 
    (coeff1 + coeff2 + coeff3 + coeff4) + 1 AS total_coeff
FROM 
    coeff t1
    INNER JOIN employees t2 ON t1.employee_id = t2.id;
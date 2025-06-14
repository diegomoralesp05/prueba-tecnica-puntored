-- Sección 2: Prueba práctica SQL

-- 1. Obtener los 5 clientes con mayor monto total de ventas en los últimos 6 meses
SELECT c.id, c.nombre, c.apellido, SUM(v.monto) AS total_ventas
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY c.id, c.nombre, c.apellido
ORDER BY total_ventas DESC
LIMIT 5;

-- 2. Calcular el ticket promedio de ventas por cliente en el último año
SELECT c.id, c.nombre, c.apellido,
       COUNT(v.id) AS cantidad_ventas,
       SUM(v.monto) AS total_ventas,
       (SUM(v.monto) / COUNT(v.id)) AS ticket_promedio
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.id, c.nombre, c.apellido;

-- 3. Obtener el nombre completo de los clientes y su monto total de ventas
SELECT CONCAT(c.nombre, ' ', c.apellido) AS nombre_completo,
       SUM(v.monto) AS total_ventas
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
GROUP BY nombre_completo;

-- 4. Ingreso promedio de ventas por mes
SELECT TO_CHAR(v.fecha, 'YYYY-MM') AS mes,
       AVG(v.monto) AS ingreso_promedio
FROM ventas v
GROUP BY mes
ORDER BY mes;

-- 5. Ranking de clientes por ventas en el último año
SELECT c.id, c.nombre, c.apellido,
       SUM(v.monto) AS total_ventas,
       RANK() OVER (ORDER BY SUM(v.monto) DESC) AS ranking
FROM clientes c
JOIN ventas v ON c.id = v.cliente_id
WHERE v.fecha >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.id, c.nombre, c.apellido;

-- 6. Total de ventas por cliente y selección de los que están por encima del promedio general
WITH ventas_por_cliente AS (
    SELECT c.id, c.nombre, c.apellido, SUM(v.monto) AS total_ventas
    FROM clientes c
    JOIN ventas v ON c.id = v.cliente_id
    GROUP BY c.id, c.nombre, c.apellido
),
promedio_general AS (
    SELECT AVG(total_ventas) AS promedio
    FROM ventas_por_cliente
)
SELECT vpc.*
FROM ventas_por_cliente vpc, promedio_general pg
WHERE vpc.total_ventas > pg.promedio;

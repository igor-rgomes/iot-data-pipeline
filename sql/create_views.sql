-- 1) Média de temperatura por sala
CREATE OR REPLACE VIEW avg_temp_por_room AS
SELECT
    "room_id/id" AS room_id,
    AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY "room_id/id";

-- 2) Quantidade de leituras por hora
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT
    EXTRACT(HOUR FROM noted_date) AS hora,
    COUNT(*) AS total_leituras
FROM temperature_readings
GROUP BY EXTRACT(HOUR FROM noted_date)
ORDER BY hora;

-- 3) Temperatura máxima e mínima por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT
    DATE(noted_date) AS data,
    MAX(temp) AS temp_max,
    MIN(temp) AS temp_min
FROM temperature_readings
GROUP BY DATE(noted_date)
ORDER BY data;
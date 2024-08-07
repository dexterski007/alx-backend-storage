-- fans calc
SELECT origin, SUM(nb_fans) as nb_fans
GROUP BY origin ORDER BY nb_fans;

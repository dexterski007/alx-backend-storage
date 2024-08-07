-- fans calc
SELECT origin, SUM(nb_fans) as tot_fans
GROUP BY origin ORDER BY tot_fans;

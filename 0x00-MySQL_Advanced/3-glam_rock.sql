-- glam rock
SELECT band_name,
CASE
    WHEN split is NULL THEN 2022 - formed
    ELSE split - formed
END as lifespan
FROM metal_bands
WHERE style == 'Glam rock'
GROUP BY band_name ORDER BY lifespan DESC;

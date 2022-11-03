-- select country of origin of bands indexed by fans
SELECT origin, sum(fans) AS nb_fans
FROM metal_bands
GROUP By origin
ORDER by  nb_fans DESC;
-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, Year(COALESCE(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE 'Glam rock' 
ORDER By lifespan DESC;
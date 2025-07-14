-- More realistic habitability criteria(loosened)
SELECT 
    name,
    mass,
    radius,
    temp_calculated,
    orbital_period,
    semi_major_axis
FROM planetary_analysis
WHERE 
    -- Keep strict temperature (most critical)
    temp_calculated BETWEEN 273 AND 323
    
    -- Loosen mass range (0.3 to 3.0 Earth masses)
    AND mass BETWEEN 0.3 AND 3.0
    
    -- Loosen radius range (0.5 to 2.0 Earth radii)
    AND radius BETWEEN 0.5 AND 2.0
    
    -- Loosen orbital period (100 to 800 days)
    AND orbital_period BETWEEN 100 AND 800
    
    -- Remove some filters that might be too restrictive
    AND mass IS NOT NULL
    AND radius IS NOT NULL
    AND temp_calculated IS NOT NULL
    
ORDER BY 
    ABS(temp_calculated - 288) + 
    ABS(mass - 1.0) + 
    ABS(radius - 1.0) +
    ABS(orbital_period - 365);


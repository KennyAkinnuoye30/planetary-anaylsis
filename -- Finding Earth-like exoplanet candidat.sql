-- Finding Earth-like exoplanet candidates for human habitability
SELECT 
    name,
    mass,
    radius,
    temp_calculated,
    orbital_period,
    semi_major_axis,
    star_mass,
    star_radius
FROM planetary_analysis
WHERE 
    -- Earth-like temperature range (habitable zone) - in Kelvin
    temp_calculated BETWEEN 273 AND 323
    
    -- Earth-like mass range (0.5 to 2.0 Earth masses)
    AND mass BETWEEN 0.5 AND 2.0
    
    -- Earth-like radius range (0.8 to 1.2 Earth radii)
    AND radius BETWEEN 0.8 AND 1.2
    
    -- Earth-like orbital period (200 to 500 days)
    AND orbital_period BETWEEN 200 AND 500
    
    -- Earth-like distance from star (0.8 to 1.2 AU)
    AND semi_major_axis BETWEEN 0.8 AND 1.2
    
    -- Sun-like star mass (0.8 to 1.2 solar masses)
    AND star_mass BETWEEN 0.8 AND 1.2
    
    -- Ensure no null values in critical fields
    AND mass IS NOT NULL
    AND radius IS NOT NULL
    AND temp_calculated IS NOT NULL
    
ORDER BY 
    -- Prioritize planets closest to Earth values
    ABS(temp_calculated - 288) +  -- Earth's average temp ~288K (15°C)
    ABS(mass - 1.0) + 
    ABS(radius - 1.0) +
    ABS(orbital_period - 365);
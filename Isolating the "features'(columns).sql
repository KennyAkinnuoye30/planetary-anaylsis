
-- Isolating the "features'(columns) I need for my analysis into a new table seperate from the original dataset
SELECT 
    name, mass, radius, orbital_period, semi_major_axis, temp_calculated,
    star_mass, star_teff, discovered, detection_type,
    mass_error_min, radius_error_min
INTO planetary_analysis
FROM Exoplanet_Dataset;
 
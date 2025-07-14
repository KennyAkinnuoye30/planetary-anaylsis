SELECT
    name, -- Planet name or designation
    mass, -- Estimated planetary mass
    radius, -- Planetary radius
    log_g, -- Surface gravity (logarithmic scale)
    orbital_period, -- Orbital period in days
    semi_major_axis, -- Semi-major axis of orbit (in AU)
    eccentricity, -- Orbital eccentricity
    temp_calculated, -- Estimated or observed equilibrium temperature
    geometric_albedo, -- Reflectivity of the planet
    molecules, -- Molecules detected in atmosphere (if any)
    star_mass, -- Stellar mass (in solar masses)
    star_radius, -- Stellar radius (in solar radii)
    star_teff, -- Effective temperature of the star (in Kelvin)
    star_age, -- Estimated age of the star (in Gyr)
    star_metallicity, -- Metallicity ([Fe/H]) of the star
    star_magnetic_field -- Presence of magnetic field (if known)
INTO
    planetary_analysis
FROM
    Exoplanet_Dataset; 
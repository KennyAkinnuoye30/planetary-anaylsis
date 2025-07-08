
-- Droping remove mass_error_min and radius_error_min from the correlation analysis since they are not real core measurements!
-- They just represent uncertainty in the core measurement. Upper Bound and Lower Bound additions or subtractions
ALTER TABLE dbo.planetary_analysis
    DROP COLUMN radius_error_min
GO

ALTER TABLE dbo.planetary_analysis
    DROP COLUMN mass_error_min
GO

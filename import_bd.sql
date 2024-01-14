USE Kaggle
GO

IF NOT EXISTS (SELECT * FROM SYS.TABLES WHERE object_id = OBJECT_ID(N'dbo.starbucks') AND type='U')
	CREATE TABLE dbo.starbucks (
	
		beverage_category VARCHAR(50),
		beverage VARCHAR(255),
		beverage_prep VARCHAR(50),
		calories DECIMAL(6, 3),
		total_fat_g VARCHAR(50),
		trans_fat_g DECIMAL(6, 3),
		saturated_fat_g DECIMAL(6, 3),
		sodium_mg DECIMAL(6, 3),
		total_carbohydrates_g DECIMAL(6, 3),
		cholesterol_mg DECIMAL(6, 3),
		dietary_fibre_g DECIMAL(6, 3),
		sugars DECIMAL(6, 3),
		protein_g DECIMAL(6, 3),
		vitamin_a_pct VARCHAR(50),
		vitamin_c_pct VARCHAR(50),
		calcium_pct VARCHAR(50),
		iron_pct VARCHAR(50),
		caffeine_pct VARCHAR(50)
	
	)

GO

TRUNCATE TABLE dbo.starbucks
GO

--importar data desde archivo

BULK INSERT dbo.starbucks
FROM 'D:\pparcial\dataset\starbucks.csv'
WITH
(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a'
)

GO

USE zillow;

SELECT * from buildingclasstype; # Description of structure of walls, frames, roofs, including type of material

SELECT * from propertylandusetype # 25 unique categories of buildings/properties
LIMIT 40;


SELECT COUNT(plut.propertylandusetypeid) FROM propertylandusetype AS plut
	JOIN properties_2017 AS prop17
		ON plut.propertylandusetypeid = prop17.propertylandusetypeid
	JOIN predictions_2017 AS pred17
		ON pred17.id = prop17.id
	WHERE plut.propertylandusetypeid IN (261,262,273,275,279) 
		AND pred17.transactiondate >= '2017-05-01' AND pred17.transactiondate <= '2017-06-30';

# prop types 261-single fam, 262-rural residence, 273- bungalow, 275-manufacturered modular prefab, 279- inferrred single fam
# Dates between May 1 and June 30, 2017
#16,083 records

SELECT * FROM propertylandusetype AS plut
	JOIN properties_2017 AS prop17
		ON plut.propertylandusetypeid = prop17.propertylandusetypeid
	JOIN predictions_2017 AS pred17
		ON pred17.id = prop17.id
	WHERE plut.propertylandusetypeid IN (261,262,273,275,279) 
		AND pred17.transactiondate >= '2017-05-01' AND pred17.transactiondate <= '2017-06-30';


#Query with columns to use
SELECT 
	propertylandusedesc,
    bathroomcnt,
    bedroomcnt,
    calculatedfinishedsquarefeet,
    taxvaluedollarcnt,
    taxamount,
    fips
FROM propertylandusetype AS plut
	JOIN properties_2017 AS prop17
		ON plut.propertylandusetypeid = prop17.propertylandusetypeid
	JOIN predictions_2017 AS pred17
		ON pred17.id = prop17.id
	WHERE plut.propertylandusetypeid IN (261,262,273,275,279) 
		AND pred17.transactiondate >= '2017-05-01' AND pred17.transactiondate <= '2017-06-30';
	
 





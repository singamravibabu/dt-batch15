query = '''SELECT
regionID, name as regionName
FROM Region
WHERE regionID=?
'''
print(query)

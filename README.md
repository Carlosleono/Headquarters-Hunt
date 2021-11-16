# Headquarters-Hunt
![portada](indoor-treasure-hunt-for-children-1695332_FINAL-a9fabbdd08a14bfcbf9acb8ecae3a2f3.png)
# Objetive
The objective of this project is to determine the perfect location for a new company in the gaming industry. 

- **Designers** --> near to companies that do design.
- **30% of the company** --> have at least 1 child.
- **Developers** --> to be near tech startups that have raised at least 1 Million dollars.
- **Executives** --> like Starbucks.
- **Account managers** --> travel a lot.
- **Average age between 25 and 40** -->some place to go party.
- **CEO** --> vegan.
- **Maintenance guy** --> basketball court
- **Dog—"Dobby"** --> hairdresser every month. 

# Structure

The structure of this project is composed of:
 1. A folder of notebooks: 
    
    a) **ComparableCompanies.ipynb** -->Where we search in the MongoDB databse "companies" for similar companies (less than 100 employes, startups, mobilegames...). We select the three companies that are more similir to our own to get three cities in which we will be looking for a headquarter

    b) **APIs.ipynb** --> Where we will find places near to our preselect locations that fit the requirements made by the employees.

    c) **Geoqueries.ipynb** --> Where we make geospatial queries to find the distance of each place to our location and make the normalize relation to get the city that best suit our company

    d) **Maps.ipynb** --> Where we draw a map of pour preferred location with the places found near it.

 2. scr folder: folder where we store the functions used in the notebooks
 
 ###




# Ressources

-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.


# Libraries



[sys](https://docs.python.org/3/library/sys.html)

[requests](https://pypi.org/project/requests/2.7.0/)

[pandas](https://pandas.pydata.org/)

[dotenv](https://pypi.org/project/python-dotenv/)

[pymongo](https://www.mongodb.com/2)

[json](https://docs.python.org/3/library/json.html)

[os](https://docs.python.org/3/library/os.html)

[geopandas](https://geopandas.org/)

[shapely](https://pypi.org/project/Shapely/)

[reduce](https://docs.python.org/3/library/functools.html)

[operator](https://docs.python.org/3/library/operator.html)

[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)

[re](https://docs.python.org/3/library/re.html)
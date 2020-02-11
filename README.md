# NetworkScience

install from `.xml` and `.dtd` files from  [DBLP dataset](https://dblp.uni-trier.de/xml/)
in order to prase the xml data you require both dtd and xml to be in the same folder


installing of dataset and parsing the data in XML format.
```bash
wget http://dblp.org/src/DblpExampleParser.java \
	http://dblp.org/src/mmdb-2019-04-29.jar \
	http://dblp.org/xml/release/dblp-2019-04-01.xml.gz \
	http://dblp.org/xml/release/dblp-2017-08-29.dtd

gunzip dblp-2019-04-01.xml.gz

javac -cp mmdb-2019-04-29.jar DblpExampleParser.java

java -Xmx8G -cp mmdb-2019-04-29.jar:. DblpExampleParser dblp-2019-04-01.xml dblp-2017-08-29.dtd
```
python3 src/dblp_parser.py
for parsing data from .xml to .json format for analytics

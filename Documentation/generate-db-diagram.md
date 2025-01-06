# Create Database Diagram with SchemaCrawler and Windows Powershell

For further options see [SchemaCrawler.com](https://www.schemacrawler.com/diagramming.html).

## For dbdiagram.io

```
docker run `
  --mount type=bind,source="$(pwd)",target=/home/schcrwlr/share `
  --rm -it `
  schemacrawler/schemacrawler `
  /opt/schemacrawler/bin/schemacrawler.sh `
  --server sqlite `
  --database share/test.db `
  --info-level standard `
  --command script `
  --script-language python `
  --script dbml.py `
  --output-file share/database.dbml
```

## As Image

```
docker run `
  --mount type=bind,source="${PWD}",target=/home/schcrwlr `
  --rm -it `
  schemacrawler/schemacrawler `
  /opt/schemacrawler/bin/schemacrawler.sh `
  --server=sqlite `
  --database=test.db `
  --info-level=standard `
  --command=schema `
  --output-file=database.png
```

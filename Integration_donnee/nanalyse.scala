val dfReader = spark.read
val empDF = dfReader.option("header","true").option("delimiter",";").option("inferSchema",true).csv ("file:///.../Employes.csv")
empDF.printSchema
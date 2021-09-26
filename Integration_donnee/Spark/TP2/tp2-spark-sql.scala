val dfReader = spark.read
val empDF = dfReader.option("header","true").option("delimiter",";").option("inferSchema",true).csv ("file:///.../Employes.csv")
empDF.printSchema
empDF.show
empDF.select('nom, 'adresse).show
val pariesiensDF = empDF.select('nom, 'adresse).where ('adresse === "Paris")
pariesiensDF.show
// conversion en type Date
empDF.select(upper('nom), to_date('ddn, "dd/MM/yyyy")).show
// Agrégation de données
empDF.groupBy('adresse).count().show
// extraction de l'année de naissance
val df2= empDF.select(upper('nom).as("NOM"), to_date('ddn, "dd/MM/yyyy").as("DDN")).select (year('DDN).as("annee_naiss"))
val df2= empDF.withColumn("DDN_DATE", to_date('ddn, "dd/MM/yyyy")).withColumn ("Annee-Naiss",year('DDN_DATE))
// Année de naissance moyenne par ville/adresse
df2.groupBy('adresse).agg(avg("Annee-Naiss").as("AnneeNaissMoyenne")).show
// (re)partitionnement de la DataFrame
df2.rdd.getNumPartitions
df2.repartition(4)
// A faire : fonctions UDF
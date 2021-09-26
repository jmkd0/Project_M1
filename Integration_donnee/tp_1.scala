val dfReader = spark.read
val empDF = dfReader.option("header","true").option("delimiter",";").option("inferSchema",true).csv("/home/komlan/Project_M1/Integration_donnee/datasets/tp1/Personnel.csv")
empDF.show
val myList = (1 to 10).toList
val rdd = sc.parallelize(myList)
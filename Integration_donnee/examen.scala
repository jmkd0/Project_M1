//EXERCICE 1
val rawdata = dfReader.option("header","true").option("delimiter",";").option("inferSchema",true).csv("/home/komlan/Project_M1/Integration_donnee/Contrôle/dataset/exo1/Personnels.csv")
rawdata.show

//Q-1. Afficher les nom et prénom de tous les personnels (noms entièrement en majuscules et seulement la première lettre pour les prénoms).

val empDF1 = rawdata.select('Nom, 'Prenom)
val empDF11 = empDF1.withColumn("Nom",initcap(col("Nom")))
empDF11.show

//Q2-  Afficher les personnels dont le prénom inclut la sous-chaine « ill ».
val empDF2 = rawdata.select('Prenom)
val empDF21 = empDF2.filter(col("Prenom").contains("ill"))
empDF21.show

//Q3- Afficher les personnels français
val upperdata = rawdata.withColumn("Country",upper(split('VillePays," ")(2)))
val empDF31 = upperdata.select('Nom, 'Prenom).where('Country === "FR")
empDF31.show

//Q-4 Afficher les personnels nés après 2000
val datedata = rawdata.withColumn("DDN", to_date(col("DDN"),"dd/MM/yyyy"))
datedata.filter("year(DDN) > 2000").show

//Q-5 Afficher l’âge moyen des personnels par pays
val agedata = empDF4.withColumn("Age",year(current_date) - year('DDN))
agedata.select(avg('Age)).show
val maxage = agedata.select(max('Age))
println(maxage[0])
agedata.select('Nom, 'Prenom).where('Age === maxage).show


///Exercice 2
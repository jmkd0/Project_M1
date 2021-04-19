val txtRDD = sc.textFile ("file:///Volumes/development/data/2020-21/m1-p8-info/datasets/dataset-spark/RecitTexte.txt")

print("Les lignes contenant le mot chapeau")
txtRDD.filter (ligne => ligne.contains("chapeau")).collect.foreach(println)

println("Nombre de mots")
txtRDD.filter(ligne => !ligne.isBlank).map (ligne => ligne.split(" ")).map (tabMots => tabMots.length).reduce ((v1,v2)=>v1+v2


txtRDD.filter(ligne => !ligne.isEmpty).flatMap(ligne => ligne.split(" ")).map (mot => mot.length)

println("Nombre de caractères")
txtRDD.filter(ligne => !ligne.isEmpty).flatMap(ligne => ligne.split(" ")).map (mot => mot.length).sum

// 2ème façon de calculer le nombre de mots (mias peu optimale !!!)
txtRDD.filter(ligne => !ligne.isEmpty).flatMap(ligne => ligne.split(" ")).map (mot => (mot, 1)).reduceByKey ((v1,v2)=>v1+v2).map (e => e._2).sum


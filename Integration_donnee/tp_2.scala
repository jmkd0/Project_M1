//10-Créer une liste de 0 à 10
val myList = (1 to 10).toList
//11- Creer une RDD
val rdd = sc.parallelize(myList)
//12- Afficher RDD
// je pense que ça n'affiche rien parceque on a pas utilisé l'équivalence de join dans les thread, donc le rdd n'a pas encore les données à afficher
rdd.foreach(x => println(x))
//13- Correction de la non affichage
rdd.collect.foreach(x =>println(x))
//14-Nombre de partition
rdd.getNumPartitions
//15-Affichage des partitions
val maxValue = rdd.glom().collect.foreach(x =>println(x))
//17 
val part = rdd.partitioner
//18- Taille de la RDD
val count = rdd.count
//19-Afficher les 3 premiers élemnts de la RDD
myList.take(3)
//20-Filtrer les nombres paires
val pairs = rdd.filter(x => x%2 == 0).collect
//21-Somme des elements 
//Avec sum
rdd.sum()
//Avec reduce
rdd.reduce((e1, e2) => e1+e2)
//22-Somme des nombres paires
rdd.filter(x => x%2 == 0).sum
//23-Somme des elements par parité
val rdd3 = rdd.map(f => if(f %2==0)("paire", f) else ("impaire",f)).reduceByKey(_+_)
rdd3.collect.foreach(println)
//23-Nombres d'elements par parité
val rdd4 = rdd.map(f => if(f %2==0)("paire", 1) else ("impaire",1)).reduceByKey(_+_)
rdd4.collect.foreach(println)
//25-Creer liste 
val myList2 = List("Paris FR 5", "Stuttgart DE 0.9", "Lyon FR 2", "Londres UK 8", "Berlin DE 4", "Marseille FR 3", "Liverpool UK 1.5", "Munich DE 1")
//26-Affichage
myList2.foreach(x => println(x))
val rd1 = sc.parallelize(myList2)
//27-Extraction du nom des viles
val rd2 = rd1.map(x=> x.split(" "))
rd2.collect.foreach(x=>println(x(0)))
//28-Extraire les villes françaises
val rd3 = rd1.map(x=> x.split(" ")).filter(w=> w(1) == "FR")
rd3.collect.foreach(x=>println(x(0)))
//29-Extraction du nom de ville avec function
def selectPays (pays:String, rd1:RDD[String]) : RDD[String] = {   

   val rdd1 = rd1.map(x=> x.split(" ")).filter(w => w(1) == pays)
  
   return rdd1
}
val rd4 = selectPays("FR",rd1)
rd4.collect.foreach(x=>println(x(0)))



import org.apache.spark.rdd.RDD
import java.text.SimpleDateFormat
import java.util.Date
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{col, to_date}
//Manip 1
//val empDF1 = spark.read.option("header","true").option("delimiter",";").option("inferSchema",true).csv("/home/komlan/Project_M1/Integration_donnee/datasets/tp3/Employes.csv")
val rawdata = dfReader.option("header","true").option("delimiter",";").option("inferSchema",true).csv("/home/komlan/Project_M1/Integration_donnee/datasets/tp2/Personnel.csv")
rawdata.show
//Manip 2: Convert Dataframe to Dataset
case class Transform(numero: String, nom: String, prenom: String, ddn: String, adresse: String, logement: String)
val dataset = rawdata.as[Transform]

//Manip 3:
//val dataset1 = dataset.select(col("ddn"),to_date(col("ddn"),"dd/MM/yyyy").as("ddn_A")) //Method 1
val dataset1 = dataset.withColumn("ddn", to_date(col("ddn"),"dd/MM/yyyy")) //Method 2
//Mani 4
val dataset2 = dataset1.withColumn("age",year(current_date) - year('ddn))
dataset2.show
//Mani 5
val dataset3 = dataset2.schema.fields.map(head => if(head.dataType == "StringType") ()
val dataset3 = dataset2.withColumn("nom",upper('nom))
dataset3.show

val types = dataset2.schema.fields.map(f => f.dataType)




import java.text.SimpleDateFormat
import java.util.Date
    val DATE_FORMAT = "yyyy/mm/dd"

    def getDateAsString(d: Date): String = {
        val dateFormat = new SimpleDateFormat(DATE_FORMAT)
        dateFormat.format(d)
    }

    def convertStringToDate(s: String): Date = {
        val dateFormat = new SimpleDateFormat(DATE_FORMAT)
        dateFormat.parse(s)
    }
    val date = convertStringToDate("2012/08/15")

    getDateAsString(date)


val data = empDF1.select('nom, 'adresse)
data.show
//Manip 2: Transformer dataframe en dataset
//val data = empDF.

val df = Seq(("2019-07-01"),
    ("2019-06-24"),
    ("2019-11-16"),
    ("2019-11-16")).toDF("input_timestamp")

  //Timestamp String to DateType
  df.withColumn("datetype",
    to_date(col("input_timestamp"),"yyyy-MM-dd"))
    .show()
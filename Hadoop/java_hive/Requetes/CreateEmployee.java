import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;
 
public class CreateEmployee {
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws SQLException, ClassNotFoundException {
   
      // Register driver and create driver instance
      
      Class.forName(driverName);
      // get connection
      Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "", "");
      
      // create statement
      Statement stmt = con.createStatement();
      
      // execute statement
 
         stmt.execute("CREATE TABLE IF NOT EXISTS "
         +" client ( id int, name String )"
         +" ROW FORMAT DELIMITED"
         +" FIELDS TERMINATED BY ','"
         +" LINES TERMINATED BY '\n'"
         +" STORED AS TEXTFILE");
         
      System.out.println("Table client created.");
      con.close();
   }
}
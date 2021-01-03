import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;
 
public class CountEmployee {
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws SQLException, ClassNotFoundException {
   
      // Register driver and create driver instance
      
      Class.forName(driverName);
      // get connection
      Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "", "");
      
      // create statement
      Statement stmt = con.createStatement();
    String tableName = "client"; 
 
   // regular hive query
   String  sql = "select count(1) from " + tableName;
    System.out.println("Running: " + sql);
ResultSet    res = stmt.executeQuery(sql);
    while (res.next()) {
      System.out.println(res.getString(1));
    }   
		 
      System.out.println("Table client chargée.");
      con.close();
   }
}
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;
 
public class SelectEmployee {
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws SQLException, ClassNotFoundException {
   
      // Register driver and create driver instance
      
      Class.forName(driverName);
      // get connection
      Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "", "");
      
      // create statement
      Statement stmt = con.createStatement();
    String tableName = "client"; 
         
    String sql = "select * from " + tableName;
    System.out.println("Running: " + sql);
    ResultSet res = stmt.executeQuery(sql);
    while (res.next()) {
      System.out.println(String.valueOf(res.getInt(1)) + "\t" + res.getString(2));
    }
		 
		 
      System.out.println("Table client chargée.");
      con.close();
   }
}
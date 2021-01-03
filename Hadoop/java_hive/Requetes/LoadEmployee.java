import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;
 
public class LoadEmployee {
   private static String driverName = "org.apache.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws SQLException, ClassNotFoundException {
   
      // Register driver and create driver instance
      
      Class.forName(driverName);
      // get connection
      Connection con = DriverManager.getConnection("jdbc:hive2://localhost:10000/default", "", "");
      
      // create statement
      Statement stmt = con.createStatement();
    String tableName = "client"; 
	String filepath = "/tmp/a.txt";
   String sql = "load data local inpath '" + filepath + "' into table " + tableName;
    System.out.println("Running: " + sql);
    stmt.executeQuery(sql);
         
		 
		 
      System.out.println("Table client chargée.");
      con.close();
   }
}